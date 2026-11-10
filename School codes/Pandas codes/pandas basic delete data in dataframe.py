"""
Created on Tue Feb 13 08:36:06 2024

@author: tempe

Question:
"""
import pandas as pd
l1 = [{"Name": "Daksh", "Age": "22"}]
df = pd.DataFrame(l1)
df.rename(columns={'Name':'name'},inplace=True)
print(df)
d = input("Enter column name: ")
s = input("Enter the data of the row you want to delete: ")
a = df.index[df[d] == s].tolist()
df = df.drop(a)
print(df)
