from typing import TypeVar

from typing_extensions import ParamSpec, TypeVarTuple

T = TypeVar("T")
DataType = TypeVar("DataType")
InputDataType = TypeVar("InputDataType")
OutputDataType = TypeVar("OutputDataType")

Ts = TypeVarTuple("Ts")

P: ParamSpec = ParamSpec("P")



