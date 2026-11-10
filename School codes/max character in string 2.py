# Question - Find the alphabet appearing maximum number of times METHOD-2
a = input().replace(' ','')
l1 = []
for i in a:
    v = a.count(i)
    l1.append(v)
s = max(l1)
o = l1.index(s)
c = a[o]
print("Value occurring max number of times:", c)
