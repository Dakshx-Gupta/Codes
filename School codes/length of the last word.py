l1 = []
x = input("Enter the str: ")
l1 = x.split()
for i in l1:
    if i.isalnum():
        print(len(l1[-1]))
#print(l1)
#print(len(l1[-1]))
