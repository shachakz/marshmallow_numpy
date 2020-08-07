import pytest
import numpy as np
from marshmallow import Schema
import marshmallow_dataclass
from dataclasses import dataclass

from marshmallow_numpy import NumpyArray


@dataclass
class TestDTO:
    array: NumpyArray

@pytest.fixture
def schema() -> Schema:
    return marshmallow_dataclass.class_schema(TestDTO)()

def test_dataclass_serialize(schema: Schema):
    res = schema.dump(TestDTO(array=np.zeros((3, 3))))

    assert res == {'array': {'data': [[0.0, 0.0, 0.0],
                                      [0.0, 0.0, 0.0],
                                      [0.0, 0.0, 0.0]],
                             'dtype': 'float64'
                             }
                   }


def test_dataclass_deserialize(schema: Schema):
    res: TestDTO = schema.load({'array': {'data': [[1.0, 1.0, 1.0],
                                                   [1.0, 1.0, 1.0],
                                                   [1.0, 1.0, 1.0]],
                                          'dtype': 'float64'
                                          }
                                })

    assert res.array.tobytes() == np.ones((3, 3)).tobytes()
    assert res.array.dtype == np.dtype('float64')
