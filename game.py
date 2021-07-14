import random
print ("Rock, Paper, Scissors, Shoot!")
x = input("Please choose one of the 'rock', 'paper', 'scissors':")
print(x)

if (x == "rock") or (x == "paper") or (x == "scissors"):
    print ("Valid")
else:
    print("You shall not pass!")
    exit()
print("USER CHOSE.",x)

valid_options = ["rock", "paper", "scissors"]
c = (random.choice(valid_options))
print("Computer Chose.", c)

if(x=="rock") and (c=="scissors"):
    print( "Rock Wins! Beat em")
if (x=="paper") and (c=="rock"):
    print("Paper wins!! You Lost ")
if (x=="scissors") and (c=="paper"):
    print("Scicorrs wins!! You got em")

if(c=="rock") and (x=="scissors"):
    print( "Rock Wins! Comp Wins")
if (c=="paper") and (x=="rock"):
    print("Paper wins!! Paper destroys ")
if (c=="sciccors") and (x=="paper"):
    print("Scissorrs wins!! Comp win")
if (x==c):
    print("Overtime!!")
    















