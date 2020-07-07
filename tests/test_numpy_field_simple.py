import pytest
import numpy as np
from marshmallow_numpy import NumpyField


@pytest.fixture()
def field() -> NumpyField:
    return NumpyField()


def test_field_serialize(field: NumpyField):
    res = field._serialize(np.zeros((3, 3)))
    assert res == {'data': [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], 'dtype': np.dtype('float64')}


def test_field_deserialize(field: NumpyField):
    res = field._deserialize({'data': [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]], 'dtype': np.dtype('float64')})
    assert res.data == np.ones((3, 3)).data
