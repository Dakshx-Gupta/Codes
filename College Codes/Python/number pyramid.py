n = 5
num = 1

for i in range(1, n + 1):
    for s in range(n - i):
        print(" ", end=" ")
    for j in range(i):
        if num % 3 == 0 and num % 5 == 0:
            print("@", end=" ")
        elif num % 3 == 0:
            print("*", end=" ")
        elif num % 5 == 0:
            print("#", end=" ")
        else:
            print(num, end=" ")
        num += 1
    print()
