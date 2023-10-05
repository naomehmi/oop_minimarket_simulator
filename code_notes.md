# CODE NOTES

*** pas edit file ini, bikin kode pakek inisial di akhir paragraf jadi bisa tau siapa2 aja yang udah berkontribusi.

(4/10/23) saya suggest demo dulu codenya di laptop kalian. Aku udah sediakan tutorial singkat untuk game kita, biar nanti kalian bisa ngerti penjelasanku di bawah _- N_

## file minimarketClasses.py

### product class

```
from time import sleep
from random import randrange

class product:
    def __init__(self, productCode, productName, productPrice, productUOM, productCondition):
        self.productCode = productCode
        self.productName = productName
        self.productPrice = productPrice
        self.productUOM = productUOM
        self.productCondition = productCondition
```

Ini class produk. Keknya nama property nya boleh kupendekin, kek dari `self.productCode` jadi `self.code` doang, biar hemat tenaga jari. Propertinya ada kodenya, itu nanti dirandom aja, abis itu ada nama produk, harga, satuan unit, dan kondisinya masi bagus/rusak. Nah, aku juga terpikir untuk membuat kelas ini abstrak, karena aku sering silap pakek kelas ini padahal gabole, cuman bisa pakek consumable sm nonConsumable kita. Gimana menurut kelen? _- N_

<hr>

### consumable and nonConsumable classes

```
class consumable(product):
    def __init__(self, productCode, productName, productPrice, productUOM, productCondition, productExpDate):
        super().__init__(productCode, productName, productPrice, productUOM, productCondition)
        self.productExpDate = productExpDate

class nonConsumable(product):
    def __init__(self, productCode, productName, productPrice, productUOM, productCondition):
        super().__init__(productCode, productName, productPrice, productUOM, productCondition)
```

Ini dua adlh child dari class produk. `Consumable` untuk produk yg bisa expired kek makanan, klo `nonConsumable` untuk produk yg gk bs expired. Sejauh ini masi blm ada method, karena kek emg produknya bs ngapain T-T. Saya juga stuggle si buat exp date sm product condition, karena untuk exp aku agak bingung gimana randomize tgl nya, jadi di main program utk sementara aku bikin semua '1 week', nnt kalian mikir dulu idenya. Abis itu utk product condition, aku bikin ada 1 dlm 9 kemungkinan dia bad, sisanya good. di main program ada kutulis, tp keknya mending aku pindahin ke sini aja gak sih. _- N_

<hr>

### customer class

```
class customer:
    def __init__(self, customerName, customerCart):
        self.customerName = customerName
        self.customerCart = customerCart
    def fillCart(self):
        pass
    def pay(self):
        pass
```

Class customer, untuk pelanggan minimarket kita. Jadi cart saya kepikir bikin tipe datanya dictionary saja, kek cth {apel : 2 pcs, susu : 2pcs} gitu. nanti bakal randomize utk method `fillCart()` untuk isi produk2nya, dan kita harus pastikan gak bakal ngebug kek misal ambil apel 10 pcs padahal stock hanya tersedia 5 gitu. Bakal susah sepertinya, tp kita gak boleh nyerah. Untuk method pay, itu blm 100% yakin, itu biar trigger menjalankan method `cashier()` si employee, nanti kujelasin di bagian class employee _- N_

<hr>

### employee Class

```
class employee:
    def __init__(self, employeeCode, employeeName):
        self.employeeCode = employeeCode
        self.employeeName = employeeName
    def cashier(self):
        pass
```

Untuk class employee, cashier saya kepikir untuk ikut game ini di play store, namanya **Supermarket Cashier**. Jadi sistem gamenya, kita jadi kasir gitu input2, abis itu kasi kembalian berapa lbr 10rb, berapa lbr 5rb, harus uang pas untuk kembaliannya. Pakek while() seharusnya bisa lah buat method ini. Untuk demo bisa lihat di foto yg w udah lampirkan di github (nama filenya whatsapp bla bla bla), yang ada skema2 (buriq si tulisannya, but kira2 aja lah itu blm pasti). _- N_

<hr>

### minimarket class

```
class minimarket:
    def __init__ (self, minimarketMoney, minimarketCustomers, minimarketLevel, minimarketDay):
        self.minimarketMoney = minimarketMoney
        self.minimarketCustomers = minimarketCustomers
        self.minimarketLevel = minimarketLevel
        self.minimarketDay = minimarketDay
```

Saya kepikir untuk class minimarket bisa level up gitu, terus sehari berapa customers, bla bla bla. `money` ya sisa uang seluruh minimarket, `customer` itu jumlah pelanggan per hari, abis itu ada level (dimana klo udah naik bisa unlock lebih banyak item), terus day itu untuk hitung udah berapa lama si player main game ini. _- N_

<hr>

### stock class

ini bakal kupecahin jadi bbrp bagian karena ane padat si methodnya. _- N_

```
class stock:
    def __init__ (self, listofProducts, stockMaxCapacity):
        self.listofProducts = listofProducts
        self.stockMaxCapacity = stockMaxCapacity
```

