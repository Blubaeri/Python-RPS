import random
from time import sleep
import sys

"""
for i in range(10):
    sys.stdout.write(".")
    sys.stdout.flush() 
    sleep(0.5)
print("")
"""
pScissors = open("scissors.txt", "r")
pRock = open("rock.txt", "r")
pPaper = open("paper.txt", "r")
pVS = open("VS.txt", "r")
"""
print(pScissors.read())
print(pVS.read())
print(pRock.read())
print(pPaper.read())
"""

class bcolors:
    WIN = '\033[92m' #GREEN
    DRAW = '\033[93m' #YELLOW
    LOSE = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR


scorePlayer = 0
scoreCpu = 0

while True:
    print("Welcome to this game of Rock Paper Scissors!")

    rounds = input("How many rounds do you want to play?: ")
    try:
        rounds = int(rounds)
    except ValueError or rounds < 1: 
        rounds = input("Please enter a valid value: ")
    
    for x in range(rounds):
        actions =  ["rock", "paper", "scissors"]
        cpu = random.choice(actions)
        player = input("Please choose one of the following: Rock, Paper, Scissors: ").lower()
        while player not in actions:
            player = input("Please enter a valid choice: ").lower()
        if (player == "rock"):
            if (cpu == "rock"):
                print(bcolors.DRAW + "Draw!" + bcolors.RESET)
            elif (cpu == "paper"):
                print(bcolors.LOSE + "You lose!" + bcolors.RESET)
                scoreCpu += 1
            elif (cpu == "scissors"):
                print(bcolors.WIN + "You win!" + bcolors.RESET)
                scorePlayer += 1
        if (player == "paper"):
            if (cpu == "rock"):
                print(bcolors.WIN + "You win!" + bcolors.RESET)
                scorePlayer += 1
            elif (cpu == "paper"):
                print(bcolors.DRAW + "Draw!" + bcolors.RESET)
            elif (cpu == "scissors"):
                print(bcolors.LOSE + "You lose!" + bcolors.RESET)
                scoreCpu += 1
        if (player == "Scissors"):
            if (cpu == "rock"):
                print(bcolors.LOSE + "You lose!" + bcolors.RESET)
                scoreCpu += 1
            elif (cpu == "paper"):
                print(bcolors.WIN + "You win!" + bcolors.RESET)
                scorePlayer += 1
            elif (cpu == "scissors"):
                print(bcolors.DRAW + "Draw!" + bcolors.RESET)
        print("You:", scorePlayer, "v.s CPU:", scoreCpu)

    print("You played", x , "rounds and won", scorePlayer, "of them and lost", scoreCpu, "of them.")
    opt = ["yes", "no"]
    retry = input("Would you like to play again?: ").lower()
    while retry not in opt:
        retry = input("Please enter a valid choice: ").lower()
    if retry == "no":
        print("Thanks for playing!")
        break