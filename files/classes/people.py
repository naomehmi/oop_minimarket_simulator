import math
from datetime import datetime
from time import sleep
from random import randrange

# customer class
class Customer:
	def __init__(self):
		self.cart = []
	
	# fill in customer's cart with random products
	def fillCart(self, stock):
		available = [i for i in range(1, stock.unlocked + 1)] # list of available products (1 - unlocked)
		limit = randrange(1, 8) # the max amount of items in customer's cart (randomized from 1-7)
		taken = 0 # the amount of items currently in customer's cart
		while taken < limit:
				if available == []: # if no products are available and the customer hasn't taken anything yet, game over
						if taken == 0: return False
						else: break
				x = randrange(0,len(available)) # randomly pick a type of product (index of available)
				if stock.shelf[available[x] - 1] == []: # if that product has 0 items, remove it from available 
					available.pop(x)
					continue
				tmp = stock.shelf[available[x] - 1] # tmp is a list of all items of that product
				i = 0
				condition = lambda y : tmp[y].condition == "BAD" # function to check if the product is in bad condition
				while (condition(i)): # skip that item if it's in bad condition/expired
					i += 1
					if i >= len(tmp): break
				if i >= len(tmp): # if all items of that product are bad/expired, remove that product from available
					available.pop(x)
					continue
				self.cart.append(tmp[i]) # if a good and unexpired item is available 
				stock.removeProducts(available[x] - 1, i) # remove that product from stock because it's taken
				taken += 1
		self.cart = sorted(self.cart, key = lambda x : x.name) # sort cart alphabetically
		return True
	
	def __repr__(self): # string representation of customer
		print("Customer's items:")
		sleep(0.3)
		for i in self.cart:
			print("{:<10} {:<10} {:<10}".format(i.code, i.name, i.price))
			sleep(0.3)
		return ""
	
