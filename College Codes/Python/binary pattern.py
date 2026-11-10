i = 1
while i <= 6:
    binary = ""
    j = 0
    while j < i:
        if j % 2 == 0:
            binary = binary + "1"
        else:
            binary = binary + "0"
        j = j + 1
    print(binary)
    i = i + 1