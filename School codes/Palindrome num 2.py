n = int(input('enter number : '))
s = 0
while n != 0: #until the value becomes 0, the loop will keep on running
    r = n % 10 #storing the remainder in variable 'r'
    n = n//10 #storing the quotient in variable 'n'
    s = s*10+r #multiplying 's' with 10 and then adding 'r'
print(s)
