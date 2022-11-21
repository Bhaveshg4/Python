apk = set()
apk.add(0)
apk.add(67)
apk.add(567)
apk.add((7,8,9))     # we can add a tuple in sets , VIMP
apk.add(1)
apk.add(3)
apk.add(2)
 #apk.add(7,8,9) # remember we cannot add a list in a set , VIMP , because its not hashable
print(apk)       # creeating and adding elements in a set 

# SETS METHODS (1)
print(len(apk))     # gives  the lengths of the set apk
print(len(apk))    # works perfectly


# SETS METHOD (2)
apk.remove(67)
print(apk)     # we can remove an element in a set by using  this function           #WORKS Well

# SETS METHOD (3)

print(apk.pop())
print(apk)

# sets method (4)
apk.union({ 67, 5,23})
print(apk)













