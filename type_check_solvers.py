import ast
import inspect
import typing

import dsl
import arc_types
import constants as consts


# Collect DSL function signatures and map annotations to simple tags.

DSL_FUNCS = {name: obj for name, obj in dsl.__dict__.items() if inspect.isfunction(obj) and obj.__module__ == dsl.__name__}

# Known arc_types alias names we care about.
ALIAS_NAMES = (
    "Boolean","Integer","IntegerTuple","Numerical","IntegerSet","Grid","Cell",
    "Object","Objects","Indices","IndicesSet","Patch","Element","Piece",
    "TupleTuple","ContainerContainer",
)

ALIAS_MAP = {name: getattr(arc_types, name) for name in ALIAS_NAMES}

CONTAINER_LIKE = {
    "Object","Objects","Indices","IndicesSet","IntegerSet","Tuple","TupleTuple",
    "Container","ContainerContainer","Grid","Patch",
}


def ann_to_tags(ann) -> typing.Set[str]:
    """Convert a typing annotation into a set of simple tag names."""
    if ann is None:
        return {"Unknown"}
    if ann is typing.Any:
        return {"Any"}
    # Callable, Container
    origin = typing.get_origin(ann)
    if origin is typing.Callable:
        return {"Callable"}
    if origin is typing.Union:
        tags = set()
        for arg in typing.get_args(ann):
            tags |= ann_to_tags(arg)
        return tags
    # Direct alias equality
    for name, alias in ALIAS_MAP.items():
        if ann == alias:
            return {name}
    # Builtins
    if ann is int:
        return {"Integer"}
    if ann is bool:
        return {"Boolean"}
    # Fallback for typing.Tuple
    if origin is tuple:
        args = typing.get_args(ann)
        # IntegerTuple commonly appears as Tuple[int, int]
        if len(args) == 2 and args[0] is int and args[1] is int:
            return {"IntegerTuple"}
        # Grid commonly appears as Tuple[Tuple[int]] (loose in this codebase)
        if len(args) == 1 and typing.get_origin(args[0]) is tuple:
            inner = typing.get_args(args[0])
            if len(inner) == 1 and inner[0] is int:
                return {"Grid"}
        return {"Tuple"}
    # typing.Container
    if ann is typing.Container or origin is typing.Container:
        return {"Container"}
    return {"Unknown"}


def build_dsl_signature_table():
    table = {}
    for name, fn in DSL_FUNCS.items():
        try:
            hints = typing.get_type_hints(fn, globalns=dsl.__dict__)
        except Exception:
            hints = getattr(fn, "__annotations__", {}) or {}
        params = []
        sig = inspect.signature(fn)
        for p in sig.parameters.values():
            params.append(ann_to_tags(hints.get(p.name)))
        ret = ann_to_tags(hints.get("return"))
        table[name] = {"params": params, "return": ret}
    return table


DSL_SIGS = build_dsl_signature_table()


def const_name_to_tag(name: str) -> typing.Set[str]:
    if not hasattr(consts, name):
        return {"Unknown"}
    val = getattr(consts, name)
    if isinstance(val, bool):
        return {"Boolean"}
    if isinstance(val, int):
        return {"Integer"}
    if isinstance(val, tuple) and len(val) == 2 and all(isinstance(x, int) for x in val):
        return {"IntegerTuple"}
    return {"Unknown"}


def is_compatible(actual: typing.Set[str], expected: typing.Set[str]) -> bool:
    if "Any" in expected or "Any" in actual:
        return True
    if not expected or "Unknown" in expected:
        return True
    # Handle unions
    if expected & actual:
        return True
    # Special unions
    if "Numerical" in expected and ("Integer" in actual or "IntegerTuple" in actual):
        return True
    if "Patch" in expected and ("Object" in actual or "Indices" in actual):
        return True
    if "Element" in expected and ("Grid" in actual or "Object" in actual):
        return True
    if "Piece" in expected and ("Grid" in actual or "Patch" in actual or "Object" in actual or "Indices" in actual):
        return True
    if "Container" in expected and (actual & CONTAINER_LIKE):
        return True
    if "Callable" in expected and "Callable" in actual:
        return True
    return False


class TypeEnv:
    def __init__(self):
        self.env = {"I": {"Grid"}}

    def get(self, name: str) -> typing.Set[str]:
        if name in self.env:
            return self.env[name]
        if name in DSL_FUNCS:
            return {"Callable"}
        # constants
        if hasattr(consts, name):
            return const_name_to_tag(name)
        return {"Unknown"}

    def set(self, name: str, tags: typing.Set[str]):
        self.env[name] = tags


class TypeErrorInfo(Exception):
    pass


