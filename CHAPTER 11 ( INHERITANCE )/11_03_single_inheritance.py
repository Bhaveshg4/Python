class Employee : 
    company = "Visa"
    eCode = 120

class Freelancer : 
    company = "Fiverr"
    level = 0
    def upgradelevel(self) : 
        self.level = self.level + 1
class Pragrammer (Employee , Freelancer ) :
    name = "Rohit"

p = Pragrammer()
p.upgradelevel()
print(p.level)