# Question - Create a arrow shape
for i in range(0, 5):
    for r in range(0, 5):
        for f in range(0, 5):
            if r == 2 and f == 0:
                print("*")
    for r in range(0, 5):
        for f in range(0, 5):
            if r == 3 and f == 1:
                print(" *")
    for r in range(0, 5):
        for f in range(0, 5):
            if r == 4 and f == 2:
                print("  *")
    for r in range(0, 5):
        for f in range(0, 5):
            if r == 3 and f == 3:
                print(" *")
    for r in range(0, 5):
        for f in range(0, 5):
            if r == 2 and f == 4:
                print("*")
    print()
