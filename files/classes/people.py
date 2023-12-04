import math
from datetime import datetime
from time import sleep
from random import randrange
from productsAndStock import nonConsumable

# class Customer/pelanggan
class Customer:
	def __init__(self):
		self.cart = []
	
	#kek 'mengisi keranjang' lah dengan produk2. ini nanti bakal diambil secara random
	def fillCart(self, stock):
		available = [i for i in range(1, stock.unlocked + 1)]
		limit = randrange(1, 8) #satu customer cuman bisa ambil sampai 7 barang aja gitu
		taken = 0
		while taken < limit:
				if available == []:
						if taken == 0: return False
						else: break
				x = randrange(min(available),max(available) + 1) - 1 #produk yang akan diambil customer

				tmp = stock.shelf[x]
				i = 0
				while tmp[i].condition == "BAD":
					i += 1
					if i >= len(tmp): return False
				# JGN LUPA BIKIN KONDISI UTK EXPIRED PNY
				self.cart.append(tmp[i])
				stock.removeProducts(x, i)
				taken += 1
				if stock.shelf[x] == []:
					available.pop(x)

		self.cart = sorted(self.cart, key = lambda x : x.name)
		return True
	
	def __repr__(self):
		print("Customer's items:")
		sleep(0.3)
		for i in self.cart:
			print("{:<10} {:<10} {:<10} {:<4}".format(i.code, i.name, i.price, i.condition))
			sleep(0.3)
		return ""
	
# class player
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
				return self.EmployeeNameCheck()
			return name.title()
	
	# proses game utamanya, kek bayar, kasi kembalian, dll
	def ProcessPayment(self, customer, stock, mistake):
			print(f"\nMISTAKES : {mistake} / 3\n")
			print(customer)
			sleep(0.6)

			items = {i.name : 0 for i in customer.cart}
			for i in customer.cart: items[i.name] += 1

			allItems = [stock.shelf[i][0].name for i in range(stock.unlocked)]
			allPrices = [stock.shelf[i][0].price for i in range(stock.unlocked)]

			print()
			sleep(0.3)
			print("="*75)
			print()
			print("{: ^75}".format("NEW PAYMENT"))
			print("Available Items in minimarket : ")
			sleep(0.3)

			for i in range(stock.unlocked): print(str(i+1) + ". " + allItems[i])

			receipts = []

			customerItems = { i : 0 for i in list(items.keys())}

			while mistake < 5:
				while len(receipts) != len(customerItems):
					try: 
						possibleErrors = [
							"Please input a number",
							"The customer does not have that product in their cart",
							"That is the wrong number of quantity of this item",
							"You have already input that product before."
						]
						idx = 0
						if mistake >= 3: return mistake
						it = int(input(f"PRODUCT (1 - {stock.unlocked}) : "))
						if allItems[it - 1] not in customerItems:
							idx = 1
							raise ValueError
						if customerItems[allItems[it-1]]:
							idx = 3
							raise ValueError
						idx = 0
						qt = int(input("QUANTITY OF PRODUCT : "))
						if qt != items[allItems[it - 1]]:
							idx = 2
							raise ValueError
						customerItems[allItems[it-1]] = 1
						receipts.append({it : qt})
						print("Item has been added.\n")
					except ValueError:
						mistake += 1
						print("=>",possibleErrors[idx])
						print(f"=> MISTAKES : {mistake} / 3\n")
				break
			total = 0
			# PRINT RECEIPT
			print("="*75), sleep(0.03)
			print("|{:^73}|".format(" ")), sleep(0.03)
			print("|{:^73}|".format("COOL MINIMARKET")), sleep(0.03)
			print("|{:^73}|".format(" ")), sleep(0.03)
			print("|{:^73}|".format(datetime.now().strftime("%c"))), sleep(0.03)
			print("|{:^73}|".format(" ")), sleep(0.03)
			print("|{:^73}|".format(f"Cashier : {self.code} - {self.name}")), sleep(0.03)
			print("|{:^73}|".format(" ")), sleep(0.03)
			for i in receipts:
				for x, y in i.items():
					price = allPrices[x - 1]
					total += y * price
					print("|{:<10}{:<25}{:17} x ${:<4}{:>13}|".format(" ", allItems[x-1], y, "%.2f" % price ," "))
					sleep(0.03)
			print("|{:^73}|".format(" "))
			sleep(0.03)
			print("|{:<10}{:<52}+{:>10}|".format(" ", "="*50, " "))
			sleep(0.03)
			print("|{:^73}|".format(" "))
			sleep(0.03)
			print("|{:<10}{:<7} : {:>40}{:>13}|".format(" ", "TOTAL", "$" + str("%.2f" % total), " "))
			sleep(0.03)
			print("|{:^73}|".format(" "))
			sleep(0.03)
			print("="*75)

			# PROSES PENGEMBALIAN
			customerPaid = randrange(math.ceil(total) + abs(10 - math.floor(total)), math.ceil(total + 25)) + (randrange(0,100) / 100)
			print(f"\nCUSTOMER'S CASH : ${customerPaid}\n")
			print("Give the customer the correct amount of change :")
			changeNeeded = "%.2f" % (customerPaid - total)
			taken = 0
			cashInHand = []
			money = [
				{"name" : "1 cent", "value" : 0.01},
				{"name" : "5 cent", "value" : 0.05},
				{"name" : "10 cent", "value" : 0.1},
				{"name" : "25 cent", "value" : 0.25},
				{"name" : "50 cent", "value" : 0.5},
				{"name" : "1 dollar", "value" : 1},
				{"name" : "5 dollars", "value" : 5},
				{"name" : "10 dollars", "value" : 10},
				{"name" : "50 dollars", "value" : 50},
				{"name" : "100 dollars", "value" : 100},
			]
			while True:
				try:
					possibleErrors = [
						"Input a number 1-3",
						"Input a number between 1-10",
						"You have given the customer the wrong amount of change. Try again",
					]
					e = 0
					print(f"cash taken out from register : {cashInHand}, total = {taken}")
					print(f"change needed : {changeNeeded}")

					if taken:
						print("Pick an action to continue (1-3)")
						print("1. Take more money from cash register")
						print("2. Put back money into cash register")
						print("3. Give cash to customer and finish payment")
						action = int(input("=>"))
						if not 1 <= action <= 3: raise ValueError

					else: action = 1

					if action == 1:
						print("Pick 1 - 10 to select which bill to take from the cash register, or pick 0 to go back to the previous menu")
						for i in range(1,6): print("{:<3} {:<12} | {:<2}. {:<12}".format(str(i) + ".", money[i-1]["name"], str(i + 5) + ".", money[i + 5 - 1]["name"]))
						print()
						interact = int(input("=> "))
						if not 0 <= interact <= 10:
							e = 1
							raise ValueError
						if interact == 0 : continue
						taken += money[interact - 1]["value"]
						cashInHand.append(money[interact - 1]["name"])
					
					elif action == 2:
						tmp = { i + 1 : cashInHand[i] for i in range(len(cashInHand))}


				except ValueError:
					mistake += 1
					if mistake == 3: return mistake
					print(possibleErrors[e])

			return mistake
