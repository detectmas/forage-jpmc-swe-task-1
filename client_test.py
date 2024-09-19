import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # First quote(ABC)
    stock_abc, bid_price_abc, ask_price_abc, price_abc = getDataPoint(quotes[0])
    self.assertEqual(stock_abc,"ABC")
    self.assertEqual(bid_price_abc, 120.48)
    self.assertEqual(ask_price_abc, 121.2)
    # Check if the price of stock ABC is actually the average of the top bid and top ask as required
    self.assertEqual(price_abc, (120.48 + 121.2) / 2) 

    # Second quote(DEF)
    stock_def, bid_price_def, ask_price_def, price_def = getDataPoint(quotes[1])
    self.assertEqual(stock_def,"DEF")
    self.assertEqual(bid_price_def, 117.87)
    self.assertEqual(ask_price_def, 121.68)
    # Check if the price of stock DEF is actually the average of the top bid(DEF) and top ask(DEF) as required
    self.assertEqual(price_def, (117.87 + 121.68) / 2) 

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    """Ensures that the function getDataPoint behaves correctly in calculating the price even when the bid price is greater than the ask price"""
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # First quote (ABC): bid price greater than ask price
    stock_abc, bid_price_abc, ask_price_abc, price_abc = getDataPoint(quotes[0])
    self.assertEqual(stock_abc, 'ABC')
    self.assertEqual(bid_price_abc, 120.48)  
    self.assertEqual(ask_price_abc, 119.2)   
    self.assertEqual(price_abc, (120.48 + 119.2) / 2)   
    # Second quote (DEF): normal bid-ask scenario
    stock_def, bid_price_def, ask_price_def, price_def = getDataPoint(quotes[1])
    self.assertEqual(stock_def, 'DEF')
    self.assertEqual(bid_price_def, 117.87)  
    self.assertEqual(ask_price_def, 121.68)   
    self.assertEqual(price_def, (117.87 + 121.68) / 2)  

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
