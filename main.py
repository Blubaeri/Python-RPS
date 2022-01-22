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

actions =  ["Rock", "Paper", "Scissors"]
cpu = random.choice(actions)

print("Welcome to this game of Rock Paper Scissors!")
player = input("Please choose one of the following: 1) Rock, 2) Paper, 3) Scissors: ")
try:
    player = int(player)
    while ((player < 1) or (player > 3)):    
        player = int(input("Please enter a valid choice: "))
except (ValueError):
    while ValueError:
        player = input("Please enter a valid choice: ")
        player = int(player)
