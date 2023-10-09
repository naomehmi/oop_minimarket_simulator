from minimarketClasses import *
from time import sleep
from random import randrange
import datetime

"""
fitur yang belum selesai:
1. exp date
2. main level (shift)
3. stats review (stlh quit/resign)
"""

def mainGame(tutorial=False):
    interact = None
    if tutorial:
        step = 1
    while interact != "3":
        sleep(0.3)
        print(f"DAY {miniMarket.level} <TUTORIAL>")
        print("="*16)
        print()
        print("1. Check Minimarket's Stock") #check stock barang sebelum mulai shift
        sleep(0.3)
        print("2. Start shift") #mulai level
        sleep(0.3)
        print("3. Resign") #quit
        print("Pick an option (1/2/3).")
        print()
        sleep(0.3)
        if tutorial:
            if step == 1:
                print(f"=> Hello, {player.name}. Welcome to your first shift. I will show you how it works.")
                print("=> There are three choices for you to pick everyday. Let's go over them one by one.")
                print()
                print("=> Try pressing '1' to check the minimarket's stock.")
            elif step == 2:
                print("=> Alright, now that we have already managed our stocks before we open the minimarket, let's start today's shift.")
                print(f"=> Press '2' to start your first shift, {player.name}.")
            while interact != str(step):
                interact = input("=> ")
                if interact != str(step):
                    print(f"=> Press '{str(step)}' to continue the tutorial.")
                    continue
            step += 1
        else:
            interact = input("=> ")
        print()
        if interact == "1":
            if tutorial:
                stock.showStock(unlocked,True)
                interact = None
            else:
                stock.showStock(unlocked)
        elif interact == '2':
            pass
        elif interact == '3':
            pass
        else:
            print("=> Press '1', '2', or '3'.")
        print()


#menu utama
def mainMenu():
    #display utama
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
    #mulai game
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
#tampil menu utama
menu = mainMenu()
#uang awal = 1000, customer utk level 1 = 3 org, masih level 1, dan masih shift 1
miniMarket = minimarket(1000, 3, 1, 1)
#list kosong itu kita anggap rak tarok produk
stock = stock([[],[],[],[],[],[],[],[]],10)
#berapa produk yang telah diunlocked
unlocked = 2
#kondisi produk. Setiap produk ada 1 dalam 9 kemungkinan kondisinya buruk
cond = ["GOOD", "BAD", "GOOD","GOOD","GOOD", "GOOD", "GOOD", "GOOD"]
#ini generate apel dan susu. untuk apel biar gak ribet tutorial nya, aku bikin 9 apel yg good, sm 1 apel yg bad biar nnt tutorial bisa kasih tau cara untuk discard produk. utk generate produk lain aku bikin di fungsi terpisah aja
for i in range(7):
    stock.listofProducts[0].append(consumable("AP-"+str(randrange(1000,10000)),"APPLE",3.00,"PCS","GOOD","1 week"))
stock.listofProducts[0].append(consumable("AP-"+str(randrange(1000,10000)),"APPLE",3.00,"PCS","BAD","1 week"))
for i in range(10):
    stock.listofProducts[1].append(consumable("MK-"+str(randrange(1000,10000)),"MILK",3.00,"PCS",cond[randrange(1,1000)%8],"1 week"))
#intro
print("=" * 75)
print()
if menu == 'p':
    print("=> Welcome to Minimarket Simulator, newbie. In this game, you will be playing as an minimarket employee.")
    print("=> Your tasks include: processing customer payments, restocking products, and managing the minimarket's finances.")
    print("=> The game will be over if you get fired or quit your job. Are you ready?")
    print()
    sleep(3)
    #nama player
    print("=> Before we start, what's your name?")
    player = employee("EMPLOYEE"+str(randrange(1000,10000)),input("=> ").title())
    print()
    interact = None
    #tanya klo mau tutorial atau lgsg skip ke game utama
    print(f"=> Would you like to play our interactive tutorial, {player.name}? (Y/N)")
    while interact != "y" and interact != "n":
        interact = input("=> ").lower()
        print()
        if interact == "y":
            mainGame(True)
        elif interact == "n":
            #blm buat
            break
        else:
            print("=> Press 'y' or 'n'")
