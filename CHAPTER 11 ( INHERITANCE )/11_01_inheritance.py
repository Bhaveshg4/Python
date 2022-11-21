class Employee : 
    company = "Adobe"
    def ShowDeetails ( self) :
        print("This is an employee")

class Programmer (Employee) :    # THIS IS CALLED INHERITANCE
    language = "Python"
    def getLanguage (self) :
        print(f"the language is {self.language}")
    def ShowDeetails ( self) :
        print("This is an employee")
e = Employee()
e.ShowDeetails()
p = Programmer()
p.getLanguage()
p.ShowDeetails()   # this also shows that it is an employee
print(p.company)

 



















 
