password = 'qwerTy'
newstring = ''
for letter in password:
    if letter.islower() == True:
        newstring+= letter
print(newstring)
