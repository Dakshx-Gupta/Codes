"Question: Max and Min num index in pandas dataframe"

import pandas as pd
df = pd.DataFrame({"A":[4, 5, 2, 6],
                   "B":[11, 2, 5, 8],
                   "c":[1, 8, 66, 4]})
print("DataFrame")
print(df)
print()
d1 = df.idxmax(axis=0)
d2 = df.idxmin(axis=0)
print("Max numbers in DataFrame")
print(d1)
print()
print("Min number in DataFrame")
print(d2)
