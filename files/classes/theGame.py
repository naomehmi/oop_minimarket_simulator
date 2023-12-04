from time import sleep
from productsAndStock import *
from people import *
from sys import exit

class MINIMARKET:
	day = 1
	money = 500
	customersPerShift = 2

	def tutorialExplanation(self, player):
		print("TUTORIAL\n")
		print(f"=> Welcome to your first day of work, {player.name}. Your job is pretty simple, basically justs keep track of the minimarket's stock and process customer payment."),sleep(0.03)
		print("=> Before you start your shift for the day, you can check the minimarket's stock. You can discard expired items or products that are in bad condition. You can also restock items. If the minimarket runs out of items to sell to customers, you will be fired."),sleep(0.03)
		print("=> After you have started your shift, all you need to do is to input the items and quantity in the customer's cart into the cashier computer. For example: \n"),sleep(0.03)
		print("CUSTOMER'S CART:"),sleep(0.03)
		print("OLIVE OIL 9.95\nOLIVE OIL 9.95\nRICE 15.46\nRICE 15.46\nRICE 15.46\n"),sleep(0.03)
		print("=> That means the customer has 2 olive oil and 3 rice in their cart. Don't worry, our state-of-the-art cashier computer will make it easy for you."),sleep(0.03)
		print("=> Then once you're done inputting everything into the computer and calculating the total, the customer will pay the total in cash and you have to return the correct change."),sleep(0.03)
		print("=> For example, if the total is $12.50 and the customer pays $15, that means you have to return two $1 bills and one 50 cent coin"),sleep(0.03)
		print("=> You are not allowed to make 3 mistakes per shift, or you're fired"),sleep(0.03)
		print("=> The longer you play, you will be able to unlock more products and have bigger capacity to restock more items"),sleep(0.03)
		print(f"=> And of course, you are allowed to quit anytime, {player.name}, by simply picking 'resign' in the menu")
		sleep(2.5)
		print("=> I think that's it for the tutorial, good luck.")
		input("\n(press ENTER to continue...)")
		print()

	def mainMenu(self):
		display = [
				"  ________",
				" /        \_____         __________",
				"/__________\____|       |          |",
				"|    |  |  |            |  |  |    |",
				"|          |            |          |",
				"|    \__/  |            |  \__/    |",
				"|__________|            |__________|",
				"|        __|___         |          |",
				"|       |______|     ___|_____     |",
				"|    ______| |__   __||_____||__   |",
				"|    |          |  \_|_|_|_|_|_/   |",
				"|___ |__________|___\|_|_|_|_|/    |",
				"|                             |    |"
		]

		print("="*75),sleep(0.03)
		print("|{:^73}|".format(" "))
		print("|{:^73}|".format("MINIMARKET SIMULATOR")),sleep(0.03)
		print("|{:^73}|".format("*"*20)),sleep(0.03)
		print("|{:^73}|".format("created by cool")),sleep(0.03)
		print("|{:^73}|".format(" ")),sleep(0.03)
		for d in display: print("|{:^18}{:<36}{:^19}|".format(" ",d," ")),sleep(0.03)
		print("|{:^5}{:^62}{:^6}|".format(" ","-"*52," ")),sleep(0.03)
		print("|{:^73}|".format(" ")),sleep(0.03)
		print("|{:^73}|".format(" ")),sleep(0.03)
		print("|{:^73}|".format("PRESS 'P' TO PLAY")),sleep(0.03)
		print("|{:^73}|".format("PRESS 'Q' TO QUIT")),sleep(0.03)
		print("|{:^73}|".format(" ")),sleep(0.03)
		print("="*75)

		while True:
			try:
				interact = input("=> ").lower()
				if interact != 'p' and interact != 'q':
						raise ValueError
				break
			except ValueError:
				print("=> Press 'p' or 'q'")
		return interact
	
	def gameplay(self):
		if self.mainMenu() == "q": exit()

		print("\n{:^74}".format("Loading..."))
		print("{:^22}".format(" "),end="")
		for i in range(30):
			print("∎",end="")
			sleep(0.02)
		print("\n\n")

		# default stock
		stock = Stock()
		stock.generateProducts(0, 8)
		stock.generateProducts(1, 10)

		print("=> Before we start, what's your name? (Numbers, spaces, and symbols are not allowed)")
		player = Employee()
		print()

		print(f"=> Would you like to read the tutorial, {player.name}? (Y/N)")
		while True:
			try:
				interact = input("=> ").lower()
				print()
				if interact not in ["y", "n"]: raise ValueError
				if interact == "y": self.tutorialExplanation(player)
				break
			except ValueError as e:
				print("=> Press 'y' or 'n'")
				print(str(e))

		while True:
			sleep(0.3)
			print()
			print(f"DAY {self.day}")
			print("="*(4+len(str(self.day))))
			print()
			print("1. Check Minimarket's Stock"), sleep(0.3) #check stock barang sebelum mulai shift
			print("2. Start shift"), sleep(0.3) #mulai level
			print("3. Resign") #quit
			print("Pick an option (1/2/3).\n"), sleep(0.3)

			try:
				interact = int(input("=> "))
				if not 1 <= interact <= 3: raise ValueError
			except ValueError:
				print("=> Press '1', '2', or '3'.")
			print()

			# check stock
			if interact == 1:
				stock.displayStock()

			# shift starts and customers come in
			elif interact == 2:
				generateCustomers = [Customer() for i in range(self.customersPerShift)]

				idx = 1
				mistake = 0

				for customer in generateCustomers:
					if not customer.fillCart(stock):
						print("There are not enough products for the customers, you're fired :/")
						self.stats()
					print(f"Customer {idx} out of {self.customersPerShift}")
					mistake = player.ProcessPayment(customer, stock, mistake)
					if mistake == 3: print(f"=> Ah. You have made 3 mistakes. You're fired, {player.name}"), self.stats()
					idx += 1
					print()

				# NAIK LEVEL
				self.day += 1
				if self.day in [2, 3, 5, 6, 7]:
					stock.unlocked += 1
					#INSERT KODE HERE UTK GENERATE PRODUK BARU
				self.customersPerShift += 2
				stock.maxCapacity += 1

			# elif interact == 3:
			#     #nanti aku mau tampilin progress si player sini
			#     print("byebye test")
			#     self.stats()
			#     break
			# print()
	
	def stats(self):
		print("the end test")
		exit()
