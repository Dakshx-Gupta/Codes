import pandas as pd
dic = [{"Name": "Daksh", "Age": "12"},{"Name": "Aadhyan","Age": "13"}]
df = pd.DataFrame(dic)
print(df)
a = int(input("Enter the index value of row: "))
b = int(input("Enter the index value of the column: "))
print(df.iloc[a, b])
