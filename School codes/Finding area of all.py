import math
num = []
s1 = []
s = input('Enter the statement of the equation: ')
s1 = s.split()

for x in s1:
  if x.isdigit():
    num.append(x)

for x in s1:
  if x == "circle":
    for x in s1:
      if s1[1] == 'area' or s1[2] == 'area':
        print("Area = ", round((3.14 * int(num[0]) ** 2), 2))
        break
      if s1[1] == 'radius' or s1[2] == 'radius':
        print("Radius =", round(math.sqrt(int(num[0]) // 3.14), 2))
        break
    for x in s1:
      if x == "circumference":
        print("Circumference = ", 2*3.14*int(num[0]))

for x in s1:
  if x == "square":
    for x in s1:
      if s1[1] == 'side' or s1[2] == 'side':
          print("Side of square = ", round(math.sqrt(int(num[0])), 2))
          break
    for x in s1:
      if x == "area":
        print("Area = ", int(num[0])**2)
      if x == "perimeter":
        print("Perimeter = ", 4*int(num[0]))

for x in s1:
  if x == "rectangle":
    for x in s1:
      if x == "area":
        print("Area = ", int(num[0])*int(num[1]))
      if x == "perimeter":
        print("Perimeter = ", 2*(int(num[0])+int(num[1])))

for x in s1:
  if x == "cube":
    for x in s1:
      if s1[1] == 'length' or s1[2] == 'length':
        q = 1/3
        print("Length of cube = ", math.pow((int(num[0])), q))
        break
    for x in s1:
      if x == "area":
        print("Area = ", 6*int(num[0])**2)
      if x == "perimeter":
        print("Perimeter = ", 4*int(num[0])*int(num[1])*int(num[2]))
      if x == "volume":
        print("Volume = ", int(num[0])*int(num[0])*int(num[0]))


for x in s1:
  if x == "cuboid":
    for x in s1:
      if x == "area":
        print("Area = ", (2*int(num[0])*int(num[1]))+(2*int(num[1])*int(num[2]))+(2*int(num[2])*int(num[0])))
      if x == "volume":
        print("Volume = ", int(num[0])*int(num[1])*int(num[2]))

for x in s1:
  if x == "cone":
    for x in s1:
      if x == "volume":
        print("Volume = ", 3.14*int(num[0])**2*int(num[1]))
      if x == "area":
        print("Area = ", 3.14*int(num[0])*(int(num[1])+int(num[0])))

for x in s1:
  if x == "parallelogram":
    for x in s1:
       if s1[5] == 'area' or s1[6] == 'area' or s1[7] == 'area' and s1[1] or s1[2] == 'height':
         print("height of parallelogram = ", int(num[0]) // int(num[1]))
         break
       if s1[5] == 'area' or s1[6] == 'area' or s1[7] == 'area' and s1[1] or s1[2] == 'breadth':
          print("Breadth of parallelogram = ", int(num[0]) // int(num[1]))
          break
       if x == "area":
         print("Area = ", int(num[0])*int(num[1]))
