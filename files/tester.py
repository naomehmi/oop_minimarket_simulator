import unittest
from people import Customer
from productsAndStock import Stock

class checkProductCondition(unittest.TestCase):
  def testing(self):
    """checking whether every product in customer's cart is in GOOD condition"""
    c = Customer()
    s = Stock()
    s.generateProducts(0, 8)
    s.generateProducts(1, 10)
    c.fillCart(s)
    for i in c.cart:
      with self.subTest("Condition",i=i):
        self.assertEqual(i.condition,"GOOD")
