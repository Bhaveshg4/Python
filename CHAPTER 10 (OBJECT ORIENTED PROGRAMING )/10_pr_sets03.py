class Train : 
    def __init__(self,name,fare,seats) : 
        self.name = name 
        self.fare = fare
        self.seats = seats
    def getStatus(self) : 
        print(f"the name of the train is {self.name}")   
        print(f"the number of the seats present in the train is {self.seats}") 
    def fareInfo(self) : 
        print(f"the price of the seat booking  is {self.name}")


intercity = Train("Intetercity Express : 1454",90,300)
intercity.getStatus()
intercity.fareInfo()


