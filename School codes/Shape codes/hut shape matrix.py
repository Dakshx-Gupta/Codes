import time as t
for c in range(1, 4):
    for r in range(1, 6):
        if r + c == 4 or (c == 2 and r + c == 6) or r + c>7:
            print("*",end=" ")
            t.sleep(0.3)
        else:
            print(" ",end="")
    print()
for c in range(1, 5):
    for r in range(1, 5):
        if r == 4 or r==1 or c==1 or c==4:
            print("*", end=" ")
            t.sleep(0.3)
        else:
            print("  ", end="")
    print()
