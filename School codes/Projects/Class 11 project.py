"""
Created on Wed Feb  7 23:26:10 2024

@author: tempe

Question:
"""
import sys
import pandas as pd
print("Hey! What do you want to do today? Select below!")
print()
l1 = []
l2 = []
df = pd.DataFrame(l1)
dfe = pd.DataFrame(l2)

def teach_data():
    global l2
    global dfe
    l2 = []
    t = int(input("Number of Teacher's data to add: "))
    for i in range(0, t):
        n = input("Enter Teacher's name: ")
        emp = input("Enter Employee ID: ")
        sub = input("Enter Teacher's subject: ")
        c = input("Enter Teacher's contact number: ")
        doa = input("Enter Teacher's DOA yyyy/mm/dd: ")
        cat = input("Enter Teacher's category: ")
        l2.append({"Name": n, "Emp ID": emp, "Subject": sub, "Contact Number": c, "DOA": doa, "Category": cat})
        dfe = pd.DataFrame(l2)
        print("Data entered successfully!")
        print()
    ch = int(input("Do you want to generate report or go back? (1: Report\ 2:Back: ")) 
    if ch == 1:
        print(dfe)
    if ch == 2:
        teacher()
            
def stu_data():
    global l1
    global df
    l1 = []
    t = int(input("Number of student's data to add: "))
    for i in range(0, t):
        n = input("Enter Student's name: ")
        p1 = input("Enter Student's Father name: ")
        p2 = input("Enter Student's Mother name: ")
        c = input("Enter Student's contact number: ")
        d = input("Enter Student's DOB yyyy/mm/dd: ")
        cl = input("Enter Student's class: ")
        doa = input("Enter Student's DOA yyyy/mm/dd: ")
        adhr = input("Enter Student's Aadhar number: ")
        l1.append({"Name": n, "Father's Name": p1, "Mother's Name": p2, "Contact Number": c, "DOB": d, "Class": cl, "DOA": doa, "Aadhar Number": adhr})
        df = pd.DataFrame(l1)
        print("Data entered successfully!")
        print()
    ch = int(input("Do you want to generate report or go back? (1: Report\ 2:Back: ")) 
    if ch == 1:
        print(df)   
    if ch == 2:
        student()
       
def teacher():
    print("~~Teacher's Database~~")
    print("1: Add new data")
    print("2: Edit existing data")
    print("3: Report")
    print("4: Delete data")
    print("5: Back")
    print("6: Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        teach_data()
    if ch == 2:
        teach_edit()
    if ch == 3:
        print(dfe)
    if ch == 4:
        teach_del()
    if ch == 5:
        main_menu()
    if ch == 6:
        print("Exit successful!")
        sys.exit()
        
def teach_edit():
    global dfe
    print(dfe)
    a = input("data you want to change: ")
    v = input("new data: ")
    dfe = dfe.replace(a, v)
    ch = int(input("Do you want to generate report or go back? (1: Report\ 2:Back: ")) 
    if ch == 1:
        print(dfe)
    if ch == 2:
        teacher()

def teach_del():
    global dfe
    print(dfe)
    s = input("Enter the value in 'Name' column of the row you want to delete: ")
    a = dfe.index[dfe["Name"] == s].tolist()
    dfe = dfe.drop(a)
    ch = int(input("Do you want to generate report or go back? (1: Report\ 2:Back: ")) 
    if ch == 1:
        print(dfe)
    if ch == 2:
        teacher()
       
def stu_del():
    global df
    print(df)
    s = input("Enter the value in 'Name' column of the row you want to delete: ")
    a = df.index[df["Name"] == s].tolist()
    df = df.drop(a)
    ch = int(input("Do you want to generate report or go back? (1: Report\ 2:Back: ")) 
    if ch == 1:
        print(df)
    if ch == 2:
        student()
    
def stu_edit():
    global df
    print(df)
    a = input("data you want to change: ")
    v = input("new data: ")
    df = df.replace(a, v)
    ch = int(input("Do you want to generate report or go back? (1: Report\ 2:Back: ")) 
    if ch == 1:
        print(df)
    if ch == 2:
        student()
   
def student():
    print("~~Student's Database~~")
    print("1: Add new data")
    print("2: Edit existing data")
    print("3: Delete data")
    print("4: Report")
    print("5: Back")
    print("6: Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        stu_data()
    if ch == 2:
        stu_edit()
    if ch == 3:
        stu_del()
    if ch == 4:
        print(df)
    if ch == 5:
        main_menu()
    if ch == 6:
        print("Exit successful!")
        sys.exit()
       
def main_menu():
    print("~~Main Menu~~")
    print("1: Student's Database")
    print("2: Teacher's Database")
    print("3: Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        student()
    if ch == 2:
        teacher()
    if ch == 3:
        print("Exit successful!")
        sys.exit()
main_menu()

