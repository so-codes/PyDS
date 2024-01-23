import numpy as np

# 1 D 
a = np.array([1, 2, 3, 4, 5, 6,7,8,9])

print("1D \n",np.where(a %2 != 0, -1, a), "\n\n")

# 2 D
b = np.array([[1, 2, 3], [4, 5, 6]])

print("2D \n",np.where(b %2 != 0, -1, b), "\n\n")

# 3 D
c = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print("3D \n", np.where(c %2 != 0, -1, c), "\n")

