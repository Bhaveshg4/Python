# write the function to dentify the gtretest of the three terms
def maximum(num1 , num2 , num3) :
    if (num1 > num2) : 
        if(num1 > num3) : 
            return num1
        else : 
               return num3
    else : 
             if ( num2 > num3) : 
                return num2
             else :
                    return num3

m = maximum(2, 5, 7)
print("the value of the maximum digit is" , m)