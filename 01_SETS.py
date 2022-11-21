a = { 2,6,7,4,5}
a_update = { 8,9 }
a.update(a_update)
print(a)                             # we can update a set , WORKS PERFECTLY

b = {2,5,7,1,9}
print(b)
print(type(b))               # works well

# VIMP  ( WE CANNOT REPET A VARIABLE IN A SET)
#ex - 
z = {5,7,8 , 6 , 8}      # it will not print 8 two times
print(z)


# EMPTY SETS AND ITS  NOTATION
# remember -
j = {}    # its not an empty set its a  empty dctionary
print(type(j))           # IT WILL GIVE DICTIONARY

# CORRECT NOTATION --
k = set()                          # NOW ITS CORRECT
print(type(k))


# HOW TO ADD ELEMENTS IN A SET  
GH = set()
GH.add(3)
GH.add(67)
GH.add(56)
print(GH)         # WORKS PERFECTLY FINE












