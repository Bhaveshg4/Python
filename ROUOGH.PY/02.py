while (True) : 
   try : 
    a = int(input("enter your number here"))
    c = 1/a
    print(c)
   except Exception as error : 
    print("exception occured")
    print(error) 

print("thanks for using this code!!")
