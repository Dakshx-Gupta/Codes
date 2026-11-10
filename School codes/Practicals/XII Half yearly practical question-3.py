from matplotlib import pyplot as pl
pn = []
ps = []
x = int(input("How many values you will enter in both list: "))
for i in range(0, x):
    s = input("Enter player name: ")
    pn.append(s)
for i in range(0, x):
    d = int(input("Enter player score: "))
    ps.append(d)
pl.plot(pn,ps)
pl.xlabel("Player Name(X axis)")
pl.ylabel("Player Score(Y axis)")
pl.show()
