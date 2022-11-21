a = "34345"
#print (type(a))
#its an string and not a  integer 
# now a =+ 3 not possible because  a itself is an string .


# if still a is in a string and we have to add a numerical value  then we use TYPECASTING 
#to convert write
a = int(a) # for string to integer

#note - TYPECASTING ONLY STIES TO CONVERT STRING TO FUNCTION OR FUNCTION TO STRING 
# IT DO NOT TAKE ANY GAURANTEE
#usually it fails to convert  string to integer ex  -harry
print(a +5 )
#if the info inside a string is  integer then it succeed to do so

# ERROR EXAMPLE 
b = "64anish "
b = int(b)
print(b+4)    # its an error as it fails to do so because its a sring
