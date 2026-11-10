#Question - "Median of two sorted list"

l1 = []
l2 = []
l3 = []
l4 = []
e = int(input("Number of elements in list 1: "))
f = int(input("Number of elements in list 2: "))

print("Enter values for list 1")
for i in range(0,e):
    x = int(input("Enter the values: "))
    l1.append(x)
    l3.append(x)
  
print()
print("Enter values for list 2")
for iu in range(0,f):
    xo = int(input("Enter the values: "))
    l2.append(xo)
    l3.append(xo)
l1.sort()
l2.sort()
l3.sort()
print(l3)
j = len(l3)
if j % 2 == 0:
    v = (j//2)-1
    h = (j//2)
    for i in range(0, len(l3)):
        if i == v:
            l4.append(l3[i])
    for i in range(0, len(l3)):
        if i == h:
            l4.append(l3[i])
            c = sum(l4)
            w = c/2
            print(w)
if j % 2 != 0:
    v = j+1
    f = (v/2)-1
    for i in range(0, len(l3)):
        if i == f:
            print(l3[i])
