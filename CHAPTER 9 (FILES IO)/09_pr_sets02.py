#The game() function in a program lets a user play a game and return the score as an integer
# you need to read a file "hiscore.txt" which is either blank or contains the previous Hi score . 
#you need to write a pragram to update the hi score when a player breakes the high score
def  game () :
    return 4

score = game()
with open ("hiscore.txt") as f :
    hiscore = int(f.read()) 
    

if hiscore < score :
    with open ("hiscore.txt","w") as f :
        f.write(str(score))                              #WORKS PERFECTLY