# player
class Employee:
	def __init__(self):
		self.code = "EMPLOYEE"+str(randrange(1000,10000)) # randomized employee code
		self.name = "" # leave blank when instantialized

	def EmployeeNameCheck(self): # recursive function to validate employee name
			print("\n\n=> Before we start, what's your name? (Numbers, spaces, and symbols are not allowed)")
			try:
				name = input("=> ")
				if not name.isalpha():
						raise ValueError("=> Numbers, spaces, and symbols are not allowed. Please try again :)\n")
			except ValueError as e:
				print(str(e))
				return self.EmployeeNameCheck()
			self.name = name.title()
	
	# cashier process
	def ProcessPayment(self, customer, stock, mistake):
			print(f"\nMISTAKES : {mistake} / 3\n") # current mistakes
			print(customer), sleep(0.6) # print customer cart

			items = {i.name : 0 for i in customer.cart} # this dictionary is to get the quantity of the items in the customer's cart
			for i in customer.cart: items[i.name] += 1

			allItems = [stock.products[i]["name"] for i in range(stock.unlocked)] # every product name that the player has unlocked
			allPrices = [stock.products[i]["price"] for i in range(stock.unlocked)] # every product price that the player has unlocked

			print("="*75),sleep(0.3)
			print("\n{: ^75}\n".format("NEW PAYMENT"))
			print("Available Items in minimarket : "), sleep(0.3)

			for i in range(stock.unlocked): print(str(i+1) + ". " + allItems[i]) # print products that the player has unlocked
			print()
			receipts = [] # the products that the player has input into the cashier computer

			customerItems = { i : 0 for i in list(items.keys()) } # to check whether the player has input the product into the cashier computer yet 

			while len(receipts) != len(customerItems):
				try:
					possibleErrors = [
						f"Please input a number between 1-{stock.unlocked}",
						"The customer does not have that product in their cart",
						"That is the wrong number of quantity of this item",
						"You have already input that product before."
					] # possible error messages
					idx = 0
					if mistake >= 3: return mistake # game over if player makes 3 mistakes
					it = int(input(f"PRODUCT (1 - {stock.unlocked}) : ")) # player input which product is in the customer's cart
					if not 1 <= it <= stock.unlocked: raise ValueError
					if allItems[it - 1] not in customerItems: # if the chosen product is not in the customer's cart, mistake + 1
						idx = 1
						raise ValueError
					if customerItems[allItems[it-1]]: # if the chosen product has already been inputted before, mistake + 1
						idx = 3
						raise ValueError
					idx = 0
					qt = int(input("QUANTITY OF PRODUCT : ")) # quantity of that product in the customer's cart
					if qt != items[allItems[it - 1]]: # if quantity of product is wrong, mistake + 1
						idx = 2
						raise ValueError
					customerItems[allItems[it-1]] = 1 # mark product as already been inputted into cashier computer
					receipts.append({it : qt}) # append the product and its quantity
					print("Item has been added.\n")
				except ValueError:
					mistake += 1
					print("=>",possibleErrors[idx])
					print(f"=> MISTAKES : {mistake} / 3\n")

			total = 0 # total cost
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

			# payment
			lowestMultipleOf5 = math.ceil(total / 5) * 5 # round up the total cost the nearest multiple of 5
			customerPaid = randrange(lowestMultipleOf5, 10 * ((lowestMultipleOf5 // 10) + 1) + 1, 5) # the customer pays in a randomized amount of dollars between the nearest multiple of 5 up to the nearest multiple of 10
			print(f"\nCUSTOMER'S CASH : ${customerPaid}\n")
			if "%.2f" % customerPaid == "%.2f" % total: # if customer pays the exact amount of money
				print("Oh, the customer has paid the exact amount, so no change needed.")
			else:
				print("Give the customer the correct amount of change to finish the payment.")
				changeNeeded = (customerPaid - total) # change
				taken = 0.00 # change taken from the cash register
				cashInHand = []
				money = [ # all the money in the cash register
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
						if taken: # if some money has already been taken out, give player the option to put back money or hand customer money
							print("\nPick an action to continue (1-3)")
							print("1. Take more money from cash register")
							print("2. Put back money into cash register")
							print("3. Give cash to customer and finish payment")
							action = int(input("=> "))
							if not 1 <= action <= 3: raise ValueError
						else: action = 1 # if no money is taken yet from the cash register, jump to taking money from cash register
						# take money from cash register
						if action == 1:
							while True:
								try: # player picks which type of money to give to customer
									print("\nPick 1 - 10 to select which bill/coin to take from the cash register", end="")
									print(", or pick '0' to go back to the previous menu") if cashInHand else print()
									for i in range(1,6): print("{:<3} {:<7} | {:<2} {:<12}".format(str(i) + ".", money[i-1]["name"], str(i + 5) + ".", money[i + 5 - 1]["name"]))
									interact = int(input("=> "))
									if not 0 <= interact <= 10: raise ValueError("Pick a number between 1-10")
									if interact == 0 : continue
									unit = "bills" if interact > 5 else "coins"
									while True:
										try:
											# player picks quantity of the chosen money value to take
											e = "pick a number above 0" # error message
											print(f"\nHow many {money[interact - 1]['name']} {unit} do you want to take from the cash register? (Pick '0' to cancel)")
											qty = int(input("=> "))
											if not 0 <= qty : raise ValueError(e)
											if qty == 0: break # return to previous menu if input 0
											if money[interact - 1]["value"] * qty > changeNeeded + 10 or qty > 50: # if player takes out too much money at a time, raise valuerror
												e = "I think that's too much money, pick a smaller amount"
												raise ValueError("I think that's too much money, pick a smaller amount")
											for i in range(qty):
												cashInHand.append(money[interact - 1]["name"]) # append the money taken from cash register
											taken += money[interact - 1]["value"] * qty
											break
										except ValueError:
											print(str(e) + "\n")
									if qty != 0: break
								except ValueError:
									pass
						# put back money into cash register
						elif action == 2:
							tmp = {}
							for i in range(len(cashInHand)) : tmp[i+1] = cashInHand[i]
							print()
							for x, y in tmp.items(): print(f"{x}. {y}") # print all the money the player has taken out from the cash register
							print(f"\nWhich dollar bill/coin do you want to put back into the cash register (1-{len(cashInHand)})? or pick '0' to go back to the previous menu.")
							while True:
								try:
									it = int(input("=> "))
									if not 0 <= it <= len(cashInHand): raise ValueError
									if it == 0: break
									for i in money: # deduct amount of money taken by the value of the money being put back inside 
										if i["name"] == cashInHand[it - 1]: taken -= i["value"]
									cashInHand.pop(it-1) # remove that money from list
									break
								except ValueError:
									print(f"pick a number between 1-{len(cashInHand)}")
						# hand customer the change
						elif action == 3:
							if '%.2f' % taken == '%.2f' % changeNeeded: # if the returned change is correct, customer interaction is completed
								print("\nThe amount of change you have returned is correct.\nThe customer has left the minimarket.")
								break
							else: # if wrong, mistake + 1
								print("\nThe amount of change you have given is incorrect, try again.")
								mistake += 1
								print(f"=> MISTAKES : {mistake} / 3")
								if mistake == 3: return mistake
					except ValueError:
						print("Input a number between 1-3")
			return mistake
