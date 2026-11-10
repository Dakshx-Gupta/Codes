import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data = {
'Math': [80, 85, 90, 95, 100],
'Physics': [75, 80, 85, 90, 95],
'Chemistry': [70, 75, 80, 85, 90]
}
df = pd.DataFrame(data)
sns.pairplot(df)
plt.show()
