import csv
import pandas as pd
import matplotlib.pyplot as plt
l1 = []
f = 0
with open('india.csv','r') as file:
    filereader = csv.reader(file)
    for line in filereader:
        f += 1
        l1.append(line)
        if f == 6:
            break

lib = pd.DataFrame(l1)
print(lib)
year = lib[0].tolist()
population = lib[1].tolist()
population.pop(0)
year.pop(0)
year = year[::-1]
population = population[::-1]
plt.plot(year,population,marker = 'o')
plt.xlabel('Years')
plt.ylabel('Total Population')
plt.title('Total population of India from 2016-2020')
plt.show()
