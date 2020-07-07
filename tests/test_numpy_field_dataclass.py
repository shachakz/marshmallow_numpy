from dataclasses import dataclass, field, asdict

import marshmallow_dataclass
import numpy as np
import pytest
from marshmallow import Schema

from marshmallow_numpy import NumpyField


@dataclass
class TestDTO:
    array: np.array = field(metadata={'marshmallow_field': NumpyField()})

@pytest.fixture
def schema() -> Schema:
    return marshmallow_dataclass.class_schema(TestDTO)()

def test_dataclass_serialize(schema: Schema):
    res = schema.dump(TestDTO(array=np.zeros((3, 3))))

    assert res == {'array': {'data': [[0.0, 0.0, 0.0],
                                      [0.0, 0.0, 0.0],
                                      [0.0, 0.0, 0.0]],
                             'dtype': np.dtype('float64')
                             }
                   }


def test_dataclass_deserialize(schema: Schema):
    res: TestDTO = schema.load({'array': {'data': [[1.0, 1.0, 1.0],
                                                   [1.0, 1.0, 1.0],
                                                   [1.0, 1.0, 1.0]],
                                          'dtype': np.dtype('float64')
                                          }
                                })

    assert res.array.tobytes() == np.ones((3, 3)).tobytes()
