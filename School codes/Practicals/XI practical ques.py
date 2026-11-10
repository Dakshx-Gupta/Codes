"""
Created on Wed Feb 21 09:19:51 2024

@author: tempe

Question:
"""
l1 = [] #two empty list, l1 stores even value and l2 odd values
l2 = []
x = input("Enter number: ") #taking input from user
for i in x: #running a loop to find the even and odd digits in the value
    f = int(i)
    if f%2 == 0:
        l1.append(i) #even values in l1
    else:
        l2.append(i) #odd values in l2
print()
a = len(l1) #len() function to find the number of even digits
b = len(l2) #len() function to find the number of odd digits

#code for output below
print("Number of even values:", a)
print("Number of odd values:", b)
print()
print("Even numbers in the value:",l1)
print()
print("Odd numbers in the value:", l2)
