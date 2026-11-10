
"""
Created on Thu Feb 15 09:05:10 2024

@author: tempe

Question:
"""
import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="manan9414",
    database="school"
)

mycursor = con.cursor()
#mycursor.execute("create table school(Name varchar(20), DOB varchar(20), Contact varchar(10), DOA varchar(20))")
# for i in mycursor:
#     print(i)
# sql = "insert into school(Name, DOB, Contact, DOA) values(%s, %s, %s, %s)"
# val = [("Nandika", "15/09/2007", "9310923563","22/09/2024"),
#        ("Rigav", "12/02/2007", "9414094453", "22/02/2022"),
#        ("Gaurav", "15/01/2007", "9514344832","25/05/2018")
#       ]
# mycursor.executemany(sql, val)
# s = "delete from school where Name like 'Daksh'"
# mycursor.execute(s)
con.commit()
mycursor.execute("select*from school")
for i in mycursor:
    print(i)

