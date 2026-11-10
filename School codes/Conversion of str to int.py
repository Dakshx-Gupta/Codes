s1 = input('Enter 1st value : ')
s2 = input('Enter 2nd value : ')
s3 = int(input('Enter the 1st value again :  '))
s4 = int(input('Enter the 2nd value again : '))
user_choice = int(input('1 for answer in string or 2 for answer in int value: '))
if user_choice == 1:
    print(s1+s2)
elif user_choice == 2:
    print(s3+s4, s3*s4, s3/s4, s3-s4)

