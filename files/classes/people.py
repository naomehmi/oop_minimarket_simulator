import math
from datetime import datetime
from time import sleep
from random import randrange

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
				x = randrange(0,len(available)) #produk yang akan diambil customer
				if stock.shelf[available[x] - 1] == []:
					available.pop(x)
					continue
				tmp = stock.shelf[available[x] - 1]
				i = 0
				condition = lambda y : tmp[y].condition == "BAD" 
				exp = lambda y : tmp[y].expDate == "EXPIRED" if tmp[y].__class__.__name__ == "Consumable" else False
				while (condition(i) or exp(i)) and i < len(tmp) - 1:
					i += 1
				if i >= len(tmp): continue
				self.cart.append(tmp[i])
				stock.removeProducts(available[x] - 1, i)
				taken += 1
				if i >= len(tmp):
					available.pop(x)
					continue

		self.cart = sorted(self.cart, key = lambda x : x.name)
		return True
	
	def __repr__(self):
		print("Customer's items:")
		sleep(0.3)
		for i in self.cart:
			print("{:<10} {:<10} {:<10}".format(i.code, i.name, i.price))
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

			allItems = [stock.products[i]["name"] for i in range(stock.unlocked)]
			allPrices = [stock.products[i]["price"] for i in range(stock.unlocked)]

			print()
			sleep(0.3)
			print("="*75)
			print()
			print("{: ^75}".format("NEW PAYMENT"))
			print("Available Items in minimarket : ")
			sleep(0.3)

			for i in range(stock.unlocked): print(str(i+1) + ". " + allItems[i])

			receipts = []

			customerItems = { i : 0 for i in list(items.keys()) }

			while mistake < 5:
				while len(receipts) != len(customerItems):
					try: 
						possibleErrors = [
							f"Please input a number between 1-{stock.unlocked}",
							"The customer does not have that product in their cart",
							"That is the wrong number of quantity of this item",
							"You have already input that product before."
						]
						idx = 0
						if mistake >= 3: return mistake
						it = int(input(f"PRODUCT (1 - {stock.unlocked}) : "))
						if not 1 <= it <= stock.unlocked: raise ValueError
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
					print("|{:<10}{:<25}{:17} x ${:<4}{:>13}|".format(" ", allItems[x-1], y, "%.2f" % price ," ")), sleep(0.03)
			print("|{:^73}|".format(" ")), sleep(0.03)
			print("|{:<10}{:<52}+{:>10}|".format(" ", "="*50, " ")), sleep(0.03)
			print("|{:^73}|".format(" ")), sleep(0.03)
			print("|{:<10}{:<7} : {:>40}{:>13}|".format(" ", "TOTAL", "$" + str("%.2f" % total), " ")), sleep(0.03)
			print("|{:^73}|".format(" ")), sleep(0.03)
			print("="*75)

			# PROSES PENGEMBALIAN
			lowestMultipleOf5 = math.ceil(total / 5) * 5
			customerPaid = randrange(lowestMultipleOf5, 10 * ((lowestMultipleOf5 // 10) + 1) + 1, 5)
			print(f"\nCUSTOMER'S CASH : ${customerPaid}\n")
			print("\nGive the customer the correct amount of change to finish the payment.")
			changeNeeded = (customerPaid - total)
			taken = 0.00
			cashInHand = []
			money = [
				{"name" : "1 cent", "value" : 0.01},
				{"name" : "5 cent", "value" : 0.05},
				{"name" : "10 cent", "value" : 0.10},
				{"name" : "25 cent", "value" : 0.25},
				{"name" : "50 cent", "value" : 0.50},
				{"name" : "1 dollar", "value" : 1.00},
				{"name" : "5 dollars", "value" : 5.00},
				{"name" : "10 dollars", "value" : 10.00},
				{"name" : "50 dollars", "value" : 50.00},
				{"name" : "100 dollars", "value" : 100.00},
			]
			while True:
				try:
					print(f"\nCash taken : {cashInHand}, total = {'%.2f' % taken}")
					print(f"\nChange needed for customer : {'%.2f' % changeNeeded}")

					if taken:
						print("\nPick an action to continue (1-3)")
						print("1. Take more money from cash register")
						print("2. Put back money into cash register")
						print("3. Give cash to customer and finish payment")
						action = int(input("=> "))
						if not 1 <= action <= 3: raise ValueError

					else: action = 1

					if action == 1:
						while True:
							try:
								print("\nPick 1 - 10 to select which bill/coin to take from the cash register", end="")
								print(", or pick '0' to go back to the previous menu") if cashInHand else print()
								for i in range(1,6): print("{:<3} {:<7} | {:<2} {:<12}".format(str(i) + ".", money[i-1]["name"], str(i + 5) + ".", money[i + 5 - 1]["name"]))
								interact = int(input("=> "))
								if not 0 <= interact <= 10:
									e = 1
									raise ValueError("Pick a number between 1-10")
								if interact == 0 : continue
								unit = "bills" if interact > 5 else "coins"
								while True:
									try:
										print(f"\nHow many {money[interact - 1]['name']} {unit} do you want to take from the cash register? (Pick '0' to cancel)")
										qty = int(input("=> "))
										if not 0 <= qty : raise ValueError("Input a number greater than or equal to 0")
										if qty == 0: break
										if money[interact - 1]["value"] * qty > changeNeeded + 10 or qty > 50: raise ValueError("I think that's too much money, pick a smaller amount")
										for i in range(qty):
											cashInHand.append(money[interact - 1]["name"])
										taken += money[interact - 1]["value"] * qty
										break
									except ValueError as e:
										print(str(e) + "\n")
								if qty != 0: break
							except ValueError:
								pass
					
					elif action == 2:
						tmp = {}
						for i in range(len(cashInHand)) : tmp[i+1] = cashInHand[i]
						print()
						for x, y in tmp.items(): print(f"{x}. {y}")
						print(f"\nWhich dollar bill/coin do you want to put back into the cash register (1-{len(cashInHand)})? or pick '0' to go back to the previous menu.")
						while True:
							try:
								it = int(input("=> "))
								if not 0 <= it <= len(cashInHand): raise ValueError
								if it == 0: break
								for i in money:
									if i["name"] == cashInHand[it - 1]: taken -= i["value"]
								cashInHand.pop(it-1)
								break
							except ValueError:
								print(f"pick a number between 1-{len(cashInHand)}")

					elif action == 3:
						if '%.2f' % taken == '%.2f' % changeNeeded:
							print("\nThe amount of change you have returned is correct.\nThe customer has left the minimarket.")
							break
						else:
							print("\nThe amount of change you have given is incorrect, try again.")
							mistake += 1
							print(f"=> MISTAKES : {mistake} / 3")
							if mistake == 3: return mistake

				except ValueError:
					print("Input a number between 1-3")

			return mistake
