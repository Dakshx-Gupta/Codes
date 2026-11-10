l1 = []
l2 = []
l3 = []
bd = ""
ad = ""
ans = ""
x = input("Num: ")
l2 = list(x)
o = l2.index(".")

#separating values before decimal
for i in range(0, len(l2)):
    if l2[i] == ".":
        break
    else:
        bd += l2[i]

#separating values after decimal
for i in range(o, len(l2)):
    ad += l2[i]

bd = int(bd)
ad = float(ad)
j = str(ad)
#print(ad)
#print(j)
lo = j.index('.')
#print(lo)
#print(j[lo+1])

while bd != 0:
    a = bd % 2
    l1.append(a)
    bd = bd//2  
  
while j[lo+1] != '0':
    op = ad*2
    a = str(op)
    #print(a)
    l3.append(a[0])
    #print(l3)
    ad = ad*2
    ad = str(ad)
    ad = ad.removeprefix((ad[0]))
    ad = float(ad)
    j = float(j)
    j = j*2
    j = str(j)
    j = j.removeprefix((j[0]))
    j = float(j)
    j = str(j)
    #print(j)
l1.reverse()
print("Before decimal point value into binary: ", l1)
print("After Decimal point value into binary: ", l3)
