import pandas as pd 
import csv

with open('hii.csv', 'r') as file:
    reader = csv.reader(file)
    lib = pd.DataFrame(reader)

l1 = []

a = input("Enter name: ")
b = int(input("Enter age: "))

l1.append([a,b])
d = pd.DataFrame(l1)  
lib = pd.concat([lib, d], ignore_index= True)
lib.to_csv('hii.csv',header=False,  index= False)
print("Data added1")
