x = input()
for i in range(0, len(x)):
    # print(l2[i])
    b = x[i]
    # print(b)
    if b == " ":
            c = b
            # print(b)
            x = x.replace(c, "_")
print(x)
