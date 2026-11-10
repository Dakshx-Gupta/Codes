print('Welcome to Tic Tac Toe Game by DAKSH GUPTA')
print()
print('Below is the structure of the game ')
l1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# Function to display the current state of the game board
def display():
    print()
    x = 1
    for i in range(0, 9):
        if x % 3 == 0:
            print(l1[i], '\n') # Print the element and move to the next line every 3 elements
        else:
            print(l1[i], end=" ") # Print the element with a space separator
        x += 1

def p1():
    c = 1
    while c != 0:
        print()
        x = int(input('Enter position: '))
        if l1[x-1] == 0:
            l1[x-1] = "*"
            c = 0
        else:
            print('Do Again')


def p2():
    c = 1
    while c != 0:
        print()
        x = int(input('Enter position: '))
        if l1[x-1] == 0:
            l1[x-1] = "#"
            c = 0
        else:
            print('Do Again')


for y in range(1, 10):
    display()
    if y % 2 == 0:
        print('Now P2 chance')
        p2()
    else:
        print('Now P1 chance')
        p1()
    if l1[0] == l1[1] == l1[2] == '*' or l1[3] == l1[4] == l1[5] == '*' or l1[6] == l1[7] == l1[8] == '*' or l1[0] == l1[3] == l1[6] == '*' or l1[1] == l1[4] == l1[7] == '*' or l1[2] == l1[5] == l1[8] == '*' or l1[0] == l1[4] == l1[8] == '*' or l1[2] == l1[4] == l1[6] == '*':
        print('Player 1 Wins!')
        break
    if l1[0] == l1[1] == l1[2] == '#' or l1[3] == l1[4] == l1[5] == '#' or l1[6] == l1[7] == l1[8] == '#' or l1[0] == l1[3] == l1[6] == '#' or l1[1] == l1[4] == l1[7] == '#' or l1[2] == l1[5] == l1[8] == '#' or l1[0] == l1[4] == l1[8] == '#' or l1[2] == l1[4] == l1[6] == '#':
        print('Player 2 Wins!')
        break
print()
print("output")
display()
