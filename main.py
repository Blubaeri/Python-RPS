import secrets
from time import sleep
import sys

"""
for i in range(10):
    sys.stdout.write(".")
    sys.stdout.flush() 
    sleep(0.5)
print("")
"""

# ASCII ART VARIABLES

# Paper
pPP = open("PP.txt", "r")
pPR = open("PR.txt", "r")
pPS = open("PS.txt", "r")

# Rock
pRP = open("RP.txt", "r")
pRR = open("RR.txt", "r")
pRS = open("RS.txt", "r")

# Scissors
pSP = open("SP.txt", "r")
pSR = open("SR.txt", "r")
pSS = open("SS.txt", "r")

class bcolors:
    WIN = '\033[92m' #GREEN
    DRAW = '\033[93m' #YELLOW
    LOSE = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

print("Welcome to this game of Rock Paper Scissors!")

while True:
    scorePlayer = 0
    scoreCpu = 0
    
    try:
        rounds = int(input("How many rounds do you want to play?: "))
    except ValueError or rounds < 1: 
        continue
    
    for x in range(rounds):
        actions =  ["rock", "paper", "scissors"]
        cpu = secrets.choice(actions)
        player = input("Please choose one of the following: Rock, Paper, Scissors: ").lower()
        while player not in actions:
            player = input("Please enter a valid choice: ").lower()
        if (player == "rock"):
            if (cpu == "rock"):
                print(pRR.read())
                print(bcolors.DRAW + "Draw!" + bcolors.RESET)
            elif (cpu == "paper"):
                print(pRP.read())
                print(bcolors.LOSE + "You lose!" + bcolors.RESET)
                scoreCpu += 1
            elif (cpu == "scissors"):
                print(pRS.read())
                print(bcolors.WIN + "You win!" + bcolors.RESET)
                scorePlayer += 1
        if (player == "paper"):
            if (cpu == "rock"):
                print(pPR.read())
                print(bcolors.WIN + "You win!" + bcolors.RESET)
                scorePlayer += 1
            elif (cpu == "paper"):
                print(pPP.read())
                print(bcolors.DRAW + "Draw!" + bcolors.RESET)
            elif (cpu == "scissors"):
                print(pPS.read())
                print(bcolors.LOSE + "You lose!" + bcolors.RESET)
                scoreCpu += 1
        if (player == "Scissors"):
            if (cpu == "rock"):
                print(pSR.read())
                print(bcolors.LOSE + "You lose!" + bcolors.RESET)
                scoreCpu += 1
            elif (cpu == "paper"):
                print(pSP.read())
                print(bcolors.WIN + "You win!" + bcolors.RESET)
                scorePlayer += 1
            elif (cpu == "scissors"):
                print(pSS.read())
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