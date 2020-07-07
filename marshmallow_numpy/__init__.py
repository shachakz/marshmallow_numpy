import numpy as np
from typing import List, Any
from marshmallow.fields import Field
from dataclasses import dataclass, asdict


@dataclass
class _NumpyArrayDTO:
    dtype: str
    data: List[Any]


class NumpyField(Field):
    def __init__(
            self, *args, **kwargs
    ):
        super(NumpyField, self).__init__(*args, **kwargs)

    def _serialize(self, value: np.array, *args, **kwargs):
        if value is None:
            return None

        return asdict(_NumpyArrayDTO(dtype=value.dtype, data=value.tolist()))

    def _deserialize(self, value, *args, **kwargs):
        if value is None:
            return None

        np_array_obj = _NumpyArrayDTO(**value)

        return np.array(np_array_obj.data, dtype=np_array_obj.dtype)
