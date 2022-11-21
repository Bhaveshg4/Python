class Employee : 
    company = "Google"
    salary = 200

harry = Employee()
rajni = Employee()

# creating insance attribute salary for both the objects
#harry.salary = 300 # this is called an attribte
#rajni.salary = 400 # if we do not write this line , it  will show the salary present in the class 
#and if the salary is not present in the class itself , it will throw an error
harry.salary = 500
print(harry.salary) # we make an attribute  so it shows 500
print(rajni.salary) # we do not make a sttribute so it shows 200 (which is present in  class )


