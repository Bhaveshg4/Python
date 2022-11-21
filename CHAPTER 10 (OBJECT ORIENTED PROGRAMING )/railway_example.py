class RailwayForm :
    formType = "RailwayForm"
    def printData(self) : 
        print(f"Name is {self.name}") 
        print (f"Train is {self.train}")

bhaveshApplication = RailwayForm()
bhaveshApplication.name = "Bhavesh"
bhaveshApplication.train = "GaribRath"
bhaveshApplication.printData()

