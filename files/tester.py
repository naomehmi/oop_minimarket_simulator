import unittest
from people import Customer
from productsAndStock import Stock

class Testing(unittest.TestCase):
  def sampleStock(self):
    s = Stock()
    s.generateProducts(0, 8)
    s.generateProducts(1, 10)
    s.generateProducts(2,7)
    return s
  
  def testQuantity(self):
    """checking whether the quantity of the generated product is correct"""
    self.sampleStock().generateProducts(5, 6)
    self.assertEqual(len(self.s.shelf[5]),6)

  def testCondition(self):
    """checking whether every product in customer's cart is in 'GOOD' condition"""
    c = Customer()
    c.fillCart(self.sampleStock())
    for i in c.cart:
      with self.subTest("Condition",i=i):
        self.assertEqual(i.condition,"GOOD")
