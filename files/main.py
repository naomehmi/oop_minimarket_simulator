from minimarketClasses import *
from time import sleep
from random import randrange
import datetime

def tutorialLevel():
    sleep(0.3)
    print(f"DAY {miniMarket.minimarketLevel} <TUTORIAL>")
    print("="*5)
    print()
    print("1. Check Minimarket's Stock")
    sleep(0.3)
    print("2. Start shift")
    sleep(0.3)
    print("3. Resign")
    print("Pick an option (1/2/3).")
    print()
    sleep(0.3)
    print(f"=> Hello, {player.employeeName}. Welcome to your first shift. I will show you how it works.")
    print("=> There are three choices for you to pick everyday. Let's go over them one by one.")
    interact = None
    print()
    print("=> Try pressing '1' to check the minimarket's stock.")
    while interact != "1":
        interact = input("=> ")
        if interact != "1":
            print("=> Press '1'")
    print()
    stock.showStock(unlocked,True)

def mainMenu():
    print("="*75)
    sleep(0.03)
    print("|{:^73}|".format(" "))
    print("|{:^73}|".format("MINIMARKET SIMULATOR"))
    sleep(0.03)
    print("|{:^73}|".format("*"*20))
    sleep(0.03)
    print("|{:^73}|".format("created by cool"))
    sleep(0.03)
    print("|{:^73}|".format(" "))
    sleep(0.03)
    print("|{:^18}{:<36}{:^19}|".format(" ","  ________"," "))
    sleep(0.03)
    print("|{:^18}{:<36}{:^19}|".format(" "," /        \_____         __________"," "))
    sleep(0.03)
    print("|{:^18}{:<36}{:^19}|".format(" ","/__________\____|       |          |"," "))
    sleep(0.03)
    print("|{:^18}{:<36}{:^19}|".format(" ","|    |  |  |            |  |  |    |"," "))
    sleep(0.03)
    print("|{:^18}{:<36}{:^19}|".format(" ","|          |            |          |"," "))
    sleep(0.03)
    print("|{:^18}{:<36}{:^19}|".format(" ","|    \__/  |            |  \__/    |"," "))
    sleep(0.03)
    print("|{:^18}{:<36}{:^19}|".format(" ","|__________|            |__________|"," "))
    sleep(0.03)
    print("|{:^18}{:<36}{:^19}|".format(" ","|        __|____        |          |"," "))
    sleep(0.03)
    print("|{:^18}{:<36}{:^19}|".format(" ","|       |______|     ___|_____     |"," "))
    sleep(0.03)
    print("|{:^18}{:<36}{:^19}|".format(" ","|    ______| |__   __||_____||__   |"," "))
    sleep(0.03)
    print("|{:^18}{:<36}{:^19}|".format(" ","|    |          |  \_|_|_|_|_|_/   |"," "))
    sleep(0.03)
    print("|{:^18}{:<36}{:^19}|".format(" ","|___ |__________|___\|_|_|_|_|/    |"," "))
    sleep(0.03)
    print("|{:^18}{:<36}{:^19}|".format(" ","|                             |    |"," "))
    sleep(0.03)
    print("|{:^73}|".format(" "))
    sleep(0.03)
    print("|{:^73}|".format(" "))
    sleep(0.03)
    print("|{:^73}|".format("PRESS 'P' TO PLAY"))
    sleep(0.03)
    print("|{:^73}|".format("PRESS 'Q' TO QUIT"))
    sleep(0.03)
    print("|{:^73}|".format(" "))
    sleep(0.03)
    print("="*75)
    interact = None
    while interact != 'p' and interact != 'q':
        interact = input("=> ").lower()
        if interact != 'p' and interact != 'q':
            print("=> Press 'p' or 'q'")
    if interact == 'p':
        print()
        print("{:^74}".format("Loading..."))
        print("{:^22}".format(" "),end="")
        for i in range(30):
            print("∎",end="")
            sleep(0.02)
        print()
        print()
    return interact
menu = mainMenu()
miniMarket = minimarket(1000, 3, 1, 1)
stock = stock([[],[],[],[],[],[],[],[]],10)
unlocked = 2
cond = ["GOOD", "BAD", "GOOD","GOOD","GOOD", "GOOD", "GOOD", "GOOD"]
for i in range(7):
    stock.listofProducts[0].append(consumable("AP-"+str(randrange(1000,10000)),"APPLE",3.00,"PCS","GOOD","1 week"))
stock.listofProducts[0].append(consumable("AP-"+str(randrange(1000,10000)),"APPLE",3.00,"PCS","BAD","1 week"))
for i in range(10):
    stock.listofProducts[1].append(nonConsumable("MK-"+str(randrange(1000,10000)),"MILK",3.00,"PCS",cond[randrange(1,1000)%8]))
print("=" * 75)
print()
if menu == 'p':
    print("=> Welcome to Minimarket Simulator, newbie. In this game, you will be playing as an minimarket employee.")
    print("=> Your tasks include: processing customer payments, restocking products, and managing the minimarket's finances.")
    print("=> The game will be over if you get fired or quit your job. Are you ready?")
    print()
    sleep(5)
    print("=> Before we start, what's your name?")
    player = employee("EMPLOYEE"+str(randrange(1000,10000)),input("=> ").title())
    print()
    interact = None
    print(f"=> Would you like to play our interactive tutorial, {player.employeeName}? (Y/N)")
    while interact != "y" and interact != "n":
        interact = input("=> ").lower()
        print()
        if interact == "y":
            tutorialLevel()
        elif interact == "n":
            break
        else:
            print("=> Press 'y' or 'n'")
