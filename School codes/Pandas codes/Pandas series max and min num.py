"Question: Max and Min num in pandas series and index value of them"

import pandas as pd
u = pd.Series([1, 2, 3, 4])
print("Max num in series: ", max(u))
b1=max(u)
print("Min num in series: ", min(u))
b2=min(u)
print()
print(u)
print()
l=len(u)
for i in range(0,l):
    if u[i]==b1:
        print('Index value of max num: ', i)
    if u[i]==b2:
        print('Index value of min num: ', i)
