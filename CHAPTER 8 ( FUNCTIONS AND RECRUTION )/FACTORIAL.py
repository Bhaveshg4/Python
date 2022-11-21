# to find factorial  using range
#n  = 4
#product = 1
#for i in range (n) : 
    #product = product * ( i + 1)
   # print(product)

# to find factorial using functions
def factorial_iter(n) : 
    product = 1 
    for i in range(n) :
        product = product*(i + 1)
    return product

f = factorial_iter(5)
print(f)





