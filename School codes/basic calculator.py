n1,op,n2 = input("enter eq. for cal = ").split()
n1 = int(n1)
n2 = int(n2)
if op == '+':
    print("{} + {} = {}".format(n1,n2,n1+n2))
if op == '-':
    print('{} - {} = {}'.format(n1,n2,n1-n2))
if op == 'x' or op == 'X':
    print('{} * {} = {}'.format(n1,n2,n1*n2))
if op == '/':
    print('{} / {} = {}'.format(n1,n2,n1/n2))
if op == '//':
    print('{} // {} = {}'.format(n1,n2,n1//n2))
if op == '%':
    print('{} % {} = {}'.format(n1,n2,n1%n2))

