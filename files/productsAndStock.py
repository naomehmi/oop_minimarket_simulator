from time import sleep
from random import randrange
from abc import ABC, abstractmethod
from os import system

# abstract class as template for consumable and non consumable (template pattern) + acts as Observer
class Product(ABC):
	def __init__(self, code, name, price, uom):
		self.code = code + "-" + str(randrange(1000, 10000))
		self.name = name
		self.price = price
		self.uom = uom
		self.condition = "BAD" if randrange(1, 10) == 1 else "GOOD"

	@property
	@abstractmethod
	def expDate(self):
		pass
	
	# observer
	@abstractmethod
	def update(self):
		pass

# products with expiry dates
class Consumable(Product):
	expDate = ""
	def __init__(self, code, name, price, uom, expDate):
		super().__init__(code, name, price, uom)
		self.expDate = expDate

	def update(self):
		if self.expDate == "EXPIRED" : self.condition = "BAD" # condition becomes bad if item is expired

# products without expiry dates
class NonConsumable(Product):
	def __init__(self, code, name, price, uom):
		super().__init__(code, name, price, uom)

	@property
	def expDate(self):
		return None
	
	def update(self):
		pass
		
# Product + Consumable + NonConsumable => Liskov Substitution Principle
		
# class to control every product in the minimarket, has an observer design pattern
# observable : stock, observer : consumable/non consumable
class Stock:
	_listOfProducts = [[] for _ in range(8)] # the minimarket sells 8 diff products, this is to store the observers
	maxCapacity = 10 # maximum amount of items per product, will increase as player levels up
	unlocked = 2 # the types of products that the minimarket sells for now, will increase as player levels up
	_ALLPRODUCTS = [
		{ "con" : 1 ,"code" : "AP", "name" : "APPLE", "price" : 3.00, "uom" : "PCS", "expDate" : "5 days", "cost" : 2.30 }, 
		{ "con" : 1 ,"code" : "MK", "name" : "MILK", "price" : 3.45, "uom" : "PCS", "expDate" : "6 days", "cost" : 2.95 }, 
		{ "con" : 1 ,"code" : "EG", "name" : "EGGS", "price" : 7.50, "uom" : "CARTONS", "expDate" : "10 days", "cost" : 6.68 }, 
		{ "con" : 0 ,"code" : "TS", "name" : "TISSUE", "price" : 5.00, "uom" : "PCS", "cost" : 4.40 }, 
		{ "con" : 1 ,"code" : "OV", "name" : "OLIVE OIL", "price" : 9.95, "uom" : "BOTTLE" , "expDate" : "15 days", "cost" : 7.77 }, 
		{ "con" : 0 ,"code" : "CH", "name" : "WOODEN CHAIR", "price" : 25.56, "uom" : "PCS", "cost" : 20.55 }, 
		{ "con" : 0 ,"code" : "TB", "name" : "WOODEN TABLE", "price" : 57.49, "uom" : "PCS", "cost" : 55.55 }, 
		{ "con" : 1 ,"code" : "RC", "name" : "RICE", "price" : 15.46, "uom" : "BAGS", "expDate" : "20 days", "cost" : 12.23 }
	] # every single product that is sold in the minimarket, acts a template to generate them
	# the 'con' key is to know whether the product is consumable or not (1 for consumable, 0 for non consumable), and the 'cost' is the price to restock each item of a product 

	# both _listOfProducts and _ALLPRODUCTS are protected attributes, so these property decorators are used so they can be called outside of this class
	@property 
	def shelf(self):
		return self._listOfProducts
	@property
	def products(self):
		return self._ALLPRODUCTS
	
	# to add items into the stock (add observer)
	def generateProducts(self, idx, qty):
		tmp = self._ALLPRODUCTS[idx].copy() # copy the dictionary of the product we want to generate from _listOfProducts
		conOrNon = tmp["con"] # store the value of con (either 0 or 1)
		# remove con and cost key from the dictionary so making a new consumable/Nonconsumable instance won't cause an error
		tmp.pop("con")
		tmp.pop("cost")
		if conOrNon: # conOrNon = 1 generate consumable
			for _ in range(qty): self._listOfProducts[idx].append(Consumable(**tmp))
		else: # conOrNon = 0 generate non consumable
			for _ in range(qty) : self._listOfProducts[idx].append(NonConsumable(**tmp))

	# to discard items from the stock (remove observer)
	def removeProducts(self, idx, row):
		self._listOfProducts[idx].pop(row)

	# notify
	def ChangeCondition(self):
		for i in self._listOfProducts:
			for j in i:
				j.update()

	# every consumable product's expiry date minus 1 day (update products)
	def expire(self):
		iterator = iter(self._listOfProducts)
		while True:
			try:
				i = next(iterator)
				if not i: break
				if isinstance(i[0], Consumable):
					item = iter(i)
					while True:
						try:
							j = next(item)
							if j.expDate != "EXPIRED" :
								day = int(j.expDate[:2].rstrip()) - 1 # take the number of days left from .expDate and convert it to int
								j.expDate = "EXPIRED" if day <= 0 else str(day) + " days" # product becomes expired after reaching 0 days
							self.ChangeCondition()	
						except StopIteration:
							break
			except StopIteration:
				break

class StockControl(ABC):
	@abstractmethod
	def formatTable(self, *args):
		pass

	@abstractmethod
	def execute(self):
		pass

