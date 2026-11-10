import pandas as pd
data = {'Name':['Freya', 'Kratos','Loki', 'Freya','Kratos'],'Age':[22, 24, 30, 22, 24]}
d = pd.DataFrame(data)
duplicaterow = d[d.duplicated()]
print(duplicaterow)

