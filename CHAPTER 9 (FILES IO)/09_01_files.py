# use open function to open a file
 #f = open("sample.txt" , "r")      # there "r" means read the file 
f = open("sample.txt")   # by default the mode is r
#data = f.read()    reads the content  in the file
data = f.read((5))  #reads only 5 content  # f.read() and f.read("any number") cnnnot be used together it will show error
print(data)
f.close()

