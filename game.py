import random

import os
from dotenv import load_dotenv 

load_dotenv() #loading content of the file .env file

user_name = os.getenv("USER_NAME")

print(user_name) #reads the variable

# use of random variable for computer
# establishing the inputs
print ("Rock, Paper, Scissors, Shoot!")
x = input("Please choose one of the 'rock', 'paper', 'scissors':")
print(x)
# choices for the variable x

if (x == "rock") or (x == "paper") or (x == "scissors"):
    print("Valid")
else:
    print("You shall not pass!")
    exit()
print("USER CHOSE.",x)
#setting the options for computer
valid_options = ["rock", "paper", "scissors"]
c = (random.choice(valid_options))
print("Computer Chose.", c)

# Logic for the game
# My choices
if(x=="rock") and (c=="scissors"):
    print( "Rock Wins! You Beat em")
if (x=="paper") and (c=="rock"):
    print("Paper Wins!! You Lost ")
if (x=="scissors") and (c=="paper"):
    print("Scissors Wins!! You got em")

# Choices for computer
if(c=="rock") and (x=="scissors"):
    print( "Rock Wins! Comp Wins")
if (c=="paper") and (x=="rock"):
    print("Paper Wins!! Computer destroys ")
if (c=="scissors") and (x=="paper"):
    print("Scissors Wins!! Computer win")
if (x==c):
    print("Overtime!!")

print("Thank you for plahying.Run it back?")

























