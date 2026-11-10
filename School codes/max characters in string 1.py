# Question - Find the alphabet appearing maximum number of times
l1 = []
l2 = []
a = input().lower()
a = a.replace(" ","")
v = list(a)
print(v)
for i in v:
    a = v.count(i)
    l1.append(a)
s = max(l1)
for i in v:
    a = v.count(i)
    if s == a:
        l2.append(i)
l2 = set(l2)
print("Character appearing maximum number of times: ", l2)
