"""Random utility functions."""
from functools import wraps, partial
from typing import Callable, TypeVar, Any, Iterable

from typing_extensions import Concatenate, TypeVarTuple, Unpack, ParamSpec

from flow_forge.custom_typing import P, T

T1 = TypeVar("T1")
T2 = TypeVar("T2")

Ts1 = TypeVarTuple("Ts1")
Ts2 = TypeVarTuple("Ts2")


P1 = ParamSpec("P1")
P2 = ParamSpec("P2")


def compose(fn1: Callable[P1, T1], fn2: Callable[Concatenate[T1, P1], T2]) -> Callable[P1, T2]:
    def composed_fn(*args: P1.args, **kwargs: P1.kwargs) -> T2:
        return fn2(fn1(*args, **kwargs), *args, **kwargs)
    return composed_fn


def add_two(x: int, y: int, *args, **kwargs) -> int:
    return x + 2 * y


def add_three(x: int, *args, **kwargs) -> int:
    return x + 3


new_func = compose(add_two, add_three)


if __name__ == '__main__':
    print(compose(add_two, add_three)(1, ))







