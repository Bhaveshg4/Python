class Programmer : 
    company = "Microsoft"
    
    def __init__(self,name,product) :
        self.name = name
        self.product = product
    def getInfo (self) : 
        print(f"The name of the programmer is {self.name} and the product is {self.product} ")
Bhavesh = Programmer ("bhavesh", "skype")
Shreyash = Programmer("Shreyash", "WINDOWS OS")    
Bhavesh.getInfo()
Shreyash.getInfo()


