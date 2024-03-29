# oop_minimarket_simulator

status: completed (100%)

## brief description

for our object oriented programming project, we have made a fun and simple minimarket simulator where the player can control stock items and process customer payment. In this game, the player can learn how to manage money and inventory, and try their best to be the best employee without getting fired. we have implemented inheritance, abstract classes, iterator patterns, various design patterns, and SOLID principles into our project.

## grading parameters

[x] inheritance\
[x] try and exception\
[x] iterator pattern\
[x] design pattern\
[x] testing\
[x] SOLID

## features / how it works

### main features

- products can expire over time, and have a 1 in 9 chance to be in bad condition when added
- cashier system and receipts
- the player can take out or put back money into cash register
- player stats when the game ends 

### start of the game

- the game opens with a simple framed illustration of a cashier and a customer, the player presses 'p' to play or 'q' to end the program
- the game asks for the player's name, then validates whether it contains numbers/symbols/spaces or not
- the player can read a brief explanation of the tutorial before starting the game

### main game

- before a level (shift) starts, the player is given 3 options: to check the minimarket's stock/inventory, to start the level, or to resign (quit)
- if the player chooses to check stock, the program will show them a brief overview of the products they currently have, and they can either pick '0' to return to the previous menu or pick the row number of a product that they want to check to see each item of that product
  - once they have picked a row number, the program will show the player all the items of that product, ranging from their code, name, expiry date, and condition. here, the player can add more items into the stock or discard products that are in bad condition or expired
  - the game will end if the player runs out of money
  - the game will end if there are not enough products for customers during the level
- if the player decides to start a level, certain amount of customers will come and fill their shopping cart, and then begin the payment process with the player
  - the player will see the contents of the customer's shopping cart, then input the product and quantity into the cashier computer
  - a receipt will show all the products that the customer has bought and the total cost
  - the customer will pay in a certain amount of cash, if it's more than the total cost, the player has to give back the correct change to the customer
  - the game will end if the player makes 3 mistakes during the level
- the game ends if the player chooses to resign
- the player can see their stats once the game is over, they can see how many days they have played, and the reason the game ended
