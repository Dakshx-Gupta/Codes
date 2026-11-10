for r in range(0, 6):
    for f in range(0, 6):
        if ((r + f == 5 and r>f ) or (r + f == 3 and f>0)):
            print ("*",end=" ")
        else:
            print(" ", end="")
    print()
