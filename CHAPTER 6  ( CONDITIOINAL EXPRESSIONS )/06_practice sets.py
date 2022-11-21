#write a program to find greatest of four numbers entered by the user


num1 = int(input("enter number 1 :-"))
num2 = int(input("enter number 2 :-"))
num3 = int(input("enter number 3 :-"))
num4 = int(input("enter number 4 :-"))

if ( num1 > num4) :
    f1 = num1
else :
    f1 = num4

if(num2 > num3) : 
    f2 = num2
else : 
    f2 = num3

if(f1>f2) :
    print(str(f1) + " is greratest")
else : 
    print(str(f2) + " is greatest")


#write a program to find out whether a student is pass or fail ,
# if it requires total 40 percent and at least 33 percent in each subject to pass .
# assume 3 subjects
sub1 = int(input("entre your marks here")) 
sub2 = int(input("entre your marks here"))
sub3 = int(input("enter your marks here"))
PERCENTAGE = (sub1 + sub2 + sub3)*100 / 300
print( PERCENTAGE )
if(PERCENTAGE > 40 ) :
    print("pass")
else : 
    print("fail") 
       



 
 














    