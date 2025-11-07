import random as rand

Rockpaperscissors = "rock","paper","Scissors"

AiChoice = rand.choice(Rockpaperscissors)

userChoice = input("Select a rock, paper or scissors: ")

if userChoice == "rock" and AiChoice == "scissors":
    print(f"You won! The ai chose {AiChoice}")
elif userChoice == "paper" and AiChoice == "rock":
    print(f"You won! The ai chose {AiChoice}")
elif userChoice == "scissors" and AiChoice == "paper":
    print(f"You won! The ai chose {AiChoice}")
elif userChoice == "paper" and AiChoice == "paper":
    print("Draw!")
elif userChoice == "rock" and AiChoice == "rock":
    print("Draw!")
elif userChoice == "scissors" and AiChoice == "scissors":
    print("Draw!")
else:
    print(f"You lost! The ai chose {AiChoice}")