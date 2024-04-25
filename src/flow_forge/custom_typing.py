from typing import TypeVar

from typing_extensions import ParamSpec, TypeVarTuple

T: TypeVar = TypeVar("T")
T2: TypeVar = TypeVar("T2")
T_co: TypeVar = TypeVar("T_co", covariant=True)
DataType: TypeVar = TypeVar("DataType")
InputDataType: TypeVar = TypeVar("InputDataType")
OutputDataType: TypeVar = TypeVar("OutputDataType")

Ts: TypeVarTuple = TypeVarTuple("Ts")

P: ParamSpec = ParamSpec("P")
P2: ParamSpec = ParamSpec("P2")



