import pandas as pd 
import csv

with open('hii.csv', 'r') as file:
    reader = csv.reader(file)
    lib = pd.DataFrame(reader)
    
print(lib)
