from typing import (
    Any,
    FrozenSet,
    Tuple,
    Union,
)

# Core scalar and tuple types
Boolean = bool
Integer = int
IntegerTuple = Tuple[Integer, Integer]
Numerical = Union[Integer, IntegerTuple]
IntegerSet = FrozenSet[Integer]

# Grids are immutable tuple-of-tuples of ints
Grid = Tuple[Tuple[Integer, ...], ...]

# Object- and patch-level constructs
Cell = Tuple[Integer, IntegerTuple]
Object = FrozenSet[Cell]
Objects = FrozenSet[Object]
Indices = FrozenSet[IntegerTuple]
IndicesSet = FrozenSet[Indices]
Patch = Union[Object, Indices]
Element = Union[Object, Grid]
Piece = Union[Grid, Patch]

# Generic tuple-of-tuples helper
TupleTuple = Tuple[Tuple[Any, ...], ...]

# Containers used throughout the DSL are either tuples or frozensets
# (we keep them immutable for predictability and hashing)
Container = Union[Tuple[Any, ...], FrozenSet[Any]]
ContainerContainer = Union[FrozenSet[FrozenSet[Any]], Tuple[Tuple[Any, ...], ...]]
