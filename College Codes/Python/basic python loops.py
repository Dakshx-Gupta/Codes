# for
print("for loop")
l = [1, 2, 3, 4]
for i in range(0, len(l)):
    print(l[i])
print()

#while
print("While loop")
i = 0  
while i < len(l):
    print(i)
    i +=1
print()

print("Jumping staements - Break")
# jumping statements
for i in range(0, len(l)):
    if l[i] == 2:
        break
    else:
        print(l[i])
print()

print("Jumping statement - continue")
for i in range(0, len(l)):
    if l[i] == 3:
        continue
    else:
        print(l[i])

for i in range(0, len(l)):
    pass

