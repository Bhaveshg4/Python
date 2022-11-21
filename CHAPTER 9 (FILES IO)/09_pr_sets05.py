f1 = "file1.txt"
f2 = "file2.txt" 

with open (f1) as f : 
    f1 =  f.read()

with open (f2)  as f :
    f2 = f.read()


if f1 == f2: 
    print("both the files are identical") 
else :
    print("not identical")        

