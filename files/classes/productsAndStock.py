from time import sleep
from random import randrange
import abc

# class abstract product
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

# Consumable = Product yang ada exp date
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
		self.condition = "BAD" if randrange(0,9) == 1 else "GOOD"
		self.expDate = expDate

# Non Consumable = Product yang gak ada exp date
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
	
class Stock:
	_listOfProducts = [[] for _ in range(8)]
	maxCapacity = 10
	unlocked = 2
	_allProducts = [
		{ "con" : 1 ,"code" : "AP", "name" : "APPLE", "price" : 3.00, "uom" : "PCS", "expDate" : "7 days", "cost" : 2.00 }, 
		{ "con" : 1 ,"code" : "MK", "name" : "MILK", "price" : 3.45, "uom" : "PCS", "expDate" : "7 days", "cost" : 3.23 }, 
		{ "con" : 1 ,"code" : "EG", "name" : "EGGS", "price" : 7.50, "uom" : "CARTONS", "expDate" : "10 days", "cost" : 6.68 }, 
		{ "con" : 0 ,"code" : "TS", "name" : "TISSUE", "price" : 5.00, "uom" : "PCS", "cost" : 3.40 }, 
		{ "con" : 1 ,"code" : "OV", "name" : "OLIVE OIL", "price" : 9.95, "uom" : "BOTTLE" , "expDate" : "15 days", "cost" : 7.77 }, 
		{ "con" : 0 ,"code" : "CH", "name" : "WOODEN CHAIR", "price" : 25.56, "uom" : "PCS", "cost" : 20.55 }, 
		{ "con" : 0 ,"code" : "TB", "name" : "WOODEN TABLE", "price" : 57.49, "uom" : "PCS", "cost" : 55.55 }, 
		{ "con" : 1 ,"code" : "RC", "name" : "RICE", "price" : 15.46, "uom" : "BAGS", "expDate" : "20 days", "cost" : 12.23 }
	]

	@property
	def shelf(self):
		return self._listOfProducts
	
	@property
	def products(self):
		return self._allProducts

	def generateProducts(self, idx, qty):
		tmp = self._allProducts[idx].copy()
		conOrNon = tmp["con"]
		tmp.pop("con")
		tmp.pop("cost")
		if conOrNon:
			for i in range(qty): self._listOfProducts[idx].append(Consumable(**tmp))
		else:
			for i in range(qty) : self._listOfProducts[idx].append(nonConsumable(**tmp))

	def removeProducts(self, idx, row):
		self._listOfProducts[idx].pop(row)

	def expire(self):
		for i in self._listOfProducts:
			if not i: break
			if i[0].__class__.__name__ == "Consumable":
				for j in i:
					if j.expDate != "EXPIRED" :
						day = int(j.expDate[:2].rstrip()) - 1
						j.expDate = "EXPIRED" if day <= 0 else str(day) + " days"

	def displayStock(self, money):
		while True:
			print("\nMONEY : $" + "%.2f" % money)
			print("-"*60)
			print("|{:^3}|{:^15}|{:^12}|{:^25}|".format("No.","Product Name", "Total Stock","Price per Unit (USD)"))
			print("|{:^3}|{:^15}|{:^12}|{:^25}|".format("-"*3,"-"*15,"-"*12,"-"*25))
			idx = 1
			for i in range(self.unlocked):
				prod = self._listOfProducts[i]
				print("|{:^3}|{:^15}|{:^12}|{:^25}|".format(idx,self._allProducts[i]["name"], str(len(prod)) + " " + self._allProducts[i]["uom"], "%.2f" % self._allProducts[i]["price"]))
				idx += 1
			print("-"*60)
			print()
			print(f"Press '0' to go back to the main menu, or press a number between 1-{self.unlocked} to check each item of the product.")

			try:
				interact = int(input("=> "))
				if not 0 <= interact <= self.unlocked: raise ValueError
				if interact == 0: return money
				money = self.restockItems(interact-1, money)
				if money < 0: return money
			except ValueError:
				print(f"Press a number between 1-{self.unlocked}\n")

	def restockItems(self, idx, money):
		while True:
			prod = self._allProducts[idx]
			className = "Consumable" if prod["con"] else "nonConsumable"
			try:
				print("\nMONEY : $" + "%.2f" % money) 
				print("\nProduct :",prod["name"])
				print(f"PRICE : ${'%.2f' % self._allProducts[idx]['cost']}/{self._allProducts[idx]['uom']}")
				print("-"*34,end="")
				if className == "Consumable": print("-"*16,end="")
				print()
				print("|{:^3}|{:^15}|".format("No.","Product Code"),end="")
				if className == "Consumable": print("{:^15}|".format("Expiry Date"),end="")
				print("{:^12}|".format("Condition"))
				print("|{:^3}|{:^15}|".format("-"*3,"-"*15),end="")
				if className == "Consumable": print("{:^15}|".format("-"*15),end="")
				print("{:^12}|".format("-"*12))
				j = 1
				prod = self._listOfProducts[idx]
				amt = len(prod)
				for i in prod:
					print("|{:^3}|{:^15}|".format(j,i.code),end="")
					if className == "Consumable": print("{:^15}|".format(i.expDate),end="")
					print("{:^12}|".format(i.condition))
					j += 1
				print("-"*34,end="")
				if className == "Consumable": print("-"*16,end="")
				print("\n\n")
				print("What would you like to do?")
				print("1. Buy more products")
				print("2. Discard a product")
				print("3. Go back")
				print("Pick one (1/2/3)")
				sleep(0.03)
				interact = int(input("=> "))
				if not 1 <= interact <= 3: raise ValueError
				print()
				if interact == 1:
					if amt == self.maxCapacity:
						print(f"There is already {self.maxCapacity} items of this product. You cannot buy more than {self.maxCapacity} items for now.")
						continue
					while True:
						err = "Please input a number more than 0."
						try:
							print(f"Quantity : {amt}\nCurrent max capacity : {self.maxCapacity}")
							print("\nHow many products do you want to add?")
							qty = int(input("=> "))
							if qty > self.maxCapacity - amt:
								err = f"You can only buy up to {self.maxCapacity - amt} for now"
								raise ValueError
							money -= self._allProducts[idx]["cost"] * qty
							self.generateProducts(idx, qty) if className == "Consumable" else self.generateProducts(idx, qty)
							print(f"\n=> {qty} product(s) have been added."), sleep(0.8)
							break
						except ValueError:
							print(err + "\n")
				elif interact == 2:
					if amt == 0:
						print("There are no products to discard. I think you should buy more instead"), sleep(0.6)
						continue
					while True:
						try:
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
