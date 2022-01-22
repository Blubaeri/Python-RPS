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

actions =  ["rock", "paper", "scissors"]
cpu = random.choice(actions)
outcomes = {"rock": "rock", "rock": "paper", "rock": "scissors", 
            "paper": "paper", "paper": "rock", "paper": "scissors",
            "scissors": "rock", "scissors": "paper", "scissors": "scissors"}

print("Welcome to this game of Rock Paper Scissors!")
player = input("Please choose one of the following: Rock, Paper, Scissors: ")
while player not in actions:
    player = input("Please enter a valid choice: ")
player = player.lower()