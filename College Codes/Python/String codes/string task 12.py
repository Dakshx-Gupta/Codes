str = "welcome to python"
print(len(str))
print(str.count("o"))
l = str.split()
for i in range(0, len(l)):
    if l[i] == 'python':
        print("Position of word Python: ", i)
