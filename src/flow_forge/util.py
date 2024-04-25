"""Random utility functions."""
from functools import wraps, partial
from typing import Callable, TypeVar, Any, Iterable

from pygments.lexers import q
from typing_extensions import Concatenate, TypeVarTuple, Unpack, ParamSpec

from flow_forge.custom_typing import P, T

T1 = TypeVar("T1")
T2 = TypeVar("T2")

Ts1 = TypeVarTuple("Ts1")
Ts2 = TypeVarTuple("Ts2")

P1 = ParamSpec("P1")
P2 = ParamSpec("P2")


def compose(fn1: Callable[P1, T1], fn2: Callable[[T1, ...], T2]) -> Callable[P1, T2]:
    @wraps(fn1)
    def composition(*args: P1.args, **kwargs: P1.kwargs) -> T2:
        return fn2(fn1(*args, **kwargs), *args, **kwargs)
    return composition


def add_two(x: int, y: int, *args, **kwargs) -> int:
    return x + 2 * y


def add_three(x: int, *args, **kwargs) -> int:
    return x + 3


class Foo:
    def __call__(self, x: int, *args, **kwargs):
        return x + 2


class Bar:
    def __call__(self, x: int, *args, **kwargs):
        return x + 6


class Baz:
    __call__ = compose(Bar(), Foo())


if __name__ == '__main__':
    print(Baz()(2))

