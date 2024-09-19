import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    """Ensures that the function getDataPoint behaves correctly in calculating the price even when the bid price is greater than the ask price"""
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_PostiveVals(self):
    """where both prices are non-zero and positive"""
    self.assertEqual(getRatio(120.48, 119.2), 120.48 / 119.2)
    self.assertEqual(getRatio(150, 50), 150 / 50)

  def test_getRatio_priceBIsZero(self):
    """where price a is positve non-zero and price b is zero. Expect "None" value return"""
    self.assertIsNone(getRatio(120.48, 0))

  def test_getRatio_priceAIsZero(self):
    """where price_a is zero and price_b is positive non-zero"""
    self.assertEqual(getRatio(0, 119.2),0)

  def test_getRatio_equalPrices(self):
    """Where  both a and b prices are equal. Expect 1"""
    self.assertEqual(getRatio(120.2,120.2),1)

  # Maybe negative prices...


if __name__ == '__main__':
    unittest.main()