Ini deklarasi property doang. jadi `listOfProducts` itu untuk tampilin dalam tabel semua produk kita, abis itu st`ockMaxCapacity buat jumlah maksimum per produk yang bisa dijual. Biar bisa menghindari player nya beli kek 1000000000 apel misalnya. Nanti per level bisa dinaikkan juga jumlahnya.

```
    def showStock(self,unlocked,tutorial=False):
        def printProducts():
            print("-"*60)
            print("|{:^3}|{:^15}|{:^12}|{:^25}|".format("No.","Product Name", "Total Stock","Price per Unit (USD)"))
            print("|{:^3}|{:^15}|{:^12}|{:^25}|".format("-"*3,"-"*15,"-"*12,"-"*25))
            for i in range(unlocked):
                print("|{:^3}|{:^15}|{:^12}|{:^25}|".format(i+1, self.listofProducts[i][0].productName, str(len(self.listofProducts[i]))+" "+self.listofProducts[i][0].productUOM,self.listofProducts[i][0].productPrice))
                i += 1
            print("-"*60)
            print()
            print(f"Press '0' to go back to the main menu, or press a number between 1-{unlocked} to check each item of the product.")
        printProducts()
        interact = ""
        while interact != "0" or interact > str(unlocked) or interact < "0":
            if tutorial:
                print(f"Let's try to check our apples. Since apple is on the No. '1' row, press '1'")
            interact = input("=> ")
            if tutorial:
                if interact != "1":
                    print("=> Press '1' to continue the tutorial.")
                    continue
            if "1" <= interact <= str(unlocked):
                if tutorial:
                    self.restock(int(interact)-1,True)
                    printProducts()
                    if tutorial:
                        print("=> Press 0 to return to the previous menu")
                    tutorial = False
                else:
                    self.restock(int(interact)-1)
            elif interact == "0":
                break
            else:
                print("=> there is no product with that number. Try again.")
```

def `printProducts()` untuk tampilkan dalam bentuk tabel. klo kalian ada nampak `if tutorial:` itu artinya klo misal lagi mode tutorial (alias `tutorial = True`), kodenya dijalankan. Tapi klo mode normal (`tutorial = False`), bagian kode itu diskip aja biar gak berbelit2. Jadi per baris ada setiap jenis produk yg dijual misal apel, susu, dsb. Jadi player tinggal ketik barisan yang mana yang ingin dicek secara detail (nnt akan dijelas di method `restock()`). nanti di method restock() baru bisa kek hapus produk, beli produk, dll. _- N_

```
    def restock(self, prod, tutorial=False):
        def printProducts():
            print()
            print("Product :",self.listofProducts[prod][0].productName)
            sleep(0.03)
            print("-"*50)
            sleep(0.03)
            print("|{:^3}|{:^15}|{:^15}|{:^12}|".format("No.","Product Code","Expiry Date","Condition"))
            sleep(0.03)
            print("|{:^3}|{:^15}|{:^15}|{:^12}|".format("-"*3,"-"*15,"-"*15,"-"*12))
            sleep(0.03)
            for i in range(len(self.listofProducts[prod])):
                print("|{:^3}|{:^15}|{:^15}|{:^12}|".format(i+1,self.listofProducts[prod][i].productCode,self.listofProducts[prod][i].productExpDate,self.listofProducts[prod][i].productCondition))
            sleep(0.03)
            print("-"*50)
            print()
            print("What would you like to do?")
            sleep(0.03)
            print("1. Buy more products")
            sleep(0.03)
            print("2. Discard a product")
            sleep(0.03)
            print("3. Go back")
            sleep(0.03)
            print("Pick one (1/2/3)")
            sleep(0.03)
        printProducts()
        if tutorial:
            print("\n=> It appears that there is an apple in our inventory that is in bad condition. We must get rid of it. Press '2' to discard a product.")
            first = False
            second = False
        interact = None
        while interact != "1" or interact != "2" or interact != "3":
            interact = input("=> ")
            if tutorial:
                if not first:
                    if interact != '2':
                        print("=> press '2'")
                        continue
                elif second:
                    if interact != "3":
                        print("=> press '3'")
                        continue
                else:
                    if interact != "1":
                        print("=> press '1'")
                        continue
