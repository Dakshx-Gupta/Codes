import csv
import pandas as pd
import sys
import time as t
import tkinter as tk 

with open('Library.csv', 'r',encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    lib = pd.DataFrame(reader)

def return_book():
    d = input("Enter the code of the book you have: ")
    r = input("Enter today's date(d-m-y format): ")
    print()
    index = lib.isin([d]).any(axis=1).idxmax()
    lib.iloc[index, 7] = ""
    lib.iloc[index, 8] = ""
    lib.iloc[index, 9] = ""
    lib.iloc[index, 10] = ""
    lib.iloc[index, 6] = 1
    lib.to_csv('Library.csv', header=False,index=False)
    rd = lib.iloc[index, 8]
    if rd == r:
        print("Thank you for returning the book!")
        print("Now what you want to do?")
        print()
        print("1 - Return another book\n2 - Customer Menu\n3 - Exit")
        ch9 = int(input("Enter your choice(1-3): "))
        if ch9 == 1:
            return_book()
        if ch9 == 2:
            customer()
        if ch9 == 3:
            sys.exit()
    else:
        print("You will be charged with late return fees as you are returning the book after the specified return date")
        print("You will be charged of:", lib.iloc[index, 5])
        print()
        print("Thank you for returning the book!")
        print("Now what you want to do?")
        print()
        print("1 - Return another book\n2 - Customer Menu\n3 - Exit")
        ch9 = int(input("Enter your choice(1-3): "))
        if ch9 == 1:
            return_book()
        if ch9 == 2:
            customer()
        if ch9 == 3:
            sys.exit()

def delete():
    global lib
    print("-----Current Library-----")
    print(lib)
    ri = int(input("Enter the index value of the row you want to delete: "))
    lib = lib.drop([ri])
    lib = lib.reset_index(drop=True)
    lib.to_csv('Library.csv', header=False, index=False)
    print()
    print("Changed Successfully! See Below")
    print(lib)
    print()
    print("Now what you want to do?")
    print()
    print("1 - Delete record again\n2 - Back\n3 - Exit")
    ch4 = int(input("Enter your choice(1-3): "))
    if ch4 == 1:
        delete()
    if ch4 == 2:
        admin()
    if ch4 == 3:
        sys.exit()

def change():
    print("-----Current Library-----")
    print(lib)
    r = int(input("Enter the index value of the row you want to change(from 0-): "))
    c = int(input("Enter the index value of the columns you want to change(from 0-): "))
    n = input("Enter the new data: ")
    lib.iloc[r,c] = n
    lib.to_csv('Library.csv', header=False, index=False)
    print()
    print("Changed Successfully! See Below")
    print(lib)
    print()
    print("Now what you want to do?")
    print()
    print("1 - Change record again\n2 - Back\n3 - Exit")
    ch4 = int(input("Enter your choice(1-3): "))
    if ch4 == 1:
        change()
    if ch4 == 2:
        admin()
    if ch4 == 3:
        sys.exit()

def customer():
    global lib
    print("-----Customer Menu-----")
    print()
    print("1 - Available Books\n2 - Return a book\n3 - Make a request for a book\n4 - Main Menu\n5 - Exit")
    ch = int(input("Enter your choice(1-3): "))
    print()
    if ch == 1:
        print("-----Current Books in The Library-----")
        df = pd.read_csv('Library.csv', usecols=['Book code','Book Name', 'Genre', 'Author','Price','Late return fees'])
        print(df)
        c = int(input("Enter the index value of the book you want (from 0-): "))
        print()
        print("Checking the availability of the book... Please Wait")
        t.sleep(0.7)
        a = lib.iloc[c+1,6]
        if a == '0':
            print("Book unavailable... Returning to Customer Menu.")
            t.sleep(0.5)
            print("Beep Beep Bop....")
            print()
            t.sleep(0.7)
            customer()
        else:
            print("Book Available!")
            cc = input("Are you sure you want to select this book (y/n): ")
            print()
            if cc == 'y' or cc == 'Y':
                print("Please Enter the necessary details below")
                nu = input("Enter your name: ")
                cn = input("Enter your mobile number: ")
                dp = input("Enter today's date: ")
                rd = input("Enter the date you will return this book: ")
                print("Thank You!")
                print("What you want to do now?")
                print("1 - Customer Menu\n2 - Exit")
                lib.iloc[c+1,9] = nu
                lib.iloc[c+1,10] = cn
                lib.iloc[c+1,7] = dp
                lib.iloc[c+1,8] = rd
                lib.iloc[c+1,6] = '0'
                lib.to_csv('Library.csv', header=False, index=False)
                ch8 = int(input("Enter your choice: "))
                if ch8 == 1:
                    customer()
                if ch8 == 2:
                    print("Thank you for coming!")
                    sys.exit()

            if cc == 'n' or cc == "N":
                print("Returning to Customer Menu!")
                t.sleep(0.7)
                customer()
    if ch == 2:
        return_book()

    if ch == 3:
        input("Enter the book name you want: ")
        print("Thank You! Your requested book will be available within a week")
        print("What you want to do now?")
        print("1 - Go Back\n2 - Exit")
        chi = int(input("Enter your choice(1-2): "))
        if chi == 1:
            customer()
        if chi == 2:
            sys.exit()
    if ch == 4:
        main()

    if ch == 5:
        print("Thanks for coming!")
        sys.exit()

def admin():
    global lib
    print("-----Admin Menu-----")
    print("1 - Add new books to the library\n2 - See Records\n3 - Remove books from the library\n4 - Exit")
    ch = int(input("Enter your choice(1-4): "))
    if ch == 1:
        l1 = []
        nb = pd.DataFrame(l1)
        print("-----Current Books in library-----")
        print(lib)
        print()
        b = int(input("How many books you want to enter: "))
        for i in range(0, b):
            c = input("Enter Book code: ")
            n = input("Enter Book name: ")
            a = input("Enter Book Genre: ")
            g = input("Enter Book Author: ")
            p = input("Enter Book Price: ")
            rf = input("Enter Late return fees: ")
            s = 1
            nb = l1.append([c,n,a,g,p,rf,s])
            nb = pd.DataFrame(l1)
            lib = pd.concat([lib, nb], ignore_index=True)
            print("Added Successfully! See Below")
            print()
            print(lib.to_string(header=False))
            l1.clear()
        lib.to_csv('Library.csv',header=False, index=False)
        print("1 - Go Back\n2 - Exit")
        ch2 = int(input("Enter your choice(1-2): "))
        if ch2 == 1:
            admin()
        if ch == 2:
            sys.exit()

    if ch == 2:
        print("-----Records-----")
        print(lib.to_string(header=False))
        print()
        print("1 - Change Records\n2 - Go Back\n3 - Exit")
        ch3 = int(input("Enter your choice(1-3): "))
        if ch3 == 1:
            change()
        if ch3 == 2:
            admin()
        if ch3 == 3:
            sys.exit()    

    if ch == 3:
        delete()

    if ch == 4:
        sys.exit()

def main():
    print("Welcome")
    print("1 - Admin\n2 - Customer\n3 - Exit")
    ch = int(input("Enter your choice(1-3): "))
    if ch == 1:
        print()
        admin()
    if ch == 2:
        print()
        customer()
    if ch == 3:
        sys.exit()
main()
