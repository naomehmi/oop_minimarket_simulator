#CLASS STOCK MASI NGEBUG AMITOFO

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
        print("-"*60)
        print("|{:^3}|{:^15}|{:^12}|{:^25}|".format("No.","Product Name", "Total Stock","Price per Unit (USD)"))
        print("|{:^3}|{:^15}|{:^12}|{:^25}|".format("-"*3,"-"*15,"-"*12,"-"*20))
        for i in range(unlocked):
            print("|{:^3}|{:^15}|{:^12}|{:^25}|".format(i+1, self.listofProducts[i][0].productName, str(len(self.listofProducts[i]))+" "+self.listofProducts[i][0].productUOM,self.listofProducts[i][0].productPrice))
            i += 1
        print("-"*60)
        print()
        interact = ""
        while interact != "0" or interact > str(unlocked) or interact < "0":
            if tutorial:
                print(f"Let's try to check our apples. Since apple is on the No. '1' row, press '1'")
            else:
                print(f"Press '0' to go back to the main menu, or press a number between 1-{unlocked} to check each item of the product")
            interact = input("=> ")
            if tutorial:
                if interact != "1":
                    print("=> Press '1' to continue the tutorial.")
                    continue
            if "1" <= interact <= str(unlocked):
                if tutorial:
                    self.restock(int(interact)-1,True)
                    tutorial = False
                else:
                    self.restock(int(interact)-1)
            elif interact == "0":
                break
            else:
                print("=> there is no product with that number. Try again.")

    def restock(self, prod, tutorial=False):
        def printProducts():
            print("Product :",self.listofProducts[prod][0].productName)
            print("-"*50)
            print("|{:^3}|{:^15}|{:^15}|{:^12}|".format("No.","Product Code","Expiry Date","Condition"))
            print("|{:^3}|{:^15}|{:^15}|{:^12}|".format("-"*3,"-"*15,"-"*15,"-"*12))
            for i in range(len(self.listofProducts[prod])):
                print("|{:^3}|{:^15}|{:^15}|{:^12}|".format(i+1,self.listofProducts[prod][i].productCode,self.listofProducts[prod][i].productExpDate,self.listofProducts[prod][i].productCondition))
            print("-"*50)
            print()
            print("What would you like to do?")
            print("1. Buy more products.")
            print("2. Discard a product")
            print("3. Go back")
            print("Pick one (1/2/3)")
        printProducts()
        if tutorial:
            print("=> It appears that there is an apple in our inventory that is in bad condition. We must get rid of it. Press '2' to discard a product.")
        interact = None
        while interact != "1" or interact != "2" or interact != "3":
            interact = input("=> ")
            if tutorial:
                if interact != '2':
                    print("=> press '2'")
                    continue
            if interact == "1":
                print("one test")
            elif interact == "2":
                print(f"=> print the row number of the item you want to discard (1-{len(self.listofProducts[prod])})")
                temp = "-1"
                while temp < "1" and temp > str(len(self.listofProducts[prod])):
                    temp = input("=> ")
                    if "1" <= temp <= str(len(self.listofProducts[prod])):
                        self.listofProducts[prod].pop(int(temp)-1)
                    else:
                        print("=> There is no row with that number. Try again")
                    temp = "-1"
            elif interact == "3":
                print()
                break
            else:
                print("=> press '1',  '2', or '3'")
        print()
