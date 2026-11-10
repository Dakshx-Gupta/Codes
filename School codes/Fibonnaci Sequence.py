x = int(input("How many times you want to run the sequence: "))
f = 0
f1 = 1
print(0)
print(1)
for i in range(0, x):
    d = f + f1
    f = f1
    f1 = d
    print(d)
