from time import sleep
from random import randrange

#ini keknya mau kubikin abstract tp blm tau
class product:
    def __init__(self, code, name, price, uom, condition):
        self.code = code
        self.name = name
        self.price = price
        self.uom = uom
        self.condition = condition

class consumable(product):
    def __init__(self, code, name, price, uom, condition, expDate):
        super().__init__(code, name, price, uom, condition)
        self.expDate = expDate

class nonConsumable(product):
    def __init__(self, code, name, price, uom, condition):
        super().__init__(code, name, price, uom, condition)

class customer:
    def __init__(self, name, cart):
        self.name = name
        self.cCart = cart
    #kek 'mengisi keranjanng' lah dengan produk2. ini nanti bakal diambil secara random
    def fillCart(self):
        pass
    #belum tau, mungkin kuhapus klo gak dipakek
    def pay(self):
        pass

class employee:
    def __init__(self, code, name):
        self.code = code
        self.name = name
    #proses game utamanya, kek bayar, kasi kembalian, dll
    def cashier(self):
        pass

#stats minimarket
class minimarket:
    def __init__ (self, money, customers, level, day):
        self.money = money
        self.customers = customers
        self.level = level
        self.day = day

#stock ini boleh kita anggap rak produk lah gitu
class stock:
    def __init__ (self, listofProducts, stockMaxCapacity):
        self.listofProducts = listofProducts
        self.stockMaxCapacity = stockMaxCapacity
    
    #menu tampilkan produk yg kita ada
    def showStock(self,unlocked,tutorial=False):
        def printProducts():
            print("-"*60)
            print("|{:^3}|{:^15}|{:^12}|{:^25}|".format("No.","Product Name", "Total Stock","Price per Unit (USD)"))
            print("|{:^3}|{:^15}|{:^12}|{:^25}|".format("-"*3,"-"*15,"-"*12,"-"*25))
            for i in range(unlocked):
                print("|{:^3}|{:^15}|{:^12}|{:^25}|".format(i+1, self.listofProducts[i][0].name, str(len(self.listofProducts[i]))+" "+self.listofProducts[i][0].uom,self.listofProducts[i][0].price))
                i += 1
            print("-"*60)
            print()
            print(f"Press '0' to go back to the main menu, or press a number between 1-{unlocked} to check each item of the product.")
        interact = ""
        while interact != "0" or interact > str(unlocked) or interact < "0":
            printProducts()
            if tutorial:
                print(f"Let's try to check our apples. Since apple is on the No. '1' row, press '1'")
            interact = input("=> ")
            if tutorial:
                if interact != "1":
                    print("=> Press '1' to continue the tutorial.\n")
                    continue
            if "1" <= interact <= str(unlocked):
                if tutorial:
                    self.restock(int(interact)-1,True)
                    printProducts()
                    print("\n=> Press '0' to return to the previous menu")
                    while interact != "0":
                        interact = input("=> ")
                        if interact != "0":
                            print("=> Press '0' to continue the tutorial.")
                    tutorial = False
                    break
                else:
                    self.restock(int(interact)-1)
            elif interact == "0":
                break
            else:
                print("=> there is no product with that number. Try again.")

    #untuk restock sm buang produk
    def restock(self, prod, tutorial=False):
        def printProducts():
            print()
            print("Product :",self.listofProducts[prod][0].name)
            sleep(0.03)
            print("-"*50)
            sleep(0.03)
            if(self.listofProducts[prod][0].__class__.__name__ == "consumable"):
                print("|{:^3}|{:^15}|{:^15}|{:^12}|".format("No.","Product Code","Expiry Date","Condition"))
                sleep(0.03)
                print("|{:^3}|{:^15}|{:^15}|{:^12}|".format("-"*3,"-"*15,"-"*15,"-"*12))
                sleep(0.03)
                for i in range(len(self.listofProducts[prod])):
                    print("|{:^3}|{:^15}|{:^15}|{:^12}|".format(i+1,self.listofProducts[prod][i].code,self.listofProducts[prod][i].expDate,self.listofProducts[prod][i].condition))
                sleep(0.03)
                print("-"*50)
            elif(self.listofProducts[prod][0].__class__.__name__ == "nonConsumable"):
                print("|{:^3}|{:^15}|{:^12}|".format("No.","Product Code","Condition"))
                sleep(0.03)
                print("|{:^3}|{:^15}|{:^12}|".format("-"*3,"-"*15,"-"*12))
                sleep(0.03)
                for i in range(len(self.listofProducts[prod])):
                    print("|{:^3}|{:^15}|{:^15}|{:^12}|".format(i+1,self.listofProducts[prod][i].code,self.listofProducts[prod][i].condition))
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
                        print("=> press '2' to continue the tutorial.")
                        continue
                elif second:
                    if interact != "3":
                        print("=> press '3' to continue the tutorial.")
                        continue
                else:
                    if interact != "1":
                        print("=> press '1' to continue the tutorial")
                        continue
            if interact == "1":
                print(f"\n=> How many {self.listofProducts[prod][0].name.lower()}s do you want to purchase?")
                print("=> MAX CAPACITY PER PRODUCT    :",self.stockMaxCapacity,self.listofProducts[prod][0].uom)
                print("=> CURRENT QUANTITY OF PRODUCT :",len(self.listofProducts[prod]),self.listofProducts[prod][0].uom)
                temp = "-1"
                if tutorial:
                    print("\n=> The current maximum capacity of each product is 10.")
                    print("=> Press '3' to buy 3 more apples since we have 7 apples already, leaving 3 slots left.")
                while temp <= "0" or int(temp) > self.stockMaxCapacity or len(self.listofProducts[prod]) + int(temp) > self.stockMaxCapacity:
                    temp = input("=> ")
                    if tutorial:
                        if temp != "3":
                            print("=> Press '3' to continue the tutorial")
                            continue
                    if temp <= "0":
                        print("=> Please input a number greater than 0.")
                    elif int(temp) > self.stockMaxCapacity or len(self.listofProducts[prod]) + int(temp) > self.stockMaxCapacity:
                        print(f"=> You currently have {len(self.listofProducts[prod])} items. You are only allowed to buy up to {self.stockMaxCapacity - len(self.listofProducts[prod])} items.")
                    else:
                        for i in range(int(temp)):
                            self.listofProducts[prod].append(consumable(self.listofProducts[prod][0].code[0:3]+str(randrange(1000,10000)),self.listofProducts[prod][0].name,self.listofProducts[prod][0].price,self.listofProducts[prod][0].uom,"GOOD","1 week"))
                        print(f"\n=> {temp} {self.listofProducts[prod][0].name.lower()}s have been added into your inventory.")
                        break
                if tutorial:
                    second = True
                    printProducts()
                    print()
                    print("=> Now that we're done, go back to the previous menu by pressing '3'")
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
                                print("=> press '8' to continue the tutorial.")
                                continue
                    if "1" <= temp <= str(len(self.listofProducts[prod])):
                        print(f"\n=> Product {self.listofProducts[prod][int(temp)-1].code} on row {temp} has been discarded.")
                        sleep(0.48)
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
