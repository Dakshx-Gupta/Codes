n = input('Enter:')
length = len(n)
flag = 0
for x in range(0, length//2):
    if n[x] == n[length-1-x]:
        continue
    else:
        print('no')
        flag = 1
        break

if flag == 0:
    print("yes")
