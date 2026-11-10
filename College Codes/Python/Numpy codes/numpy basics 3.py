import numpy as np

a = np.array([1,2,3])
print(a)
print("Dimensions:", a.ndim, "|",  "Shape:", a.shape)
print()

b = np.array([[1,2,3], [4, 5, 6]])
print(b)
print("Dimensions:", b.ndim, "|",  "Shape:", b.shape)
print()

c = np.array([[[1,2,3], [4, 5, 6], [7, 8, 9]]])
print(c)
print("Dimensions:", c.ndim, "|",  "Shape:", c.shape)
