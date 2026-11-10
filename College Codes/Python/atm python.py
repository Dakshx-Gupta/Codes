balance = 20000
while True : 
    print("\n----ATM MENU----")
    print("1. DEPOSIT")
    print("2. WITHDRAW")
    print("3. CHECK BALANCE")
    print("4. EXIT")
    
    choice = int(input("ENTER YOURT CHOICE: "))
    if choice == 1:
        amt = int(input("ENTER AMOUNT TO DEPOSIT: "))
        if amt > 0:
            balance += amt
            print("DEPOSIT SUCCESSFUL!")
            print("UPDATED BALANCE: ", balance)
        else:
            print("ENTER VALID AMOUNT!")
    elif choice == 2:
        amt = int(input("ENTER AMOUNT TO WITHDRAW: "))
        if amt > balance:
            print("NOT ENOUGH MONEY!")
        else:        
            balance -= amt
            print("WITHDRAWL SUCCESSFUL!")
            print("UPDATED BALANCE: ", balance)
    elif choice == 3:
        print("CURRENT BALANCE IS: ", balance)
    elif choice == 4:
        print("THANKYOU FOR USING ATM!")
        break;
    else:
        print("ENTER VALID OPTION!")