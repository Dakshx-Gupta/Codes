e = int(input('enter no. of elements: '))
l1 = []
f = 0
for e in range(0,e):
    x = int(input('enter value: '))
    l1.append(x)
print(l1)
for i in l1:
    if i == 1:
        f+=1
    while i!=0:
        r = i%10
        if r == 1:
            f+=1
        i = i//10
print(f) 
