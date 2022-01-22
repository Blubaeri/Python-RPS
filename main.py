import random
from time import sleep
import sys

"""
for i in range(10):
    sys.stdout.write(".")
    sys.stdout.flush() 
    sleep(0.5)
print("")

pScissors = open("scissors.txt", "r")
pRock = open("rock.txt", "r")
pPaper = open("paper.txt", "r")
pVS = open("VS.txt", "r")
print(pScissors.read())
print(pVS.read())
print(pRock.read())
print(pPaper.read())
"""
scorePlayer = 0
scoreCpu = 0

while True:
    actions =  ["rock", "paper", "scissors"]
    cpu = random.choice(actions)

    print("Welcome to this game of Rock Paper Scissors!")
    player = input("Please choose one of the following: Rock, Paper, Scissors: ").lower()
    while player not in actions:
        player = input("Please enter a valid choice: ").lower()  
    if (player == "rock"):
        if (cpu == "rock"):
            print("Draw!")
        elif (cpu == "paper"):
            print("You lose!")
            scoreCpu += 1
        elif (cpu == "scissors"):
            print('You win!')
            scorePlayer += 1
    if (player == "paper"):
        if (cpu == "rock"):
            print("You win!")
            scorePlayer += 1
        elif (cpu == "paper"):
            print("Draw!")
        elif (cpu == "scissors"):
            print('You lose!')
            scoreCpu += 1
    if (player == "Scissors"):
        if (cpu == "rock"):
            print("You lose!")
            scoreCpu += 1
        elif (cpu == "paper"):
            print("You win!")
            scorePlayer += 1
        elif (cpu == "scissors"):
            print('Draw!')

    opt = ["yes", "no"]
    retry = input("Would you like to play again?: ").lower()
    while retry not in opt:
        retry = input("Please enter a valid choice: ").lower()