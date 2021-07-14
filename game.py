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

valid_options = ["rock", "paper", "sciccors"]
c = (random.choice(valid_options))
print("Computer Chose.", c)













