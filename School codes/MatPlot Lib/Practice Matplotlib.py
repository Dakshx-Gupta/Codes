from matplotlib import pyplot as pl
import pandas as pd
names = pd.Series(['Kratos','Freya','Loki','Odin'])
age = pd.Series([40,60,80,90])
pl.bar(names,age, color = 'Red')
pl.title("Name and Age of different characters ")
pl.xlabel("Names")
pl.ylabel("Age")
pl.show()
