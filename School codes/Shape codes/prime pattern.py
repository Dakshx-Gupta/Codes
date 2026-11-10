primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

index = 0
for row in range(1, 6):
    for col in range(row):
        print(primes[index], end=' ')
        index = index + 1
    print()
