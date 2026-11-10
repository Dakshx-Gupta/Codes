import random
num = random.randint(1, 100)
print("You have 5 tries!")
print("Good Luck!")
trials = 0

while trials != 5:
    answer = int(input('Guess the number : '))
    if answer != num:
        trials += 1
        if answer >= num:
            print('Too High')
        elif answer <= num:
            print('Too Low')
    if answer == num:
        print("Correct, You Win!")
        break

if trials == 5:
    print("Game Over! You lose, LOSER!")
    print("The number was =", num)
