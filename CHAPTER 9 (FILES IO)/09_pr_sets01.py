# open a txt document names poems . txt in python
# write a program to identify the word  twinkle in the poem
h = open("poem.txt")
s = h.read()
if "twinkle " in s :
    print ("twinkle word is present")
else : 
    print("twinkle word is not present")

h.close()   



