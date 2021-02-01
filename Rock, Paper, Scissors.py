# Rock Paper Scissors

import random

rock = "rock "
paper = "paper "
scissors = "scissors "

list = ("rock", "paper", "scissors")

prompt = input("Enter rock, paper, or scissors: ")
response = print("Computer's response: ")
computer = (random.choice(list))

print(computer)

# Conditions for winning
if (computer == "rock") and (prompt == "rock"):
    print("Tie! Try again!")
elif (computer == "rock") and (prompt == "scissors"):
    print("Rock wins!")
elif (computer == "rock") and (prompt == "paper"):
    print("Paper wins!")
if (computer == "paper") and (prompt == "paper"):
    print("Tie! Try again!")
elif (computer == "paper") and (prompt == "scissors"):
    print("Scissors wins!")
elif (computer == "paper") and (prompt == "rock"):
    print("Paper wins!")
if (computer == "scissors") and (prompt == "scissors"):
    print("Tie! Try again!")
elif (computer == "scissors") and (prompt == "rock"):
    print("Rock wins!")
elif (computer == "scissors") and (prompt == "paper"):
    print("Scissors wins!")
