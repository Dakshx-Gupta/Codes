import matplotlib.pyplot as plt
att = [60,70,80,85,90, 10, 60, 70, 40, 100]
marks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.scatter(att, marks)
plt.xlabel("attendance")
plt.ylabel("Marks")
plt.title("attendance vs Marks")
plt.show()
