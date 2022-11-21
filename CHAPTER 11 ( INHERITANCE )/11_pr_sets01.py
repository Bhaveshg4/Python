# Create a class 2d vector and use it to create another class representing a 3d vector
class  c2dvec :
     def __init__(Self , i , j) :
         self.icap = i 
         self.jcap = j 
def __str__(self) : 
    return f"{self.icap}i + {self.jcap}j"


class c3dvec(c2dvec) :
    def __init__(self,i,j,k) : 
        super().__init__(i,j)
        self.icap = i
        self.jcap = j 
        self.kcap = k 

    def __str__(self) : 
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"    

v3d = c3dvec(1, 9 , 7 ) 
print(v2d)
print(v3d)






