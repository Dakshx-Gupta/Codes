import matplotlib.pyplot as plt

subjects = ['English','Maths', 'Science','Hindi']
avgpercentage = [90, 70, 60, 80]
plt.pie(avgpercentage, labels= subjects)
plt.xlabel('Subjects')
plt.ylabel('Average Percentage')
plt.legend()
plt.title('Average percentage of class 12 students in different subjects')
plt.show()
