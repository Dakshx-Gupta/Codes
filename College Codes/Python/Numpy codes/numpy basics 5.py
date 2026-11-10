import numpy as np
l1 = []
n = int(input("Enter the number of elements to enter in the list: "))
for i in range(0, n):
    x =  int(input("Enter values: "))
    l1.append(x)

a = np.array(l1)
# print(a)
b = np.reshape(a, (3, 2))
print("2D Array")
print(b)
print("Dimensions: ", b.ndim)
print("Shape: ", b.shape)
print("Size: ", b.size)
print("Data Type: ", b.dtype)
print("Itemsize: ", b.itemsize)

print()
c = np.ones(shape = (3, 2), dtype = int)
d = b + c
print(d)
