#  PRACTICE SETS [CHAPTER STRINGS]
# MAKE A PROGRAM  THAT WISHES A PROGRAMER GOOD MORNING
#name =  input  ("enter your name here")
#print("good morning",name)

# make a letter format foa a candidate who is selected

letter =  ''' Dear  <|NAME|>,
             you are selected ! congratulagions
             Date : <|DATE|>'''
name = input("entre your name here")
date = input("entre today's date")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>" , date)

print(letter)  
# REMEMBRE - if you have to replace something from  letter  write it as letter = letter.replace(___)


# make a  program to find the number of double spaces in a sring


STRING = " Shreyash is a    good boy . He is very good coder"
DS = STRING.find("    ")
print(DS)
              





   



    
