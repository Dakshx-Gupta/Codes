'''
Question - In this code, we check if a year is a leap year or not, 
the components required to check whether a year is a leap year are stored in list 
and we cannot use loop
'''
l1 = [4, 100, 400]
x = input("Enter year: ")
if int(x) % l1[0] == 0:
    print("Leap year")
else:
    print("not leap year")

if int(x) % l1[1] == 0:
    if int(x) % l1[2] == 0:
        print("Leap year")
    else:
        print("Not leap year") 
