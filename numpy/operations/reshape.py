import numpy as np

## Reshape
# numpy.reshape(array, shape, order)

# create an array
a = np.array([0, 1, 2, 3, 4, 5, 6, 7])

# reshape the array
b = np.reshape(a, (2, 4))

print(b)
