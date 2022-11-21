class Employee : 
    company = "bharat Gas"
    salary = 5000
    salarybonus = 500
    #totalSalary =  if you hard code this the salary will be fixed but it cant be in real life .
    @property
    def totalSalary ( self) : 
        return self.salary + self.salarybonus

    @totalSalary.setter 
    def totalSalary(self,val) : 
        self.salarybonus = val - self.salary  
e = Employee()
print(e.totalSalary)  
e.totalSalary = 5800
print(e.salary)
print(e.salarybonus) 



 #@property function makes a property - property as well as a function , as shown in the above example

 
