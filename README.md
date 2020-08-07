# Marshmallow Numpy JSON serializer / deserializer
![Python package](https://github.com/shachakz/marshmallow_numpy/workflows/Python%20package/badge.svg?branch=master)
## Example:
```python
import numpy as np
import marshmallow_dataclass
from marshmallow_numpy import NumpyArray

@marshmallow_dataclass.dataclass
class MyClass:
  my_number: int
  my_numpy_array: NumpyArray
  
if __name__ == "__main__":
  example = MyClass(my_number=5, my_numpy_array=np.zeros((3, 3)))
  schema = marshmallow_dataclass.class_schema(MyClass)()
  print(schema.dump(example))
```
