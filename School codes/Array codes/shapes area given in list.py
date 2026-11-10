'''
Question - In this code, we give users a choice to select a shape they like and then find the area of that shape
'''
l1 = ["Square", "Cube", "Rectangle"]
print("Name of shapes: ", l1)
x = int(input("Which shape area you want to find (Enter Index (Starts from 0)): "))
if x == 0:
    s = int(input("Enter side of square: "))
    a = s*s
    print("Area: ", a)
if x == 1:
    s = int(input("Enter side of cube: "))
    a = s*s*s
    print("Area: ", a)
if x == 2:
    l = int(input("Enter length: "))
    b = int(input("Enter breadth: "))
    a = l*b
    print("Area: ", a)
