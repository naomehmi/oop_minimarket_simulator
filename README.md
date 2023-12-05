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

## some code explanation

- we added an abstract class `Product` to act as a template for our `Consumable` and `nonConsumable` classes
- `Consumable` class is used to create instances of products that can be consumed aka they have expiry dates
- `nonConsumable` class is used to create instances of products that cannot be consumed aka they don't have expiry dates
- `Stock` class is used to manage all products in the minimarket, it implements the _Observer_ design pattern, where the object that we're observing are both the consumable and non consumable products
(readme not done yet)
