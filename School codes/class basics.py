class employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gg.com"
        
    def fullname(self):
        return self.first + " " + self.last
         
emp1 = employee("daksh", "gupta", 500)

print(emp1.fullname())
