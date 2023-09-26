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
    def restock(self):
        pass
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
    
    def showStock(self,unlocked,name,tutorial=False):
        print("-"*71)
        print("|{:^3}|{:^15}|{:^15}|{:^12}|{:^20}|".format("No.","Product Code","Product Name", "Total Stock","Price per Unit"))
        print("|{:^3}|{:^15}|{:^15}|{:^12}|{:^20}|".format("-"*3,"-"*15,"-"*15,"-"*12,"-"*20))
        for i in range(unlocked):
            print("|{:^3}|{:^15}|{:^15}|{:^12}|{:^20}|".format(i+1, self.listofProducts[i][0].productCode, self.listofProducts[i][0].productName, str(len(self.listofProducts[i]))+" "+self.listofProducts[i][0].productUOM,self.listofProducts[i][0].productPrice))
            i += 1
        print("-"*71)
        print()
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

    def restock(self, prod):
        print("tes")
