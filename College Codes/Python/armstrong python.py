a = int(input("Enter number: "))
sum = 0
c = str(a)
b = a
digit = 0

while(b != 0):
    digit = b % 10
    # print(digit)
    sum = sum + digit ** len(c)
    b = b // 10
# print(sum)
if sum == a:
    print("Armstrong")
else:
    print("Not")