def expr_type(node: ast.AST, tenv: TypeEnv) -> typing.Set[str]:
    if isinstance(node, ast.Name):
        return tenv.get(node.id)
    if isinstance(node, ast.Call):
        # function part
        if isinstance(node.func, ast.Name):
            fname = node.func.id
            # DSL function
            if fname in DSL_SIGS:
                sig = DSL_SIGS[fname]
                # positional args first
                arg_types = [expr_type(arg, tenv) for arg in node.args]
                # map keyword args by parameter order
                if node.keywords:
                    # merge keywords into appropriate positions if possible
                    param_names = list(inspect.signature(DSL_FUNCS[fname]).parameters.keys())
                    name_to_index = {p: i for i, p in enumerate(param_names)}
                    # extend arg_types to full length
                    while len(arg_types) < len(param_names):
                        arg_types.append({"Unknown"})
                    for kw in node.keywords:
                        if kw.arg in name_to_index:
                            arg_types[name_to_index[kw.arg]] = expr_type(kw.value, tenv)
                # check arity (best effort)
                for i, expected in enumerate(sig["params"]):
                    if i >= len(arg_types):
                        raise TypeErrorInfo(f"{fname}: missing argument at position {i}")
                    actual = arg_types[i]
                    if not is_compatible(actual, expected):
                        raise TypeErrorInfo(f"{fname}: argument {i} has type {sorted(actual)} but expected {sorted(expected)}")
                return sig["return"]
            else:
                # calling a value (likely a Callable)
                ftype = tenv.get(fname)
                if "Callable" not in ftype:
                    raise TypeErrorInfo(f"Attempting to call non-callable '{fname}' of type {sorted(ftype)}")
                # We do not know return type; treat as Any
                # but verify the arguments are at least well-typed constants/known names
                for arg in node.args:
                    expr_type(arg, tenv)
                return {"Any"}
        else:
            # complex call, just walk args
            for arg in node.args:
                expr_type(arg, tenv)
            return {"Any"}
    # constants: not expected in solvers; treat as Unknown
    return {"Unknown"}


def check_solver(fn) -> typing.Tuple[bool, str]:
    src = inspect.getsource(fn)
    tree = ast.parse(src)
    tenv = TypeEnv()
    try:
        for stmt in tree.body[0].body:  # FunctionDef body
            if isinstance(stmt, ast.Assign) and len(stmt.targets) == 1:
                target = stmt.targets[0]
                if isinstance(target, ast.Name):
                    t = expr_type(stmt.value, tenv)
                    tenv.set(target.id, t)
            elif isinstance(stmt, ast.Return):
                # ensure return variable is Grid when returning O
                if isinstance(stmt.value, ast.Name) and stmt.value.id == "O":
                    ot = tenv.get("O")
                    if not is_compatible(ot, {"Grid"}):
                        raise TypeErrorInfo(f"Return 'O' has type {sorted(ot)}; expected ['Grid']")
                else:
                    # compute return type
                    _ = expr_type(stmt.value, tenv)
        return True, ""
    except TypeErrorInfo as e:
        return False, str(e)
    except Exception as e:
        return False, f"Unexpected error: {e}"


def check_function_ast(func_node: ast.FunctionDef) -> typing.Tuple[bool, str]:
    tenv = TypeEnv()
    try:
        for stmt in func_node.body:
            if isinstance(stmt, ast.Assign) and len(stmt.targets) == 1:
                target = stmt.targets[0]
                if isinstance(target, ast.Name):
                    t = expr_type(stmt.value, tenv)
                    tenv.set(target.id, t)
            elif isinstance(stmt, ast.Return):
                if isinstance(stmt.value, ast.Name) and stmt.value.id == "O":
                    ot = tenv.get("O")
                    if not is_compatible(ot, {"Grid"}):
                        raise TypeErrorInfo(f"Return 'O' has type {sorted(ot)}; expected ['Grid']")
                else:
                    _ = expr_type(stmt.value, tenv)
        return True, ""
    except TypeErrorInfo as e:
        return False, str(e)
    except Exception as e:
        return False, f"Unexpected error: {e}"


def find_redundant_casts_in_src(src: str) -> typing.List[typing.Tuple[str, int, int]]:
    tree = ast.parse(src)
    func: ast.FunctionDef = tree.body[0]  # solvers are simple single-def sources
    casts = []

    class CastCollector(ast.NodeVisitor):
        def visit_Call(self, node: ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id.startswith('cast_') and len(node.args) == 1:
                casts.append((node.func.id, node.lineno, node.col_offset))
            self.generic_visit(node)

    CastCollector().visit(func)

    redundant = []

    for cname, ln, col in casts:
        class RemoveOne(ast.NodeTransformer):
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

        mutated = ast.Module(body=[RemoveOne().visit(func)], type_ignores=[])
        ast.fix_missing_locations(mutated)
        ok, _ = check_function_ast(mutated.body[0])
        if ok:
            redundant.append((cname, ln, col))
    return redundant


def check_redundant_casts_report(solvers_module) -> typing.List[typing.Tuple[str, str, int, int]]:
    names = [n for n in dir(solvers_module) if n.startswith("solve_") and callable(getattr(solvers_module, n))]
    redundancies = []
    for name in sorted(names):
        src = inspect.getsource(getattr(solvers_module, name))
        reds = find_redundant_casts_in_src(src)
        for cname, ln, col in reds:
            redundancies.append((name, cname, ln, col))
    return redundancies


def main():
    import solvers
    solver_names = [n for n in dir(solvers) if n.startswith("solve_") and callable(getattr(solvers, n))]
    total = len(solver_names)
    passed = 0
    failures = []
    for name in sorted(solver_names):
        ok, msg = check_solver(getattr(solvers, name))
        if ok:
            passed += 1
        else:
            failures.append((name, msg))
    print(f"Type check passed: {passed}/{total}")
    if failures:
        for name, msg in failures:
            print(f"FAIL {name}: {msg}")
    # Redundant casts report
    reds = check_redundant_casts_report(solvers)
    if reds:
        print(f"Redundant casts found: {len(reds)}")
        for fn, cname, ln, col in reds[:100]:
            print(f"REDUNDANT {fn}:{ln}:{col} -> {cname}")
    else:
        print("No redundant casts detected.")


if __name__ == "__main__":
    main()
