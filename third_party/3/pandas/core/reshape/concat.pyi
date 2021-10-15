from typing import Any, Mapping, overload, Sequence, Union

from pandas import DataFrame as DataFrame, Series as Series
from pandas._typing import AxisOptionHorizontal, AxisOptionVertical, FrameOrSeries, Label


# For some reason mypy won't read this declaration correctly if we use 2 overloads with union
# It's complicated to read so citing the docs:
# "When concatenating all Series along the index (axis=0), a Series is returned. When objs contains at least one DataFrame,
# a DataFrame is returned. When concatenating along the columns (axis=1), a DataFrame is returned."
@overload
def concat(objs: Union[Sequence[Series], Mapping[Label, Series]], axis: AxisOptionHorizontal = ..., join: str=..., ignore_index: bool=..., keys: Any = ..., levels: Any = ..., names: Any = ..., verify_integrity: bool=..., sort: bool=..., copy: bool=...) -> Series: ...
@overload
def concat(objs: Union[Sequence[DataFrame], Mapping[Label, DataFrame]], axis: AxisOptionHorizontal = ..., join: str=..., ignore_index: bool=..., keys: Any = ..., levels: Any = ..., names: Any = ..., verify_integrity: bool=..., sort: bool=..., copy: bool=...) -> DataFrame: ...
@overload
def concat(objs: Union[Sequence[FrameOrSeries], Mapping[Label, FrameOrSeries]], axis: AxisOptionVertical, join: str=..., ignore_index: bool=..., keys: Any = ..., levels: Any = ..., names: Any = ..., verify_integrity: bool=..., sort: bool=..., copy: bool=...) -> DataFrame: ...

class _Concatenator:
    intersect: bool = ...
    objs: Any = ...
    axis: Any = ...
    keys: Any = ...
    names: Any = ...
    levels: Any = ...
    sort: Any = ...
    ignore_index: Any = ...
    verify_integrity: Any = ...
    copy: Any = ...
    new_axes: Any = ...
    def __init__(self, objs: Any, axis: Any = ..., join: str=..., keys: Any = ..., levels: Any = ..., names: Any = ..., ignore_index: bool=..., verify_integrity: bool=..., copy: bool=..., sort: Any = ...) -> None: ...
    def get_result(self) -> Any: ...
