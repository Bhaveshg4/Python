class Employee : 
    company = "Google"

    def __init__(self) :
        print("Employee is created")

    def getSalary (self) : 
        print (f"salary of this employ working in  { self.company} is {self.salary}")

    @staticmethod
    def greet () :
        print("hello , sir , HARRY")

    @staticmethod
    def time () :
        print("the time is 9 AM in the morning")    

harry = Employee()
harry.salary = 100000
harry.getSalary() # employee.getsalary(harry)
harry.greet()   
harry.time()
harry = Employee()
