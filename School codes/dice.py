import random
sum = 0
dr = int(input('how many dices to roll'))

for x in range(0,dr):
    num = random.randint(1,6)
    print("the number on dice " ,x+1," is ",num)
    sum = sum + num
print('the sum of no. is this:', sum)
