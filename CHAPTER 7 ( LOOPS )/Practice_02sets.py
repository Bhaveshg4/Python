# write a program to check whether a  number is prime or not
A = int(input("enter your number here\n"))
prime = True
for i in range ( 2, A) : 
    if A%i == 0 :
        prime = False
        break                
if prime  : 
    print( " this number is prime")
else : 
    print( " the number is not prime")


#WRITE A PRAGRAM TO FIND A FACTORIAL OF A GIVEN  NUMBER
U = int(input("enter your number :\n"))
factorial = 1 
for i in range ( 1 , U+1) : 
    factorial = factorial*i
print(f"the factorial of { U} is {factorial}")                # works perfectly














   