import matplotlib.pyplot as plt

subjects = ['English','Maths', 'Science','Hindi']
avgpercentage = [90, 70, 60, 80]
avgpercentage2 = [80, 60, 90, 50]
plt.plot(subjects, avgpercentage, color = 'Green', label = 'Class 12')
plt.plot(subjects, avgpercentage2, color = 'Red', label = 'Class 11')
plt.xlabel('Subjects')
plt.ylabel('Average Percentage')
plt.legend(['Class 12'])
plt.title('Average percentage of class 12 and 11')
plt.show()
