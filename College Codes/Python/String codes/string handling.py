a = ' daksh '
b = "da3ksh"
d = "d a k s h"
print(a.strip())
print(a.title())
for i in range(0, len(b)):
    if b[i].isdigit():
        c = b[i]
        # print(c)
        b = b.replace(c, " ")
print(b)
print(c)
print("daksh".zfill(5))
