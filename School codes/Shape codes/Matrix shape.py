for c in range(1, 6):
    for r in range(1, 4):
        if c == 1 and r == 2:
            print('  #')
        if r == 2 and c == 1:
            print('$', end=' ')
        if r == 2 and c == 2:
            print('#', end=' ')
        if r == 2 and c == 3:
            print('$')
        if c == 5 and r == 1:
            print('$', end=' ')
        if c == 5 and r == 2:
            print('#', end=' ')
        if c == 5 and r == 3:
            print('$', end=' ')
        if c == 5 and r == 4:
            print('#', end=' ')
        if c == 5 and r == 5:
            print('$')
