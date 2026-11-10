l1 = []
l2 = []
l3 = []
eve = 0
odd = 0
x = int(input("How many values you will enter: "))
for i in range(0, x):
    s = int(input("Enter values: "))
    l1.append(s)
for i in range(0, len(l1)):
    if l1[i]%2==0:
        l2.append(l1[i])
        eve+= 1
    else:
        odd+=1
        l3.append(l1[i])
if eve == 1:
    print("Odd value is")
    print(l2[0])
if odd == 1:
    print("Odd value is")
    print(l3[0])
if eve and odd > 1:
    print("No odd value")
