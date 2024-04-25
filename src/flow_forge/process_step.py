from typing_extensions import Protocol, runtime_checkable

from flow_forge.custom_typing import P, T


@runtime_checkable
class ProcessStep(Protocol[P, T]):
    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T:
        ...

