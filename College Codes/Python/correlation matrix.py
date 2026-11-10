import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {
'marks': [80, 85, 90, 95],
'attendance': [75, 80, 85, 90],
'studyh': [7, 5, 8, 5],
'sleep': [7, 8, 9, 10]
}
df = pd.DataFrame(data)
corr = df.corr()
sns.heatmap(corr, annot=True)
plt.show()
