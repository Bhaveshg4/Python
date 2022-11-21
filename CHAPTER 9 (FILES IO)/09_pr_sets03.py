# a file contain a word "donkey" multiple times , you need to sensor the word
# Make a program to do so

with open ("donkey_sensors.txt") as f :
    content = f.read()
content = content.replace("donkey", "#%@^&$")

with open("donkey_sensors.txt", "w") as f :
     f.write(content)
     # works perfectly

     
