import ast
import copy
import sys

from type_check_solvers import check_function_ast


def collect_cast_calls(func: ast.FunctionDef):
    calls = []
    class V(ast.NodeVisitor):
        def visit_Call(self, node: ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id.startswith('cast_') and len(node.args) == 1:
                calls.append((node.func.id, node.lineno, node.col_offset))
            self.generic_visit(node)
    V().visit(func)
    return calls


def remove_one(func: ast.FunctionDef, target):
    cname, ln, col = target
    class R(ast.NodeTransformer):
        def visit_Call(self, node: ast.Call):
            node = self.generic_visit(node)
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Name)
                and node.func.id == cname
                and hasattr(node, 'lineno') and hasattr(node, 'col_offset')
                and node.lineno == ln and node.col_offset == col
                and len(node.args) == 1
            ):
                return node.args[0]
            return node
    newf = copy.deepcopy(func)
    newf = R().visit(newf)
    ast.fix_missing_locations(newf)
    return newf


def strip_redundant_in_func(func: ast.FunctionDef):
    # Iteratively remove redundant casts until stable
    changed = True
    while changed:
        changed = False
        casts = collect_cast_calls(func)
        redundant = []
        for c in casts:
            trial = remove_one(func, c)
            ok, _ = check_function_ast(trial)
            if ok:
                redundant.append(c)
        if redundant:
            # remove all redundant in one pass
            for c in redundant:
                func = remove_one(func, c)
            changed = True
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

