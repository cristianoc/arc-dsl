import ast
import sys


class DedupCasts(ast.NodeTransformer):
    def visit_Call(self, node: ast.Call):
        node = self.generic_visit(node)
        if isinstance(node.func, ast.Name) and node.func.id.startswith('cast_') and node.args:
            # Collapse nested identical casts: cast_X(cast_X(expr)) -> cast_X(expr)
            inner = node.args[0]
            while (
                isinstance(inner, ast.Call)
                and isinstance(inner.func, ast.Name)
                and inner.func.id == node.func.id
                and len(inner.args) == 1
            ):
                inner = inner.args[0]
            node.args[0] = inner
        return node


def main(path: str):
    src = open(path, 'r').read()
    tree = ast.parse(src)
    new_tree = DedupCasts().visit(tree)
    ast.fix_missing_locations(new_tree)
    new_src = ast.unparse(new_tree)
    with open(path, 'w') as f:
        f.write(new_src + ("\n" if not new_src.endswith('\n') else ''))


if __name__ == '__main__':
    p = sys.argv[1] if len(sys.argv) > 1 else 'solvers.py'
    main(p)

