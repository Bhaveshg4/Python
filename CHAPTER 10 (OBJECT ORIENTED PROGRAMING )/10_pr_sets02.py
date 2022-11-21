class Calculator : 
    def __init__(self,num) : 
        self.num = num
    def square (self) :
        print(f"the square of the number is {self.num **2} ")
    def cube  (self) : 
        print(f"the cube of the number is {self.num**3} ")
    def squareRoot (self) : 
        print(f"the square root of the number is {self.num**0.5}")
    
a = Calculator(int(input("enter your number here\n")))
b = Calculator(int(input("enter your number here\n")))
c = Calculator(int(input("enter your number here\n")))


a.square()
b.cube()
c.squareRoot()