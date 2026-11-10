import seaborn as sns
import matplotlib.pyplot as plt
marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
marks_2 = [80, 90, 33, 45, 44, 89, 45, 90, 34, 22]
sns.boxplot(data=[marks_2, marks])
plt.title("Boxplot of Marks")
plt.show()
