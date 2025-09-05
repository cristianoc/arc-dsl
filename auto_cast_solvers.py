import ast
import io
import sys


CASTS = {
    'mapply': [('ContainerContainer', 1)],
    'apply': [('Container', 1)],
    'merge': [('ContainerContainer', 0)],
    'fill': [('Patch', 2)],
    'underfill': [('Patch', 2)],
    'paint': [('Grid', 0), ('Object', 1)],
    'shift': [('Patch', 0)],
    'move': [('Object', 1)],
    'argmax': [('Container', 0)],
    'argmin': [('Container', 0)],
    'first': [('Container', 0)],
    'last': [('Container', 0)],
    'sfilter': [('Container', 0)],
    'mfilter': [('Container', 0)],
    'remove': [('Container', 1)],
    'product': [('Container', 0), ('Container', 1)],
    'papply': [('Tuple', 1), ('Tuple', 2)],
    'prapply': [('Container', 1), ('Container', 2)],
    'mpapply': [('Tuple', 1), ('Tuple', 2)],
    'pair': [('Tuple', 0), ('Tuple', 1)],
    'cover': [('Grid', 0), ('Patch', 1)],
    'subgrid': [('Patch', 0), ('Grid', 1)],
    'recolor': [('Patch', 1)],
    'center': [('Patch', 0)],
    'ulcorner': [('Patch', 0)],
    'urcorner': [('Patch', 0)],
    'llcorner': [('Patch', 0)],
    'lrcorner': [('Patch', 0)],
    'toindices': [('Patch', 0)],
    'normalize': [('Patch', 0)],
    'delta': [('Indices', 0)],
    'size': [('Container', 0)],
    'combine': [('Container', 0), ('Container', 1)],
    'astuple': [('Integer', 0), ('Integer', 1)],
    'crop': [('Grid', 0)],
    'mostcolor': [('Element', 0)],
    'switch': [('Grid', 0)],
    'hmirror': [('Grid', 0)],
    'vmirror': [('Grid', 0)],
    'dmirror': [('Grid', 0)],
    'cmirror': [('Grid', 0)],
    'rot90': [('Grid', 0)],
    'rot180': [('Grid', 0)],
    'rot270': [('Grid', 0)],
    'hconcat': [('Grid', 0), ('Grid', 1)],
    'vconcat': [('Grid', 0), ('Grid', 1)],
    'width': [('Patch', 0)],
    'height': [('Patch', 0)],
    'shape': [('Patch', 0)],
    'portrait': [('Patch', 0)],
    'occurrences': [('Grid', 0), ('Object', 1)],
    'gravitate': [('Patch', 0), ('Patch', 1)],
    'outbox': [('Patch', 0)],
    'inbox': [('Patch', 0)],
    'box': [('Patch', 0)],
    'backdrop': [('Patch', 0)],
    'position': [('Patch', 0), ('Patch', 1)],
    'palette': [('Element', 0)],
    'colorfilter': [('Objects', 0)],
    'replace': [('Grid', 0)],
    'upscale': [('Element', 0)],
    'hupscale': [('Grid', 0)],
    'vupscale': [('Grid', 0)],
    'ofcolor': [('Grid', 0)],
    'partition': [('Grid', 0)],
    'canvas': [('IntegerTuple', 1)],
    'underpaint': [('Grid', 0), ('Object', 1)],
    'toobject': [('Patch', 0), ('Grid', 1)],
    'order': [('Container', 0)],
    'dedupe': [('Tuple', 0)],
    'minimum': [('IntegerSet', 0)],
    'maximum': [('IntegerSet', 0)],
    'extract': [('Container', 0)],
    'increment': [('Integer', 0)],
    'decrement': [('Integer', 0)],
    'color': [('Object', 0)],
    'corners': [('Patch', 0)],
}


def cast_call(tag: str, node: ast.AST) -> ast.Call:
    return ast.Call(func=ast.Name(id=f'cast_{tag}', ctx=ast.Load()), args=[node], keywords=[])


class Rewriter(ast.NodeTransformer):
    def visit_Assign(self, node: ast.Assign) -> ast.AST:
        self.generic_visit(node)
        if len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) and node.targets[0].id == 'O':
            node.value = cast_call('Grid', node.value)
        return node
    def visit_Call(self, node: ast.Call) -> ast.AST:
        self.generic_visit(node)
        # Wrap calls through local temp names like x5, m3, f7 as Callable
        if isinstance(node.func, ast.Name) and len(node.func.id) >= 2 and node.func.id[0].islower() and node.func.id[1:].isdigit():
            node.func = ast.Call(func=ast.Name(id='cast_Callable', ctx=ast.Load()), args=[node.func], keywords=[])

        # Handle specific DSL functions argument casts
        if isinstance(node.func, ast.Name):
            fname = node.func.id
            if fname in CASTS:
                # Ensure list of args long enough (ignore keywords; solvers use positional mostly)
                args = list(node.args)
                for tag, idx in CASTS[fname]:
                    if idx < len(args):
                        args[idx] = cast_call(tag, args[idx])
                node.args = args
        return node


def main(path: str):
    src = open(path, 'r').read()
    tree = ast.parse(src)
    new_tree = Rewriter().visit(tree)
    ast.fix_missing_locations(new_tree)
    new_src = ast.unparse(new_tree)
    with open(path, 'w') as f:
        f.write(new_src + ("\n" if not new_src.endswith('\n') else ''))


if __name__ == '__main__':
    p = sys.argv[1] if len(sys.argv) > 1 else 'solvers.py'
    main(p)
