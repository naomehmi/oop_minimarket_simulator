from time import sleep
from random import randrange
from datetime import datetime
import abc

# FITUR YANG BELUM
# ================
# sistem manajemen keuangan (game ini bisa beli2 tp gk ada uanganya AWKWKWK)
# Design pattern gabung employee dan customer => employee.shiftGameplay(variabelCustomer) misal
# RAPIKAN FUNCTION GENERATEPRODUCTS() DI CLASS STOCK, BISA PAKAI DESIGN PATTERN UNTUK MERAPIKANNYA, jadi lgsg kek mis generateProducts(consumable(....))
# validasi agar customer tidak mengambil product yang bad/expired
# fak help me hiks

#class abstract product
class Product(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def code(self):
        pass
    @abc.abstractproperty
    def name(self):
        pass
    @abc.abstractproperty
    def price(self):
        pass
    @abc.abstractproperty
    def uom(self):
        pass
    @abc.abstractproperty
    def condition(self):
        pass

#Consumable = Product yang ada exp date
class Consumable(Product):
    code = ""
    name= ""
    price = 0
    uom = ""
    condition = ""
    def __init__(self, code, name, price, uom, condition, expDate):
        self.code = code
        self.name = name
        self.price = price
        self.uom = uom
        self.condition = condition
        self.expDate = expDate

#Product yang gak ada exp date
class nonConsumable(Product):
    code = ""
    name= ""
    price = 0
    uom = ""
    condition = ""
    def __init__(self, code, name, price, uom, condition):
        self.code = code
        self.name = name
        self.price = price
        self.uom = uom
        self.condition = condition

#class Customer/pelanggan
class Customer:
    def __init__(self, cart):
        self.cart = cart
    
    #kek 'mengisi keranjang' lah dengan produk2. ini nanti bakal diambil secara random
    def fillCart(self,unlocked, stock):
        available = [i for i in range(1,unlocked + 1)]

        for i in range(randrange(1,min(len(available),4))):
            if available == []:
                if i == 0:
                    print("There are not enough products for the customers, you're fired :/")
                    return False
                else:
                    break
            x = randrange(min(available),max(available) + 1) - 1
            self.cart.append(stock.listofProducts[x][0])
            stock.listofProducts[x].pop(0)
            if stock.listofProducts[x] == []:
                available.pop(x)
        return True

#class player
class Employee:
    def __init__(self):
        self.code = "EMPLOYEE"+str(randrange(1000,10000))
        self.name = self.EmployeeNameCheck()

    def EmployeeNameCheck(self):
        try:
            name = input("=> ")
            if not name.isalpha():
                raise ValueError("=> Numbers, spaces, and symbols are not allowed. Please try again :)\n")
        except ValueError as e:
            print(str(e))
            #mencoba terus sampe gak ValueError
            return self.EmployeeNameCheck()
        return name.title()
    
    #proses game utamanya, kek bayar, kasi kembalian, dll
    def ShiftGameplay(self, customer, stock, unlocked, mistake, tutorial=False):
        def printCart():
            print("Customer's items:")
            sleep(0.3)
            for i in customer.cart:
                print("{:<10} {:<10} {:<10}".format(i.code, i.name, i.price))
                sleep(0.3)

        customer.cart = sorted(customer.cart, key = lambda x : x.name)

        if tutorial:
            print("\n=> It is time to serve your first Customer.")
            print("\n=> Your task is to input the items that are in the customer's cart ")
            print("=> The items have already been sorted by name, so all you need to do is input the name of the product and the quantity of each product.")
            sleep(2.2)

        print(f"\nMISTAKES : {mistake} / 5\n")
        sleep(1)
        if tutorial:
            print("=> Here above, are the mistakes you are able to make per shift. If you have accumulated 5 mistakes, you will be fired. ")
            print("=> But since this is only a tutorial, you are allowed to make as many mistakes as you want so ignore it for now...\n")
            sleep(2.2)

        printCart()
        sleep(0.6)

        items = {i.name : 0 for i in customer.cart}
        for i in customer.cart: items[i.name] += 1
        allItems = [stock.listofProducts[i][0].name for i in range(unlocked)]
        allPrices = [stock.listofProducts[i][0].price for i in range(unlocked)]

        firstItem = list(items.keys())[0] # tutorial only
        firstQty = items[list(items.keys())[0]] #tutorial only

        if tutorial:
            print(f"\n=> As we can see, the customer has {firstQty} {firstItem}")
            print(f"=> On the cashier computer below, choose {firstItem}")
        print()
        sleep(0.3)
        print("="*75)
        print()
        print("{: ^75}".format("NEW PAYMENT"))
        print("Available Items in minimarket : ")
        sleep(0.3)

        for i in range(unlocked):
            print(str(i+1) + ". " + allItems[i])

        receipts = []

        customerItems = list(items.keys())

        while mistake < 5:
            while len(receipts) != len(customerItems):
                try: 
                    possibleErrors = [
                        "Please input a number",
                        "The customer does not have that product in their cart",
                        "That is the wrong number of quantity of this item",
                        f"Wrong. Choose {firstItem} please", # tutorial only
                        f"Wrong. Input {firstQty}" # tutorial only
                    ]
                    idx = 0
                    if mistake >= 5:
                        return mistake
                    it = int(input(f"PRODUCT (1 - {unlocked}) : "))
                    if allItems[it - 1] not in customerItems:
                        idx = 1 if not tutorial else 3
                        raise ValueError
                    idx = 0
                    qt = int(input("QUANTITY OF PRODUCT : "))
                    if qt != items[allItems[it - 1]]:
                        idx = 2 if not tutorial else 4
                        raise ValueError
                    receipts.append({it : qt})
                except ValueError:
                    mistake += 1 if not tutorial else 0
                    print("=>",possibleErrors[idx])
                    print(f"=> MISTAKES : {mistake} / 5\n")
            break

        # PRINT RECEIPT
        print("="*75)
        sleep(0.03)
        print("|{:^73}|".format(" "))
        sleep(0.03)
        print("|{:^73}|".format("COOL MINIMARKET"))
        sleep(0.03)
        print("|{:^73}|".format(" "))
        sleep(0.03)
        print("|{:^73}|".format(datetime.now().strftime("%c")))
        sleep(0.03)
        print("|{:^73}|".format(" "))
        sleep(0.03)
        print("|{:^73}|".format(f"Cashier : {self.code} - {self.name}"))
        sleep(0.03)
        print("|{:^73}|".format(" "))
        sleep(0.03)

        total = 0

        for i in receipts:
            for x, y in i.items():
                price = allPrices[x - 1]
                total += y * price
                print("|{:<10}{:<25}{:17} x ${:>4}{:>10}|".format(" ", allItems[x-1], y, price ," "))
                sleep(0.03)
        print("|{:^73}|".format(" "))
        sleep(0.03)
        print("|{:<10}{:<52}+{:>10}|".format(" ", "="*50, " "))
        sleep(0.03)
        print("|{:^73}|".format(" "))
        sleep(0.03)
        print("|{:<10}{:<7} : {:>43}{:>10}|".format(" ", "TOTAL", "$" + str(total), " "))
        sleep(0.03)
        print("|{:^73}|".format(" "))
        sleep(0.03)
        print("="*75)

        customerPaid = randrange(total, total + min([abs(i - total) for i in [500, 100, 50, 20, 10, 5]]))
        print(customerPaid)

        return mistake

#stats Minimarket
class Minimarket:
    def __init__ (self, money, Customers, level, day):
        self.money = money
        self.Customers = Customers
        self.level = level
        self.day = day

#stock ini boleh kita anggap rak produk lah gitu
class Stock:
    def __init__ (self, listofProducts, stockMaxCapacity):
        self.listofProducts = listofProducts
        self.stockMaxCapacity = stockMaxCapacity

    # menambah stok produk
    def generateProducts(self,quantity, product, className, tutorial=False):
        allProducts = [{
            "code" : "AP",
            "name" : "APPLE",
            "price" : 3.00,
            "uom" : "PCS",
            }, 
            
            {
            "code" : "MK",
            "name" : "MILK",
            "price" : 3.45,
            "uom" : "PCS",
            }, 
            
            {
            "code" : "EG",
            "name" : "EGGS",
            "price" : 7.50,
            "uom" : "CARTONS",
            }, 
            
            {
            "code" : "TS",
            "name" : "TISSUE",
            "price" : 5.00,
            "uom" : "PCS",
            }, 
            
            {
            "code" : "OV",
            "name" : "OLIVE OIL",
            "price" : 9.95,
            "uom" : "BOTTLE",
            }, 
            
            {
            "code" : "CH",
            "name" : "WOODEN CHAIR",
            "price" : 25.56,
            "uom" : "PCS",
            }, 
            
            {
            "code" : "TB",
            "name" : "WOODEN TABLE",
            "price" : 57.49,
            "uom" : "PCS",
            }, 
            
            {
            "code" : "RC",
            "name" : "RICE",
            "price" : 15.46,
            "uom" : "BAGS",
            }]

        cond = ["GOOD", "BAD", "GOOD","GOOD","GOOD", "GOOD", "GOOD", "GOOD"]

        if tutorial:
            for _ in range(quantity):
                self.listofProducts[product].append(Consumable(allProducts[product]["code"]+"-"+str(randrange(1000,10000)),allProducts[product]["name"],allProducts[product]["price"],allProducts[product]["uom"],"GOOD","7 days"))
            self.listofProducts[product].append(Consumable(allProducts[product]["code"]+"-"+str(randrange(1000,10000)),allProducts[product]["name"],allProducts[product]["price"],allProducts[product]["uom"],"BAD","7 days"))
            return
        
        if className == "Consumable":
            for _ in range(quantity):
                self.listofProducts[product].append(Consumable(allProducts[product]["code"]+"-"+str(randrange(1000,10000)),allProducts[product]["name"],allProducts[product]["price"],allProducts[product]["uom"],cond[randrange(1,1000)%8],"7 days"))
        else:
            for _ in range(quantity):
                self.listofProducts[product].append(nonConsumable(allProducts[product]["code"]+"-"+str(randrange(1000,10000)),allProducts[product]["name"],allProducts[product]["price"],allProducts[product]["uom"],cond[randrange(1,1000)%8]))
    
    #menu tampilkan produk yg kita ada
    def showStock(self,unlocked,tutorial=False):
        def printProducts():
            print("-"*60)
            print("|{:^3}|{:^15}|{:^12}|{:^25}|".format("No.","Product Name", "Total Stock","Price per Unit (USD)"))
            print("|{:^3}|{:^15}|{:^12}|{:^25}|".format("-"*3,"-"*15,"-"*12,"-"*25))
            i = 0
            prod = iter(self.listofProducts)
            while True:
                try:
                    a = next(prod)
                    if a == []:
                        raise StopIteration
                    print("|{:^3}|{:^15}|{:^12}|{:^25}|".format(i+1, self.listofProducts[i][0].name, str(len(self.listofProducts[i]))+" "+self.listofProducts[i][0].uom,"%.2f" % self.listofProducts[i][0].price))
                    i += 1
                except StopIteration:
                    break 
            print("-"*60)
            print()
            print(f"Press '0' to go back to the main menu, or press a number between 1-{unlocked} to check each item of the product.")
        interact = ""
        doneRestock = False
        while True:
            printProducts()
            if tutorial:
                print("\n=> Let's try to check our apples. Since apple is on row No. '1', press '1'.") if not doneRestock else print("Press '0' to return to the previous menu.")
                
            try:
                interact = int(input("=> "))
                if tutorial:
                    if interact != 1 and not doneRestock:
                        print("=> press '1' to continue the tutorial.\n")
                        continue
                    elif interact != 0 and doneRestock:
                        print("\n=> Press '0' to continue the tutorial")
                        continue
                    elif interact == 0 and doneRestock:
                        tutorial = False
                        break
                if 1 <= interact <= unlocked:
                    if tutorial:
                        self.restock(int(interact)-1,self.listofProducts[int(interact)-1][0].__class__.__name__,True)
                        doneRestock = True
                    else:
                        self.restock(int(interact)-1,self.listofProducts[int(interact)-1][0].__class__.__name__, False)
                elif interact == 0:
                    break
            except ValueError:
                print("=> There is no product with that number. Try again.\n")
                sleep(0.3)

    #untuk restock sm buang produk
    def restock(self, prod, className, tutorial=False):
        def printProducts():
            print()
            print("Product :",self.listofProducts[prod][0].name)
            print("-"*34,end="")
            if className == "Consumable":
                print("-"*16,end="")
            print()

            print("|{:^3}|{:^15}|".format("No.","Product Code"),end="")
            if className == "Consumable":
                print("{:^15}|".format("Expiry Date"),end="")
            print("{:^12}|".format("Condition"))
            print("|{:^3}|{:^15}|".format("-"*3,"-"*15),end="")
            if className == "Consumable":
                print("{:^15}|".format("-"*15),end="")
            print("{:^12}|".format("-"*12))
            j = 1

            for i in self.listofProducts[prod]:
                print("|{:^3}|{:^15}|".format(j,i.code),end="")
                if className == "Consumable":
                    print("{:^15}|".format(i.expDate),end="")
                print("{:^12}|".format(i.condition))
                j += 1

            print("-"*34,end="")

            if className == "Consumable":
                print("-"*16,end="")
            print()

            print()
            print("What would you like to do?")
            print("1. Buy more products")
            print("2. Discard a product")
            print("3. Go back")
            print("Pick one (1/2/3)")
            sleep(0.03)
        printProducts()

        if tutorial:
            print("\n=> It appears that there is an apple in our inventory that is in bad condition. We must get rid of it. Press '2' to discard a product.")
            first = False
            second = False

        while True:
            try:
                interact = int(input("=> "))

                if tutorial:
                    if not first:
                        if interact != 2:
                            print("=> press '2' to continue the tutorial.")
                            continue
                    elif second:
                        if interact != 3:
                            print("=> press '3' to continue the tutorial.")
                            continue
                    else:
                        if interact != 1:
                            print("=> press '1' to continue the tutorial")
                            continue
                
                else:
                    if interact > 3 or interact < 1:
                        raise ValueError
            
            except ValueError:
                print("=> Press '1', '2', or '3'")

            if interact == 1:
                print(f"\n=> How many {self.listofProducts[prod][0].name.lower()}s do you want to purchase?")
                print("=> MAX CAPACITY PER PRODUCT    :",self.stockMaxCapacity,self.listofProducts[prod][0].uom)
                print("=> CURRENT QUANTITY OF PRODUCT :",len(self.listofProducts[prod]),self.listofProducts[prod][0].uom)
                if tutorial:
                    print("\n=> The current maximum capacity of each product is 10.")
                    print("=> Press '3' to buy 3 more apples since we have 7 apples already, leaving 3 slots left.")
                while True:
                    try:
                        qty = int(input("=> "))
                        if tutorial:
                            if qty != 3:
                                print("=> Press '3' to continue the tutorial")
                                continue
                        if qty <= 0:
                            raise ValueError("=> Please input a number greater than 0.")
                        elif qty > self.stockMaxCapacity or len(self.listofProducts[prod]) + int(qty) > self.stockMaxCapacity:
                            raise ValueError(f"=> You currently have {len(self.listofProducts[prod])} items. You are only allowed to buy up to {self.stockMaxCapacity - len(self.listofProducts[prod])} items.")
                        else:
                            self.generateProducts(int(qty),prod,self.listofProducts[prod][0].__class__.__name__)
                            print(f"\n=> {qty} {self.listofProducts[prod][0].name.lower()}s have been added into your inventory.")
                            sleep(0.3)
                            printProducts()
                            break
                    except ValueError as e:
                        print(str(e))

                if tutorial:
                    second = True
                    print()
                    print("=> Now that we're done, go back to the previous menu by pressing '3'")

            elif interact == 2:
                print(f"\nPrint the row number of the item you want to discard (1-{len(self.listofProducts[prod])})")
                if tutorial and not first:
                    print("=> Since the apple in row '8' has gone bad. Press '8' to discard that item.")
                while True:
                    try:
                        rowNum = int(input("=> "))
                        if tutorial:
                            if not first:
                                if rowNum != 8:
                                    print("=> press '8' to continue the tutorial.")
                                    continue
                        if 1 <= rowNum <= len(self.listofProducts[prod]):
                            print(f"\n=> Product {self.listofProducts[prod][rowNum-1].code} on row {rowNum} has been discarded.")
                            sleep(0.48)
                            self.listofProducts[prod].pop(rowNum-1)
                            sleep(0.03)
                            printProducts()
                            if tutorial:
                                first = True
                                print("\n=> Now, let's restock and order some apples.")
                                print("=> Always make sure there are always enough products for Customers everyday before you start your shift.")
                                print("=> The game will be over if there are not enough products that are in good condition and not expired yet.")
                                print("\n=> Press '1' to buy more products")
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("=> There is no row with that number. Try again.")
            elif interact == 3:
                print()
                break
