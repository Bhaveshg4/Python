mydict = { 
    "fast" : "anything that moves quickly",
    "Marks" : [23,65,87] ,
    "hello" : "greeting gesture",
    "marks " : [21,54,76,98],
    1 : 32
    }

# DICTIONARY METHODS ( 1 )

# mydict.keys()       # it  gives a list of all the keys  in the program
print(mydict.keys())      # WORKS WELL
print(type(mydict.keys()) )  # this type of statement is called 'dict_keys'
print(list(mydict.keys()) )   # to convert it into a list , [matter]


#DICTIONARY METHODS  ( 2 )
 #list(mydict.values(()))           # GIVES A LIST OF ALL THE VALUES in the program
print(mydict.values())

# DICTIONARY METHODS  ( 3 )
#(mydict.items())     GIVES  KEY VALUE PAIR IN A TUPLE FORM
print(mydict.items())


# DICTIONARY METHODS  ( 4 )
(mydict.items())  #prints the (keys, values) , for all the items of the dictionary

# DICTIONARY METHODS  ( 5 )
#(mydict.update())     # updates the  new items in the  list and keys option


updateDict =  { "friend" : "om",
                "mother" : "sunita",
                "fast" : "quitely"}     # update the dictionary by adding key values  pair from updateDict
mydict.update(updateDict)
print(mydict)                        # works well 
                                   # remember it also update the old key if its name is used , ex - fast

#
print(mydict.get("fast"))          # it  gives the value of fast
# same work can be done with print(mydict["fast"])
# but if we write "harry2" insted of "harry"  , mydict.get do not throw an error but mydict["fast"] throws it
# VIMP 
 
 # DIFFERENCE BETWEEN .GET AND [] SYNTEX IN DICTIONARY
print(mydict.get("fast2"))    # returns none    # works well
 #print(mydict["fast2"])  # throws an error as harry2 is not present in the dictionary



















































 






