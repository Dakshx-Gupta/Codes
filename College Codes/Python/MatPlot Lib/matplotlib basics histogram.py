import matplotlib.pyplot as plt
import random
l1 = random.sample(range(1, 101), 20)
plt.hist(l1, bins=5)
plt.title("Marks Distribution")
plt.show()
