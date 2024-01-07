from productsAndStock import *
from people import *
from printFormat import PRINT73

from sys import exit
from time import sleep
from random import randrange
from os import system

class MINIMARKET:
	# facade pattern
	def __init__(self):
		self.day = 1 # level
		self.money = 100 # starter money
		self.customersPerShift = 2 # the amount of customers per level
		self.stock = Stock() # stock of the entire minimarket
		self.player = Employee() # player
		self.StockControl = StockControl(self.stock) # interface to control minimarket inventory
		self.minReward = 80 # the lowest possible value for a reward after completing a shift
		self.maxReward = 151 # the highest possible value for a reward after completing a shift
		
	# tutorial
	def tutorialExplanation(self):
		print("\nTUTORIAL\n")
		print(f"=> Welcome to your first day of work, {self.player.name}. Your job is pretty simple, basically just keep track of the minimarket's stock and process customer payment."),sleep(0.3)
		print("=> Before you start your shift for the day, you can check the minimarket's stock. You can discard expired items or products that are in bad condition. You can also restock items. If the minimarket runs out of items to sell to customers, you will be fired."),sleep(0.3)
		print("=> After you have started your shift, all you need to do is to input the items and quantity in the customer's cart into the cashier computer. For example: \n"),sleep(0.3)
		print("CUSTOMER'S CART:"),sleep(0.3)
		print("OLIVE OIL 9.95\nOLIVE OIL 9.95\nRICE 15.46\nRICE 15.46\nRICE 15.46\n"),sleep(0.3)
		print("=> That means the customer has 2 OLIVE OIL and 3 RICE in their cart. Don't worry, our state-of-the-art cashier computer will make it easy for you."),sleep(0.3)
		print("=> Then once you're done inputting everything into the computer and calculating the total, the customer will pay the total in cash and you have to return the correct change."),sleep(0.3)
		print("=> For example, if the total is $12.50 and the customer pays $15, that means you have to return two 1 dollar bills and one 50 cent coin"),sleep(0.3)
		print("=> You are not allowed to make 3 mistakes per shift, or you're fired"),sleep(0.3)
		print("=> You'll also get fired if the minimarket's money reaches below 0")
		print("=> The more you play, you will be able to unlock new products and have bigger capacity to restock more items"),sleep(0.3)
		print("=> if the minimarket does not have enough items to sell, you're fired!"), sleep(0.03)
		print(f"=> And of course, you are allowed to quit anytime, {self.player.name}, by simply picking 'resign' in the menu")
		sleep(2.5)
		print("=> I think that's it for the tutorial, good luck.")
		input("\n(press ENTER to continue...)")

	# main menu
	def mainMenu(self):
		system('cls')
		display = [
				"  ________",
				" /        \\_____         __________",
				"/__________\\____|       |          |",
				"|    |  |  |            |  |  |    |",
				"|          |            |          |",
				"|    \\__/  |            |  \\__/    |",
				"|__________|            |__________|",
				"|        __|___         |          |",
				"|       |______|     ___|_____     |",
				"|    ______| |__   __||_____||__   |",
				"|    |          |  \\_|_|_|_|_|_/   |",
				"|___ |__________|___\\|_|_|_|_|/    |",
				"|                             |    |"
		]
		TopFrame = [
			" ",
			"MINIMARKET SIMULATOR",
			"*"*20,
			"created by cool",
			" "
		]
		BottomFrame = [
			" ",
			" ",
			"PRESS 'P' TO PLAY",
			"PRESS 'Q' TO QUIT",
			" "
		]
		print("="*75),sleep(0.03)
		for i in TopFrame: PRINT73().value(i)
		for d in display: print("|{:^18}{:<36}{:^19}|".format(" ",d," ")),sleep(0.03)
		print("|{:^5}{:^62}{:^6}|".format(" ","-"*52," ")),sleep(0.03)
		for i in BottomFrame: PRINT73().value(i)
		print("="*75)
		# p to play, q to quit
		while True:
			try:
				interact = input("=> ").lower()
				if interact != 'p' and interact != 'q':
						raise ValueError
				break
			except ValueError:
				print("=> Press 'p' or 'q'")
		if interact == 'q': exit()
		self.gameplay()

	def introduction(self):
		# loading screen
		print("\n{:^74}".format("Loading..."))
		print("{:^22}".format(" "),end="")
		for _ in range(30): print("∎",end=""), sleep(0.02)
		print(), system('cls')
		# default products at the start of the game, 8 apples and 10 milk
		self.stock.generateProducts(0, 8)
		self.stock.generateProducts(1, 10)
		# player name
		self.player.name = EmployeeNameValidation().check()
		# show player tutorial yay or nay
		print(f"\n=> Would you like to read the tutorial, {self.player.name}? (Y/N)")
		while True:
			try:
				interact = input("=> ").lower()
				if interact not in ["y", "n"]: raise ValueError
				if interact == "y": self.tutorialExplanation()
				break
			except ValueError: print("=> Press 'y' or 'n'")

	# after player finishes a level
	def levelUp(self):
		system('cls')
		self.day += 1 # level + 1
		self.stock.expire() # every consumable product's expiry date -1
		if self.day in [2, 3, 5, 6, 7, 9]: # if player reaches a certain level, they unlock a new product
			self.stock.unlocked += 1
			self.stock.generateProducts(self.stock.unlocked - 1, randrange(6,9))
			print(f"\nNEW PRODUCT UNLOCKED < {self.stock.shelf[self.stock.unlocked-1][0].name} > ! CHECK YOUR STOCK"), sleep(0.3)
		self.customersPerShift += 2 if self.day % 2 == 0 else 0 # the amount of customers per level increments by 2 if the level is an even number
		self.stock.maxCapacity += 2 # the max capacity of each product is increased by 2
		self.minReward += 5 # minimum value for rewards increments by 5
		self.maxReward += 5 # maximum value for rewards increments by 5
		self.player.mistake = 0 # mistakes reset to 0 after every shift
		print(f"Product max capacity has increased by 2, you can now store up to {self.stock.maxCapacity} items per product"),sleep(0.3)
		print("Don't forget to restock your items before your next shift starts!"), sleep(1.5)
		input("\n(PRESS ENTER TO CONTINUE TO THE NEXT DAY...)")

	def checkStock(self):
		self.money = self.StockControl.displayStock(self.money)  # check stock, returns money. if money < 0 game over
		if self.money < 0: print("\nYou have wasted all of our money. You're fired >:("), self.stats(1)

	def startShift(self):
		generateCustomers = [Customer() for _ in range(self.customersPerShift)] # customers per shift
		idx = 1
		for customer in generateCustomers:
			if not customer.fillCart(self.stock): # if there are not enough items for customer to add in their cart, player gets fired
				sleep(0.4)
				print("Uh oh, it seems there are not enough products for the customers, you're fired >:("), self.stats(2)
			system('cls')
			print(f"Customer {idx} out of {self.customersPerShift}")
			print("\nScanning items",end=""), sleep(0.6)
			for _ in range(3): print(".",end=""), sleep(0.6)
			print()
			self.player.ProcessPayment(customer, self.stock) # triggers cashier game, returns the amount of mistake the players have
			if self.player.mistake == 3: print(f"=> Ah. You have made 3 mistakes. You're fired, {self.player.name}"), self.stats(3) # fired if mistake = 3, game stops
			idx += 1
			print()
		yay = randrange(self.minReward, self.maxReward) # reward randomized
		bon = 0
		system('cls')
		print("Great job! You have done well this shift, here's your reward"), sleep(0.3)
		print(f"Money Earned today: ${yay}"), sleep(0.3)
		if self.player.mistake == 0: # player gets additional money if they did not make any mistakes
			bon = randrange(20,81)
			print(f"Bonus (no mistakes during shift) : ${bon}"), sleep(0.3)
		self.money += yay + bon
		sleep(2.2)

	def gameplay(self):
		self.introduction()
		# MAIN LEVEL
		while True:
			system('cls')
			print(), sleep(0.3)
			print(f"DAY {self.day}")
			print("="*(4+len(str(self.day))))
			print("\n1. Check Minimarket's Stock"), sleep(0.3) # check stock before shift starts
			print("2. Start shift"), sleep(0.3) # begin serving customers
			print("3. Resign"), sleep(0.3) # quit
			print("Pick an option (1/2/3).\n")
			try: # validasi
				interact = int(input("=> "))
				if not 1 <= interact <= 3: raise ValueError
			except ValueError:
				print("=> Press '1', '2', or '3'.")
			print()
			# check stock
			if interact == 1: self.checkStock()
			# shift starts and customers come in
			elif interact == 2: self.startShift(), self.levelUp()
			# player quits
			elif interact == 3: print(f"Aw, well it was nice meeting you, {self.player.name}. Don't come back."), self.stats(4)

	# shows stats of player's progress and the reason why the game is over
	def stats(self, reason):
		system('cls')
		status = "Resigned" if reason == 4 else "FIRED"
		comment = ["Caused the minimarket bankruptcy", "Was too lazy to restock the minimarket", "Bad customer service", "Probably got bored on the job"]
		print("\nGAME OVER")
		print("="*9)
		print("\nDays Played\t\t:",self.day)
		print("Employee Code\t\t:",self.player.code)
		print("Name\t\t\t:",self.player.name)
		print("Status\t\t\t:",status)
		print("Reason\t\t\t:",comment[reason - 1])
		print("\nTHANK YOU SO MUCH FOR PLAYING MINIMARKET SIMULATOR!\n")
		exit()
