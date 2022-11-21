class Person :
     
    country = "India" 
    def takeBreak(self) : 
        print("I am breathing")

class Employee (Person)  : 
   
    company = "Adobe"  
    def getSalary(self) : 
        print(f"Salary is {self.salary}") 
        def takeBreak(self) :
            super().takeBreak() 
            print("Iam an Employee so I am breathing")

class Programmer(Employee) : 
    company = "Fiverr"


    def getSalary(self) : 
        print (f"No salary to programmers")
    def takeBreak(self) : 
        super().takeBreak()
        print("I am a Programmer so I am breathing++")
p = Person()
p.takeBreak()
e = Employee()
e.takeBreak()
pr = Programmer()
pr.takeBreak()
e = Employee()
    


