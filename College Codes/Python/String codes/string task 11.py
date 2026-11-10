a = input("Enter a string: ")
print(a[0], a[-1])
print(a[0:4])
print(a[-4:])
print(a[::-1])

for i in range(0, len(a)):
    if i % 2 == 0:
        print("Even: ", a[i])
    else:
        print("Odd: ", a[i])

print(a[1:len(a)-1])

b = a[::-1]
if a == b:
    print("Palindrome")
else:
    print("Not Palindrome")