```

untuk `restock()` aku bakal bagi jadi beberapa bagian. Yg di atas ini utk print tabelnya, misal kita pilih apel, terus kita bisa liat apel2 mana aja yang udah mau expired, apel2 mana aja yang udah busuk, dll. terus diberi pilihan, klo pilih 1 utk beli produk, klo pilih 2 utk buang produk, klo pilih 3 utk kembali ke menu sebelumnya. _- N_

```
            if interact == "1":
                print(f"\n=> How many {self.listofProducts[prod][0].productName.lower()}s do you want to purchase?")
                print("MAX CAPACITY PER PRODUCT :",self.stockMaxCapacity)
                temp = "-1"
                if tutorial:
                    print("\n=> The current maximum capacity of each product is 10.")
                    print("=> Press '3' to buy 3 more apples since we have 7 apples already, leaving 3 slots left.")
                while temp <= "0" or int(temp) > self.stockMaxCapacity or len(self.listofProducts[prod]) + int(temp) > self.stockMaxCapacity:
                    temp = input("=> ")
                    if tutorial:
                        if temp != "3":
                            print("press '3'")
                            continue
                    if temp <= "0":
                        print("=> Please input a number greater than 0.")
                    elif int(temp) > self.stockMaxCapacity or len(self.listofProducts[prod]) + int(temp) > self.stockMaxCapacity:
                        print(f"=> You currently have {len(self.listofProducts[prod])} items. You are only allowed to buy up to {self.stockMaxCapacity - len(self.listofProducts[prod])} items.")
                    else:
                        for i in range(int(temp)):
                            self.listofProducts[prod].append(consumable(self.listofProducts[prod][0].productCode[0:4]+str(randrange(1000,10000)),self.listofProducts[prod][0].productName,self.listofProducts[prod][0].productPrice,self.listofProducts[prod][0].productUOM,"GOOD","1 week"))
                        print(f"=> {temp} {self.listofProducts[prod][0].productName.lower()}s have been added into your inventory.\n")
                        break
                if tutorial:
                    second = True
                    printProducts()
                    print()
                    print("=> Now that we're done, go back to the previous menu by pressing '3'")
```

klo pilih 1, itu untuk beli produk baru. kek misal stock kita ada 7 apel, jadi mau restock lagi. ada dikasih batasan, kek misal `stockMaxCapacity` nya 10, jadi maksimumnya cmn beli 3 pcs. _- N_

```
            elif interact == "2":
                print(f"\n=> print the row number of the item you want to discard (1-{len(self.listofProducts[prod])})")
                if not first:
                    print("=> Since the apple in row '8' has gone bad. Press '8' to discard that item.")
                temp = "-1"
                while temp < "1" or temp > str(len(self.listofProducts[prod])):
                    temp = input("=> ")
                    if tutorial:
                        if not first:
                            if temp != "8":
                                temp = "-1"
                                print("=> press '8'")
                                continue
                    if "1" <= temp <= str(len(self.listofProducts[prod])):
                        print(f"=> Product {self.listofProducts[prod][int(temp)-1].productCode} on row {temp} has been discarded.")
                        self.listofProducts[prod].pop(int(temp)-1)
                        sleep(0.03)
                        printProducts()
                        if tutorial:
                            first = True
                            print("\n=> Now, let's restock and order some apples.")
                            print("=> Always make sure there are always enough products for customers everyday before you start your shift.")
                            print("=> The game will be over if there are not enough products that are in good condition and not expired yet.")
                            print("\n=> Press '1' to buy more products")
                        break
                    else:
                        print("=> There is no row with that number. Try again")
                    temp = "-1"
            elif interact == "3":
                print()
                break
            else:
                print("=> press '1',  '2', or '3'")
        print()
```

klo pilih 2, untuk buang produk, nanti ada tampil tabel dengan kode, expdate, kondisi masing2 produk. terus nanti disuru pilih barisan mana yg ingin dibuang. klo pilih 3, itu balik ke menu sblmnya. _- N_

<hr>

## file main.py

### def tutorialLevel()

```
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
```

ni untuk jalankan tutorial, nanti di bagian paling bawah ada `stock.showStock(unlocked, True)` kan, aku bikin True biar bisa jalankan program yg ada bagian `if tutorial:` yang ada di file `minimarketClasses.py`. _- N_

<hr>

### def mainMenu()

```
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
```

Ini untuk tampilkan menu utama, jadi klo dia pilih `p` dia jalankan program utama, klo `q` biar hentikan program. _- N_


<hr>

### program utama

```
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
```

ni w jelas perbaris yah:
1. pertama menu ambil klo value nya `p` atau `q`
2. kita declare object `miniMarket`, uang awal 1000 dolar, itu 3 anggap aja customer, baru level 1, baru masih shift/hari pertama 
3. `stock` itu aku declare list kosong, biar untuk tampilkan tabel. Ada 8 produk total yg aku rencana jual, ada kulist semua di file rough draft (paling bawah klo gk salah)
4. `unlocked` adlh produk yg kita ada. level 1 kita cuman bisa jual apel sm susu.
5. nah itu `cond` yg ada good bad itu, w buat untuk kondisi barang. jadi nanti aku randomize pas kita bikin object produk. Jadi ada 1 dalam 9 chance kondisinya buruk
6. terus `for` nya yg pertama, utk apel sementara aku bikin semua good sebanyak 7 untuk tutorialnya biar gak ada yang bad.
7. baru aku bikin 1 apel yg `bad` demi tutorial
8. nah `for` kedua ini, itu untuk generate 10 susu biar dijual
9. baru yg `if menu == 'p'`, itu mulai simulator nya
10. ada banyak tulisan bla bla, nanti ada tanya nama player terus kasi kode random
11. nnt ada tanya mau main tutorial atau gak, nanti jalankan `tutorialLevel()`, klo gak aku bikin `break` sementara karena blm buat kode game utamanya _- N_