class DisplayStock(StockControl):
	def __init__(self, stock, money):
		self.stock = stock
		self.money = money

	def formatTable(self, *args):
		a, b, c, d = map(str, list(args))
		print("|{:^3}|{:^15}|{:^12}|{:^25}|".format(a, b, c, d))

	def execute(self):
		while True:
			system('cls')
			print("\nMONEY : $" + "%.2f" % self.money)
			# table to show the available products that the player has unlocked
			print("-"*60)
			self.formatTable("No.","Product Name", "Total Stock","Price per Unit (USD)")
			self.formatTable("-"*3,"-"*15,"-"*12,"-"*25)
			idx = 1
			for i in range(self.stock.unlocked):
				prod = self.stock.shelf[i]
				self.formatTable(idx,self.stock.products[i]["name"], str(len(prod)) + " " + self.stock.products[i]["uom"], "%.2f" % self.stock.products[i]["price"])
				idx += 1
			print("-"*60)
			print(f"\nPress '0' to go back to the main menu, or press a number between 1-{self.stock.unlocked} to check each item of the product.")
			# if player presses 0, goes back to main game in theGame.py. if the player selects the row of a product, goes to restockItems()
			try:
				interact = int(input("=> "))
				if not 0 <= interact <= self.stock.unlocked: raise ValueError
				if interact == 0: return self.money
				self.money = RestockItems(self.stock, self.money, interact-1).execute()
				if self.money < 0: return self.money
			except ValueError: print(f"Press a number between 1-{self.stock.unlocked}\n"), sleep(0.5)

class RestockItems(StockControl):
	def __init__(self, stock, money, idx):
		self.stock = stock
		self.money = money
		self.idx = idx

	def formatTable(self, *args):
		con, text = list(args)
		print("|{:^3}|{:^15}|".format(text[0], text[1]),end="")
		if con: print("{:^15}|".format(text[2]),end="")
		print("{:^12}|".format(text[3]))

	def execute(self):
		while True:
			system('cls')
			prod = self.stock.products[self.idx] # the dictionary of product we want to add/discard
			className = bool(prod["con"]) 
			try: # print table
				print("\nMONEY : $" + "%.2f" % self.money) 
				print("\nProduct :",prod["name"])
				print("-"*34,end="")
				if className: print("-"*16,end="")
				print()
				TABLEHEADER = [
					["No.", "Product Code", "Expiry Date" , "Condition"],
					["-"*i for i in [3, 15, 15, 12]]
				]
				for i in TABLEHEADER: self.formatTable(className,i)
				j = 1
				prod = self.stock.shelf[self.idx]
				amt = len(prod)
				iterator = iter(prod)
				while True: # print items
					try:
						i = next(iterator)
						self.formatTable(className, [j, i.code, i.expDate, i.condition])
						j += 1
					except StopIteration:
						break
				print("-"*34,end="")
				if className: print("-"*16,end="")
				print("\nWhat would you like to do?\n1. Buy more products\n2. Discard a product\n3. Go back\nPick one (1/2/3)")
				sleep(0.03)
				interact = int(input("=> "))
				if not 1 <= interact <= 3: raise ValueError
				print()
				if interact == 1: # buy product
					if amt == self.stock.maxCapacity: # cannot buy if the quantity of items has already reached the max capacity
						print(f"There is already {self.stock.maxCapacity} items of this product. You cannot buy more than {self.stock.maxCapacity} items for now.")
						continue
					while True:
						err = "Please input a number more than 0." # default error message
						try:
							print(f"Quantity : {amt}\nCurrent max capacity : {self.stock.maxCapacity}") # quantity of items to buy
							print(f"Cost to Buy : ${'%.2f' % self.stock.products[self.idx]['cost']}/{self.stock.products[self.idx]['uom']}")
							print("\nHow many products do you want to add?")
							qty = int(input("=> "))
							if qty > self.stock.maxCapacity - amt: # cannot buy more than max capacity
								err = f"You can only buy up to {self.stock.maxCapacity - amt} for now" # change error message
								raise ValueError
							cost = self.stock.products[self.idx]["cost"] * qty
							self.money -= cost # money is subtracted by cost of items
							self.stock.generateProducts(self.idx, qty) # add the items into the stock
							print(f"(-${'%.2f' % cost})\n\n=> {qty} product(s) have been added."), sleep(0.8)
							break
						except ValueError:
							print(err + "\n")
				elif interact == 2: # discard product
					if amt == 0: # if there are 0 items of this product, go back to previous menu
						print("There are no products to discard. I think you should buy more instead"), sleep(0.9)
						continue
					while True:
						try: # pick row of item to be discarded
							print(f"Which row do you want to discard (1-{amt})? Pick '0' to go back to the previous menu")
							row = int(input("=> "))
							if not 0 <= row <= amt: raise ValueError
							if row == 0: break
							print(f"Product {prod[row-1].code} has been discarded."), sleep(0.8)
							self.stock.removeProducts(self.idx, row-1)
							break
						except ValueError:
							print(f"Input a number between 1-{amt}\n")
				elif interact == 3: break
			except ValueError:
				print("Press '1', '2', or '3'."), sleep(0.52)
		return self.money

# SOLID - Open/Closed Principle + Liskov Substitution Principle + Dependency Inversion (karena bergantung sm class product(abstract)
