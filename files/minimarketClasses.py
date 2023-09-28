#CLASS STOCK MASI NGEBUG AMITOFO
from time import sleep
from random import randrange

class product:
    def __init__(self, productCode, productName, productPrice, productUOM, productCondition):
        self.productCode = productCode
        self.productName = productName
        self.productPrice = productPrice
        self.productUOM = productUOM
        self.productCondition = productCondition

class consumable(product):
    def __init__(self, productCode, productName, productPrice, productUOM, productCondition, productExpDate):
        super().__init__(productCode, productName, productPrice, productUOM, productCondition)
        self.productExpDate = productExpDate

class nonConsumable(product):
    def __init__(self, productCode, productName, productPrice, productUOM, productCondition):
        super().__init__(productCode, productName, productPrice, productUOM, productCondition)

class customer:
    def __init__(self, customerName, customerCart):
        self.customerName = customerName
        self.customerCart = customerCart
    def fillCart(self):
        pass
    def pay(self):
        pass

class employee:
    def __init__(self, employeeCode, employeeName):
        self.employeeCode = employeeCode
        self.employeeName = employeeName
    def cashier(self):
        pass

class minimarket:
    def __init__ (self, minimarketMoney, minimarketCustomers, minimarketLevel, minimarketDay):
        self.minimarketMoney = minimarketMoney
        self.minimarketCustomers = minimarketCustomers
        self.minimarketLevel = minimarketLevel
        self.minimarketDay = minimarketDay

class stock:
    def __init__ (self, listofProducts, stockMaxCapacity):
        self.listofProducts = listofProducts
        self.stockMaxCapacity = stockMaxCapacity
    
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
