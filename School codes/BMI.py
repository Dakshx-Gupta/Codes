"""
Created on Sat Oct 28 20:49:29 2023

@author: Daksh

Questions: 
"""

w = int(input("Enter your weight: "))
h = float(input("Enter your height (In meters): "))
b = w/(h**2)
c = round(b, 1)
print("Your BMI is:", c)

if c < 18.5:
    print("Nutritional Status: Underweight")
elif c >= 18.5 and c < 24.9:
    print("Nutritional Status: Normal")
elif c >= 25 and c < 29.9:
    print("Nutritional Status: Overweight") 
elif c >= 30:
    print("Nutritional Status: Obese")
