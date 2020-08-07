import numpy as np
from typing import List, Any, Tuple
from marshmallow import ValidationError
from marshmallow.fields import Field
from dataclasses import dataclass, asdict
from marshmallow_dataclass import NewType


@dataclass
class _NumpyArrayDTO:
    dtype: str
    data: List[Any]


class NumpyField(Field):
    def __init__(
            self, *args, **kwargs
    ):
        super(NumpyField, self).__init__(*args, **kwargs)

    def _serialize(self, value: np.ndarray, *args, **kwargs):
        if value is None:
            return None

        return asdict(_NumpyArrayDTO(dtype=value.dtype.name, data=value.tolist()))

    def _deserialize(self, value, *args, **kwargs):
        if value is None:
            return None

        np_array_obj = _NumpyArrayDTO(**value)

        return np.array(np_array_obj.data, dtype=np.dtype(np_array_obj.dtype))

NumpyArray = NewType("NdArray", np.ndarray, field=NumpyField)

__all__ = [NumpyField, NumpyArray]