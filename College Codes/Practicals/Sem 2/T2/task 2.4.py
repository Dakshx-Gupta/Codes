import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
'salary': [100000, 30000, 50000, 70000],
'attendance': [60,70,80,85],
'experince': [7, 5, 8, 5],
'performance score': [988, 95,100,65]
}
df = pd.DataFrame(data)
corr = df.corr()
print(corr)
sns.heatmap(corr, annot = True)
plt.show()
