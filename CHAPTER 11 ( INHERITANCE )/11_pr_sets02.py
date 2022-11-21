# Create a class pets from a class Animals and further create class Dog from Pets . Add a method
# bark to the class Dog
class Animals : 
    animalType = "Mammal"

class Pets : 
    color = "White"

class Dog : 
    @staticmethod
    def bark() : 
      print ("BOW! BOW!") 

d = Dog()
d.bark()              