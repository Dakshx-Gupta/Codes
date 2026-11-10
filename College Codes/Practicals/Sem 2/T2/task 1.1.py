import numpy as np

a = np.array([1,2,3])
print(a)
print(a.ndim, a.shape, a.size, a.dtype)
print()

b = np.array([[1,2,3], [4, 5, 6]])
print(b)
print(b.ndim, b.shape, b.size, b.dtype)
print()

c = np.array([[[1,2,3], [4, 5, 6], [7, 8, 9]]])
print(c)
print(c.ndim, c.shape, c.size, c.dtype)
