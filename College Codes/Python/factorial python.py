n = int(input("Enter the number: "))
fact = 1
if n < 0:
    print("Number entered is negative")
else:
    for i in range(1, n+1):
        fact *= i
print("Factorial is: ", fact)
