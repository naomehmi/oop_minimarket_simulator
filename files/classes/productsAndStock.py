from time import sleep
from random import randrange
import abc

# abstract class as template for consumable and non consumable (template pattern??)
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

# products with expiry dates
class Consumable(Product):
	code = ""
	name= ""
	price = 0
	uom = ""
	condition = ""
	def __init__(self, code, name, price, uom, expDate):
		self.code = code + "-" + str(randrange(1000,10000))
		self.name = name
		self.price = price
		self.uom = uom
		self.condition = "BAD" if randrange(0,9) == 1 else "GOOD" # there is a 1 in 9 chance the produuct is in bad condition
		self.expDate = expDate

# products without expiry dates
class nonConsumable(Product):
	code = ""
	name= ""
	price = 0
	uom = ""
	condition = ""
	def __init__(self, code, name, price, uom):
		self.code = code + "-" + str(randrange(1000,10000))
		self.name = name
		self.price = price
		self.uom = uom
		self.condition = "BAD" if randrange(0,9) == 1 else "GOOD"
		
# class to control every product in the minimarket, has an observer design pattern
# observer : stock, observed : consumable/non consumable
class Stock:
	_listOfProducts = [[] for _ in range(8)] # the minimarket sells 8 diff products
	maxCapacity = 10 # maximum amount of items per product, will increase as player levels up
	unlocked = 2 # the types of products that the minimarket sells for now, will increase as player levels up
	_allProducts = [
		{ "con" : 1 ,"code" : "AP", "name" : "APPLE", "price" : 3.00, "uom" : "PCS", "expDate" : "7 days", "cost" : 2.30 }, 
		{ "con" : 1 ,"code" : "MK", "name" : "MILK", "price" : 3.45, "uom" : "PCS", "expDate" : "7 days", "cost" : 2.95 }, 
		{ "con" : 1 ,"code" : "EG", "name" : "EGGS", "price" : 7.50, "uom" : "CARTONS", "expDate" : "10 days", "cost" : 6.68 }, 
		{ "con" : 0 ,"code" : "TS", "name" : "TISSUE", "price" : 5.00, "uom" : "PCS", "cost" : 4.40 }, 
		{ "con" : 1 ,"code" : "OV", "name" : "OLIVE OIL", "price" : 9.95, "uom" : "BOTTLE" , "expDate" : "15 days", "cost" : 7.77 }, 
		{ "con" : 0 ,"code" : "CH", "name" : "WOODEN CHAIR", "price" : 25.56, "uom" : "PCS", "cost" : 20.55 }, 
		{ "con" : 0 ,"code" : "TB", "name" : "WOODEN TABLE", "price" : 57.49, "uom" : "PCS", "cost" : 55.55 }, 
		{ "con" : 1 ,"code" : "RC", "name" : "RICE", "price" : 15.46, "uom" : "BAGS", "expDate" : "20 days", "cost" : 12.23 }
	] # every single product that is sold in the minimarket, acts a template to generate them
	# the 'con' key is to know whether the product is consumable or not (1 for consumable, 0 for non consumable), and the 'cost' is the price to restock each item of a product 

	# both _listOfProducts and _allProducts are protected attributes, so these property decorators are used so they can be called outside of this class
	@property 
	def shelf(self):
		return self._listOfProducts
	@property
	def products(self):
		return self._allProducts
	
	# to add items into the stock
	def generateProducts(self, idx, qty):
		tmp = self._allProducts[idx].copy() # copy the dictionary of the product we want to generate from _listOfProducts
		conOrNon = tmp["con"] # store the value of con (either 0 or 1)
		# remove con and cost key from the dictionary so making a new consumable/nonconsumable instance won't cause an error
		tmp.pop("con")
		tmp.pop("cost")
		if conOrNon: # conOrNon = 1 generate consumable
			for i in range(qty): self._listOfProducts[idx].append(Consumable(**tmp))
		else: # conOrNon = 0 generate non consumable
			for i in range(qty) : self._listOfProducts[idx].append(nonConsumable(**tmp))

	# to discard items from the stock
	def removeProducts(self, idx, row):
		self._listOfProducts[idx].pop(row)

	# every consumable product's expiry date minus 1 day
	def expire(self):
		for i in self._listOfProducts:
			if not i: break
			if i[0].__class__.__name__ == "Consumable":
				item = iter(i)
				while True:
					try:
						j = next(item)
						if j.expDate != "EXPIRED" :
							day = int(j.expDate[:2].rstrip()) - 1 # take the number of days left from .expDate and convert it to int
							j.expDate = "EXPIRED" if day <= 0 else str(day) + " days" # product becomes expired after reaching 0 days
							if j.expDate == "EXPIRED" : j.condition = "EXPIRED" # condition becomes bad if item is expired
					except StopIteration:
						break

	# stock control
	def displayStock(self, money):
		while True:
			print("\nMONEY : $" + "%.2f" % money)
			# table to show the available products that the player has unlocked
			print("-"*60)
			print("|{:^3}|{:^15}|{:^12}|{:^25}|".format("No.","Product Name", "Total Stock","Price per Unit (USD)"))
			print("|{:^3}|{:^15}|{:^12}|{:^25}|".format("-"*3,"-"*15,"-"*12,"-"*25))
			idx = 1
			for i in range(self.unlocked):
				prod = self._listOfProducts[i]
				print("|{:^3}|{:^15}|{:^12}|{:^25}|".format(idx,self._allProducts[i]["name"], str(len(prod)) + " " + self._allProducts[i]["uom"], "%.2f" % self._allProducts[i]["price"]))
				idx += 1
			print("-"*60)
			print(f"\nPress '0' to go back to the main menu, or press a number between 1-{self.unlocked} to check each item of the product.")
			# if player presses 0, goes back to main game in theGame.py. if the player selects the row of a product, goes to restockItems()
			try:
				interact = int(input("=> "))
				if not 0 <= interact <= self.unlocked: raise ValueError
				if interact == 0: return money
				money = self.restockItems(interact-1, money)
				if money < 0: return money
			except ValueError:
				print(f"Press a number between 1-{self.unlocked}\n")

	# this is where player can buy or discard items of a product
	def restockItems(self, idx, money):
		while True:
			prod = self._allProducts[idx] # the dictionary of product we want to add/discard
			className = "Consumable" if prod["con"] else "nonConsumable" 
			try: # format table
				print("\nMONEY : $" + "%.2f" % money) 
				print("\nProduct :",prod["name"])
				print(f"PRICE : ${'%.2f' % self._allProducts[idx]['cost']}/{self._allProducts[idx]['uom']}")
				print("-"*34,end="")
				if className == "Consumable": print("-"*16,end="")
				print("\n|{:^3}|{:^15}|".format("No.","Product Code"),end="")
				if className == "Consumable": print("{:^15}|".format("Expiry Date"),end="")
				print("{:^12}|".format("Condition"))
				print("|{:^3}|{:^15}|".format("-"*3,"-"*15),end="")
				if className == "Consumable": print("{:^15}|".format("-"*15),end="")
				print("{:^12}|".format("-"*12))
				j = 1
				prod = self._listOfProducts[idx]
				amt = len(prod)
				iterator = iter(prod)
				while True: # print items
					try:
						i = next(iterator)
						print("|{:^3}|{:^15}|".format(j,i.code),end="")
						if className == "Consumable": print("{:^15}|".format(i.expDate),end="")
						print("{:^12}|".format(i.condition))
						j += 1
					except StopIteration:
						break
				print("-"*34,end="")
				if className == "Consumable": print("-"*16,end="")
				print("\nWhat would you like to do?")
				print("1. Buy more products")
				print("2. Discard a product")
				print("3. Go back")
				print("Pick one (1/2/3)")
				sleep(0.03)
				interact = int(input("=> "))
				if not 1 <= interact <= 3: raise ValueError
				print()
				if interact == 1: # buy product
					if amt == self.maxCapacity: # cannot buy if the quantity of items has already reached the max capacity
						print(f"There is already {self.maxCapacity} items of this product. You cannot buy more than {self.maxCapacity} items for now.")
						continue
					while True:
						err = "Please input a number more than 0." # default error message
						try:
							print(f"Quantity : {amt}\nCurrent max capacity : {self.maxCapacity}") # quantity of items to buy
							print("\nHow many products do you want to add?")
							qty = int(input("=> "))
							if qty > self.maxCapacity - amt: # cannot buy more than max capacity
								err = f"You can only buy up to {self.maxCapacity - amt} for now" # change error message
								raise ValueError
							money -= self._allProducts[idx]["cost"] * qty # money is subtracted by cost of items
							self.generateProducts(idx, qty) # add the items into the stock
							print(f"\n=> {qty} product(s) have been added."), sleep(0.8)
							break
						except ValueError:
							print(err + "\n")
				elif interact == 2: # discard product
					if amt == 0: # if there are 0 items of this product, go back to previous menu
						print("There are no products to discard. I think you should buy more instead"), sleep(0.6)
						continue
					while True:
						try: # pick row of item to be discarded
							print(f"Which row do you want to discard (1-{amt})? Pick '0' to go back to the previous menu")
							row = int(input("=> "))
							if not 0 <= row <= amt: raise ValueError
							if row == 0: break
							print(f"Product {prod[row-1].code} has been discarded."), sleep(0.8)
							self.removeProducts(idx, row-1)
							break
						except ValueError:
							print(f"Input a number between 1-{amt}\n")
				elif interact == 3: break
			except ValueError:
				print("Press '1', '2', or '3'.")
		return money
