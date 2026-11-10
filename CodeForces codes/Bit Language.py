#CodeForces problem Bit++ (282A)
n = int(input(""))
x = 0
for i in range(0, n):
    d = input("")
    if d[0] == "+" or d[1] == "+":
        x += 1
    else:
        x -= 1
print(x)
