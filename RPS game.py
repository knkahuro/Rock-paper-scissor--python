#k3nny
#29/03/24

import time
import random

bot = ["R", "P", "S"]
win = 0
name = input("Enter your name player👾:\n")
print("wait...\n")
time.sleep(2)
print("Welcome " + name + "👾")
time.sleep(3)
print("Let's play Rock _Paper_ Scissors, \n")
time.sleep(4)
print("Here are the rules: type R for rock, type P for paper and type S for scissors \n")
time.sleep(5)
print("\[READY...GO AHEAD🕹️\]")

while True:
    a = input("\nR, P, S (or 'q' to quit): \n").upper()
    if a == 'Q':
        break
    if a not in ["R", "P", "S"]:
        print("Invalid input. Please try again.")
        continue
    x = random.choice(bot)
    print("Your choice:", a, "Computer's choice:", x)
    
    if a == x:
        print("It's a tie!")
    elif (a == "R" and x == "S") or (a == "P" and x == "R") or (a == "S" and x == "P"):
        print("You win!🍬")
        win += 1
    else:
        print("Computer wins!🤖")
    
    print("Your score:", win)
    
print("Thanks for playing! \nHere is some chocolate🍫")
