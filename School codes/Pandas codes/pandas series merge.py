"""
Created on Sun Dec 10 23:37:26 2023

@author: tempe

Question: Merge two series 
"""

import pandas as pd

a = pd.Series([1, 2, 3, 4, 5])
b = pd.Series([1, 5, 7, 9, 4])
c = pd.concat([a,b], ignore_index=True)
print(c)
