# oop_minimarket_simulator

status: in progress

## brief description

for our object oriented programming project, we have made a fun and simple minimarket simulator where the player can control stock items and process customer payment. In this game, player can learn how to manage money and inventory, and try their best to be the best employee without getting fired. we have implemented inheritance, abstract classes, iterator patterns, and various design patterns in our project.

## grading parameters

[x] inheritance\
[x] try and exception\
[x] iterator pattern\
[x] design pattern\
[ ] testing\
[ ] solid

## features / how it works

### main features

- products can expire over time, and have a 1 in 9 chance to be in bad condition when added
- cashier system and receipts
- the player can take out or put back money into the cash register
- stats when the game ends 

### start of the game

- the game opens with a simple framed illustration of a cashier and a customer, the player presses 'p' to play or 'q' to end the program
- the game asks for the player's name, then validates whether it contains numbers/symbols/spaces or not
- the player can read a brief explanation of the tutorial before starting the game

### main game

- before a level (shift) starts, the player is given 3 options: check minimarket stock/inventory, start the level, or resign (quit)
- if the player picks checking stock, the program will show them a brief overview of the products they currently have, and they can either pick '0' to return to the previous menu or pick the row number of a product that they want to check to see each items of that product
  - once they have picked a row number, the program will show the player all the items of that product, ranging from their code, name, expiry date, and condition. here, the player can add more items into the stock or discard products that are in bad condition or expired
  - the game will end if the player runs out of money
  - the game will end if there are not enough products for customers during the level
- if the player decide to start a level, certain amount of customers will come and fill their shopping cart, and then begin the payment process with the player
  - the player will see the contents of the customer's shopping cart, then input the product and quantity into the cashier computer
  - a receipt will show all the products that the customer has bought and the total cost
  - the customer will pay in a certain amount of cash, if it's more than the total cost, the player has to give back the correct change to the customer
  - the game will end if the player makes 3 mistakes during the level
- the game ends if the player chooses to resign
- the player can see their stats once the game is over, they can see how many days they have played, and the reason the game ended

## some code explanation

- we added an abstract class `Product` to act as a template for our `Consumable` and `nonConsumable` classes
  - attributes
    - code => contains two letters + 4 randomly generated numbers 
    - name
    - price
    - uom => unit of measurement
    - condition => has a 1 in 9 chance to be _BAD_, other than that _GOOD_
- `Consumable` class is used to create instances of products that have expiry dates
  - attributes are inherited from `Product`, and has a new attribute called _expDate_
- `nonConsumable` class is used to create instances of products that don't have expiry dates
  - attributes are inherited from `Product`
- `Stock` class is used to manage all products in the minimarket, it implements the _Observer_ design pattern, where the object that we're observing are both the consumable and non consumable products
  - attributes
    - **_listOfProducts** => a protected attribute that acts as a 'shelf' to store all products, is a 2 dimensional list, where each sublist contains items of each product
    -  **maxCapacity** => max capacity of every product, so players can't buy too much items at a time
    -  **unlocked** => the available number of products that the player currently have
    -  **_allProducts** => a protected attribute that contains every type of product that the minimarket sells, is a 2 dimensional list containing dictionaries, which each key represents:
        - con => 1 if it's a consumable product, 0 if it's non consumable
        - code => the two letter code for each product
        - name
        - price
        - uom
        - expDate (for consumable products)
        - cost => the cost to stock an individual item of a product
  - property functions
    - **shelf()** => to call _listOfProducts outside of the class
    - **products()** => to call _allProducts outside of the class
  - methods
    - `generateProducts(idx, qty)`
      - to add items of a product into _listOfProducts
      - how it works
        1. first we copy the dictionary of the product details and store it into a variable called _tmp_
        2. _conOrNon_ is a variable that stores the value of the 'con' key from _tmp_ dictionary
        3. then remove the 'con' and 'cost' keys from _tmp_
        4. then with a for loop, we append new `Consumable` or `nonConsumable` instances using tmp as **kwargs into _listOfProducts
    - `removeProducts(idx, row)`
      - to remove 1 item of a product
      - how it works
        1. pop the _row_-th index of _listOfProducts[_idx_]
    - `expire()`
      - to decrease the expiration date of every consumable object (observer design pattern to change the state of other objects)
      - how it works:
        1. iterate throught _listOfProducts
        2. 
\(readme not done yet)
