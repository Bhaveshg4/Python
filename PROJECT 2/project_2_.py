import random
randNumber = random.randint(1,5)
print(randNumber)

userGuess = int(input("enter your guess here"))
if (userGuess == randNumber) : 
    print ( "Your guess was right")
else : 
    print("you guessed it wrong")
    









