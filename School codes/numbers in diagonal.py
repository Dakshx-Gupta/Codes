a = 1
for i in range (0,11):
    for k in range(0,11):
        if i == k:
            print(a)
        else:
            print(end=" ")
    a = a+1
    print()
