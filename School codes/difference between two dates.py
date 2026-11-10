from datetime import date

x = input("enter u DOB yyyy/mm/dd: ").split('/')
y = int(x[0])
m = int(x[1])
d = int(x[2])

d1 = date(y, m, d)
d2 = date.today()
diff = d2-d1
print("Num of days you have lived:", diff.days)
