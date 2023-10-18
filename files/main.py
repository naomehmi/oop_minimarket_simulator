from minimarketClasses import *
from time import sleep
from random import randrange
import datetime

"""
fitur yang belum selesai:
1. exp date
2. main level (shift)
3. stats review (stlh quit/resign)
4. formatting tabel (blm rapi)
"""

#try dan except nama si employee
def employeeNameCheck():
    try:
        name = input("=> ")
        if not name.isalpha():
            raise ValueError("=> Numbers, spaces, and symbols are not allowed. Please try again :)\n")
    except ValueError as e:
        print(str(e))
        #mencoba terus sampe gak ValueError
        return employeeNameCheck()
    return name.title()

#main gameplay
def mainGame(tutorial=False):
    #step = langkah ke brp dlm tutorial
    if tutorial:
        step = 1
    while True:
        sleep(0.3)
        print(f"DAY {miniMarket.level}",end=" ")
        if tutorial:
            print("<TUTORIAL>")
            print("="*11,end="")
        else:
            print()
        print("="*5)
        print()
        print("1. Check Minimarket's Stock") #check stock barang sebelum mulai shift
        sleep(0.3)
        print("2. Start shift") #mulai level
        sleep(0.3)
        print("3. Resign") #quit
        print("Pick an option (1/2/3).")
        print()
        sleep(0.3)

        #klo tutorial = true
        if tutorial:
            if step == 1:
                print(f"=> Hello, {player.name}. Welcome to your first shift. I will show you how it works.")
                print("=> There are three choices for you to pick everyday. Let's go over them one by one.")
                print()
                print("=> Try pressing '1' to check the minimarket's stock.")
            elif step == 2:
                print("=> Alright, now that we have already managed our stocks before we open the minimarket, let's start today's shift.")
                print(f"=> Press '2' to start your first shift, {player.name}.")
            while True:
                try:
                    interact = int(input("=> "))
                    if interact == step:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print(f"=> Press '{step}' to continue the tutorial.")
            step += 1

        #klo gk tutorial
        else:
            try:
                interact = int(input("=> "))
                if interact < 1 or interact > 3:
                    raise ValueError
            except ValueError:
                print("=> Press '1', '2', or '3'.")
        print()
        if interact == 1:
            if tutorial:
                stock.showStock(unlocked,True)
                interact = None
            else:
                stock.showStock(unlocked)
        elif interact == 2:
            #proses kasir2an
            pass
        elif interact == 3:
            #nanti aku mau tampilin progress si player
            print("byebye")
            break
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
    while True:
        try:
            interact = input("=> ").lower()
            if interact != 'p' and interact != 'q':
                raise ValueError
            break
        except ValueError:
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
stock.generateProducts(7,0,"consumable",True)
stock.generateProducts(10,1,"consumable")

#intro dan tutorial
if menu == 'p':
    print("=" * 75)
    print()
    print("=> Welcome to Minimarket Simulator, newbie. In this game, you will be playing as a minimarket employee.")
    print("=> Your tasks include: processing customer payments, restocking products, and managing the minimarket's finances.")
    print("=> The game will be over if you get fired or quit your job. Are you ready?")
    print()
    sleep(2)

    #buat object player pakek class employee
    print("=> Before we start, what's your name? (Numbers, spaces, and symbols are not allowed)")
    player = employee("EMPLOYEE"+str(randrange(1000,10000)),employeeNameCheck())
    print()

    #tanya klo mau tutorial atau lgsg skip ke game utama
    print(f"=> Would you like to play our interactive tutorial, {player.name}? (Y/N)")
    while True:
        try:
            interact = input("=> ").lower()
            print()
            if interact == "y":
                mainGame(True)
            elif interact == "n":
                mainGame()
            else:
                raise ValueError
            break
        except ValueError:
            print("=> Press 'y' or 'n'")
