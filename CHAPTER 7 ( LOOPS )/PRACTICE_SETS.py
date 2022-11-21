# WRITE A MULRIPLICATION TABLE USING FOR LOOP
numb = int(input("enter your number here\n"))

for i in range(1,11) :
     #print(str(numb) + "X" + str(i) + "=" + str(i *numb) )      #or
     print(f"{numb} x {i} = {numb*i}")

# Write a program to great all the person names stored in a list L1 and which starts with S

L1 = [ " harry" , "soham" , "sona " , "lalit" ]
for name in L1 :
    if name.startswith( "s")  : 
        print(("hello")  + name)        # works well





        






                                                    