for i in range(0, 5):
        for r in range(0, 11):
                for c in range(0, 11):
                    if r == 2 and c == 0:
                            print("*")
                    else:
                            print("", end=" ")
                    if r == 4 and c == 1:
                            print("*")
                    else:
                            print("", end="")
                    if r == 6 and c == 3:
                            print("*")
                    else:
                            print("", end="")
                    if r == 8 and c == 4:
                            print("*")
                    else:
                            print("",end="")
                    if r == 10 and c == 3:
                            print("*")
                    else:
                            print("",end="")
        print('')
