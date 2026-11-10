"""
Created on Wed Feb 21 09:43:51 2024

@author: tempe

Question:
"""

def push(): #creating function push()
    print("A program to find the odd value in the list and then print it in reverse order") #taking input
    print()
    l1 = []
    for i in range(0, 5):
        v = int(input("Enter 4 even values and 1 odd value: "))
        l1.append(v)
    for i in l1: #running a loop to find the odd value
        if i%2 != 0: #if i is not divisible by 2 then print that value
            print("Odd value in the list:", i) #odd value in list
    print(l1)
    print("List in reverse order:", l1[::-1]) #list in reverse order
push() #calling the function
