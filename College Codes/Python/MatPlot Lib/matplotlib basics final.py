import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

d = {
    'marks' : [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
    'att' : [40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
}
df = pd.DataFrame(d)

marks = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
att = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85]

corr = df.corr()
sns.heatmap(corr, annot=True)
# print(df.corr())
# sns.pairplot(df)
# plt.bar(marks, att)
# plt.hist(marks, bins = 5)
# plt.scatter(att, marks)
# sns.boxplot(data=[marks, att])
plt.show()
