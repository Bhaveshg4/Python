# write a program to rename  a file to  halwa.txt
import os
oldname = "to_be_deleted.txt"
newname = "halwa.txt"
with open ( oldname) as f : 
    content = f.read()
with open(newname,"w")  as  f : 
    f.write(content)


os.remove(oldname)    



