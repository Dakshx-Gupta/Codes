n = 5
for i in range(1, n+1):
    if i == 1 or i == n:
        for j in range(1, n+1):
            print(j, end=" ")
    else:
        print("1", end=" ")
        for j in range(n-2):
            print(" ", end=" ")
        print(n, end=" ")
    print()
