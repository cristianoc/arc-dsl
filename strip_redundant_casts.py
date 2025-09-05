import ast
import copy
import sys
from typing import List, Tuple, Set

from type_check_solvers import (
    DSL_SIGS,
    TypeEnv,
    expr_type,
    is_compatible,
    check_function_ast,
)


def expected_param_tags(call: ast.Call, idx: int) -> Set[str]:
    if isinstance(call.func, ast.Name):
        fname = call.func.id
        if fname in DSL_SIGS:
            params = DSL_SIGS[fname]["params"]
            if 0 <= idx < len(params):
                return params[idx]
    return {"Unknown"}


def cast_name(node: ast.AST) -> Tuple[str, ast.AST]:
    """If node is cast_* call with one arg, return (cast_name, inner)."""
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
        fname = node.func.id
        if fname.startswith("cast_") and len(node.args) == 1:
            return fname, node.args[0]
    return "", node


def try_remove_in_call_args(func_node: ast.FunctionDef) -> Tuple[ast.FunctionDef, bool]:
    """Remove redundant casts in function-call arguments using local type info."""
    changed_any = False
    # Work on a deep copy to allow rollback per edit
    fn = copy.deepcopy(func_node)
    env = TypeEnv()

    new_body = []
    for stmt in fn.body:
        # Transformer for a single statement, capturing env and accumulating edits
        class ArgStripper(ast.NodeTransformer):
            def visit_Call(self, node: ast.Call):
                # Process children first
                node = self.generic_visit(node)
                # cast_Callable(f)(...) -> f(...) when f is Callable
                if isinstance(node.func, ast.Call):
                    cname, inner = cast_name(node.func)
                    if cname == 'cast_Callable':
                        itags = expr_type(inner, env)
                        if 'Callable' in itags:
                            node.func = inner
                            # mark change
                            setattr(node, '_changed_by_stripper', True)

                # For positional args: cast_* wrappers that are statically compatible
                if isinstance(node.func, ast.Name) and node.func.id in DSL_SIGS:
                    fname = node.func.id
                    args = list(node.args)
                    for i, a in enumerate(args):
                        cname, inner = cast_name(a)
                        if not cname:
                            continue
                        expected = expected_param_tags(node, i)
                        if expected and 'Unknown' not in expected:
                            actual = expr_type(inner, env)
                            if is_compatible(actual, expected):
                                args[i] = inner
                                # mark change on node
                                setattr(node, '_changed_by_stripper', True)
                    node.args = args
                return node

        # Apply transformer to this statement
        new_stmt = ArgStripper().visit(copy.deepcopy(stmt))
        ast.fix_missing_locations(new_stmt)

        # Proactively verify function still type-checks after this one-statement edit
        trial_fn = copy.deepcopy(fn)
        trial_fn.body = new_body + [new_stmt] + fn.body[len(new_body)+1:]
        ok, _ = check_function_ast(trial_fn)
        if ok:
            # Accept the new statement and update env accordingly
            new_body.append(new_stmt)
            # If this statement or any nested calls were changed, reflect in flag
            if hasattr(new_stmt, '_changed_by_stripper'):
                changed_any = True
            # Update env with this statement's assignments
            if isinstance(new_stmt, ast.Assign) and len(new_stmt.targets) == 1 and isinstance(new_stmt.targets[0], ast.Name):
                t = new_stmt.targets[0].id
                tags = expr_type(new_stmt.value, env)
                env.set(t, tags)
            elif isinstance(new_stmt, ast.AnnAssign) and isinstance(new_stmt.target, ast.Name) and new_stmt.value is not None:
                t = new_stmt.target.id
                tags = expr_type(new_stmt.value, env)
                env.set(t, tags)
        else:
            # Reject this change; keep original statement, and update env based on original
            new_body.append(stmt)
            if isinstance(stmt, ast.Assign) and len(stmt.targets) == 1 and isinstance(stmt.targets[0], ast.Name):
                t = stmt.targets[0].id
                tags = expr_type(stmt.value, env)
                env.set(t, tags)
            elif isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name) and stmt.value is not None:
                t = stmt.target.id
                tags = expr_type(stmt.value, env)
                env.set(t, tags)

    fn.body = new_body
    ast.fix_missing_locations(fn)
    return fn, changed_any


def strip_redundant_in_func(func: ast.FunctionDef) -> ast.FunctionDef:
    # Iterate until stable or no more safe changes
    iterations = 0
    while True:
        iterations += 1
        newf, changed = try_remove_in_call_args(func)
        if not changed:
            return func
        ok, _ = check_function_ast(newf)
        if ok:
            func = newf
        else:
            # If any iteration produces a non-type-checking function, stop
            return func


def main(path: str):
    src = open(path, 'r').read()
    tree = ast.parse(src)
    new_body = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name.startswith('solve_'):
            node = strip_redundant_in_func(node)
        new_body.append(node)
    tree.body = new_body
    ast.fix_missing_locations(tree)
    new_src = ast.unparse(tree)
    with open(path, 'w') as f:
        f.write(new_src + ("\n" if not new_src.endswith('\n') else ''))


if __name__ == '__main__':
    p = sys.argv[1] if len(sys.argv) > 1 else 'solvers.py'
    main(p)
