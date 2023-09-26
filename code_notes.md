# PENJELASAN CODE yg agak rumit

## di file class

itu def showStock (dari class stock) itu utk format tabel, tampilin semua jenis.
```
def showStock(self,unlocked,name,tutorial=False):
        print("-"*71)
        print("|{:^3}|{:^15}|{:^15}|{:^12}|{:^20}|".format("No.","Product Code","Product Name", "Total Stock","Price per Unit"))
        print("|{:^3}|{:^15}|{:^15}|{:^12}|{:^20}|".format("-"*3,"-"*15,"-"*15,"-"*12,"-"*20))
        for i in range(unlocked):
            print("|{:^3}|{:^15}|{:^15}|{:^12}|{:^20}|".format(i+1, self.listofProducts[i][0].productCode, self.listofProducts[i][0].productName, str(len(self.listofProducts[i]))+" "+self.listofProducts[i][0].productUOM,self.listofProducts[i][0].productPrice))
            i += 1
        print("-"*71)
        print()
```
ini dibawah untuk pilih mau cek produk mana secara detail. Kek misal baris pertama di tabel itu apel. Jadi klo user input '1' itu nanti lihat masing-masing apel, kek bs cek udh ada yg rusak atau expired. class stock ini ibaratnya kek rak-rak isi produknya gitu.
```
        interact = ""
        while interact != "0" or interact > str(unlocked) or interact < "0":
            if tutorial:
                print(f"Let's try to check our apples. Since apple is on the number '1' row, press '1', {name}.")
            else:
                print(f"Press '0' to go back to the main menu, or press a number between 1-{unlocked} to check each item of the product")
            interact = input("=> ")
            if tutorial:
                if interact != "1":
                    print("=> Press '1' to continue the tutorial.")
                    continue
            if "1" <= interact <= str(unlocked):
                self.restock(int(interact)-1)
                if tutorial:
                    tutorial = False
            elif interact == "0":
                break
            else:
                print("=> there is no product with that number. Try again.")
```

## di file program utama

ini untuk tutorial, kek demo cara mainnya

```
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
    print(f"=> Hello, {player.employeeName}. Welcome to your first shift.")
    print("=> There are three choices for you to pick everyday. Let's go over them one by one.")
    interact = None
    print()
    print("=> Try pressing '1' to check the minimarket's stock.")
    while interact != "1":
        interact = input("=> ")
        if interact != "1":
            print("=> Press '1'")
    print()
    stock.showStock(unlocked,player.employeeName,True)
```
terus di bawah ini untuk menu utama aplikasi kita. sebnrnya ini simpel aja, yg bikin panjang itu adlh gambar orang yg aku bikin AWKWKWKWK
```
def mainMenu():
    print("="*75)
    sleep(0.03)
    print("|{:^73}|".format(" "))
    print("|{:^73}|".format("MINIMARKET SIMULATOR"))
    sleep(0.03)
    print("|{:^73}|".format("*"*20))
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
        print("{:^74}".format("Loading"))
        print("{:^22}".format(" "),end="")
        for i in range(30):
            print("∎",end="")
            sleep(0.02)
        print()
        print()
    return interact
```
ini gambar di menu utamanya :
```
   ________
  /        \_____         __________
 /__________\____|       |          |
 |    |  |  |            |  |  |    |
 |          |            |          |
 |    \__/  |            |  \__/    |
 |__________|            |__________|
 |        __|____        |          |
 |       |______|     ___|_____     |
 |    ______| |__   __||_____||__   |
 |    |          |  \_|_|_|_|_|_/   |
 |___ |__________|___\|_|_|_|_|/    |
 |                             |    |
```
jadi menu utamanya, klo ketik 'p' main game, terus ketik 'q' itu quit

abis itu, di bawah ini cuman deklarasi produk default. tp nnt condition nya aku randomize good/bad. ini cuman testing aja.

```
for i in range(7):
    stock.listofProducts[0].append(consumable("RA-759","APPLE",3.00,"PCS","GOOD",datetime.datetime(2023,12,1)))
for i in range(10):
    stock.listofProducts[1].append(nonConsumable("MK-011","MILK",3.00,"PCS","GOOD"))
```
