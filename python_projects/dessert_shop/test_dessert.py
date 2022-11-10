from dessert import *
from packaging import Packaging
from payment import Payment, PayType

def test_DessertItem_Attribute():
  """Tests DessertItem Attributes"""
  #default value
  a = Candy()
  assert a.name == ""
  #non-default value
  b = Candy("Brownies")
  assert b.name == "Brownies"


def test_DessertItem_Modify():
  """Tests DessertItem Modifying"""
  #default value
  a = Candy()
  a.name = "Cookies"
  assert a.name == "Cookies"
  #non-default value
  b = Candy("Brownies")
  b.name = 'Cookies'
  assert b.name == 'Cookies'

def test_DessertItem_taxrate():
    """Tests DessertItem Tax Percent"""
    a = Candy()
    assert a.tax_percent == 7.25

def test_Candy_Attribute():
  """Tests Candy Attributes"""
  # default value
  a = Candy()
  assert a.name == ""
  assert a.candy_weight == 0.0
  assert a.price_per_pound == 0.0
  # non_default value
  a = Candy("Snickers", 2.5, 5.0)
  assert a.name == "Snickers"
  assert a.candy_weight == 2.5
  assert a.price_per_pound == 5.0


def test_Candy_Modify():
  """Tests Candy Modify"""
  #default value
  a = Candy()
  a.name = "Reeses"
  a.candy_weight = 1.5
  a.price_per_pound = 4.0
  assert a.name == 'Reeses'
  assert a.candy_weight == 1.5
  assert a.price_per_pound == 4.0
  #non-default value
  a = Candy("Snickers", 2.5, 5.5)
  a.name = "Reeses"
  a.candy_weight = 1.5
  a.price_per_pound = 4.0
  assert a.name == 'Reeses'
  assert a.candy_weight == 1.5
  assert a.price_per_pound == 4.0

def test_Candy_cost():
    """Tests Candy Order Cost"""
    order1 = Order()
    order1.add(Candy("Candy Corn", 1.5, .25))
    assert order1.order_cost() == 0.38
    order2 = Order()
    order2.add(Candy("Gummy Bears", .25, .35))
    assert order2.order_cost() == 0.09

def test_Candy_tax():
    """Tests Candy Tax"""
    dessert1 = Candy("Candy Corn", 1.5, .25)
    assert float(dessert1.calculate_tax()) == 0.03
    dessert2 = Candy("Gummy Bears", .25, .35)
    assert float(dessert2.calculate_tax()) == 0.01

def test_Candy_Packaging():
  """Tests Candy Packaging"""
  dessert1 = Candy("Candy Corn", 1.51, .25)
  assert dessert1.packaging == "Bag"

def test_Cookie_Attribute():
  """Tests Cookie Attributes"""
  #default value
  a = Cookie()
  assert a.name == ""
  assert a.cookie_quantity == 0
  assert a.price_per_dozen == 0.0
  #non-default value
  b = Cookie("Oreo", 24, 5.99)
  assert b.name == 'Oreo'
  assert b.cookie_quantity == 24
  assert b.price_per_dozen == 5.99

def test_Cookie_Modify():
  """Tests Cookie Modify"""
  #default value
  a = Cookie()
  a.name = "Lornadune"
  a.cookie_quantity = 12
  a.price_per_dozen = 4.5
  assert a.name == "Lornadune"
  assert a.cookie_quantity == 12
  assert a.price_per_dozen == 4.5
  #non_default value
  b = Cookie("Oreo", 24, 5.99)
  b.name = 'Lornadune'
  b.cookie_quantity = 12
  b.price_per_dozen = 4.5
  assert b.name == "Lornadune"
  assert b.cookie_quantity == 12
  assert b.price_per_dozen == 4.5

def test_Cookie_cost():
    """Tests Cookie Order Cost"""
    order1 = Order()
    order1.add(Cookie("Chocolate Chip", 6, 3.99))
    assert order1.order_cost() == 2.00

def test_Cookie_tax():
    """Tests Cookie Tax"""
    dessert1 = Cookie("Chocolate Chip", 6, 3.99)
    assert float(dessert1.calculate_tax()) == 0.14

def test_Cookie_Packaging():
    """Tests Cookie Packaging"""
    dessert1 = Cookie("Oreo", 12, 5.00)
    assert dessert1.packaging == "Box"

def test_IceCream_Attribute():
  """Tests IceCream Attributes"""
  #default value
  a = IceCream()
  assert a.name == ""
  assert a.scoop_count == 0
  assert a.price_per_scoop == 0.0
  #non-default value
  a = IceCream("Vanilla", 2, 2.5)
  assert a.name == "Vanilla"
  assert a.scoop_count == 2
  assert a.price_per_scoop == 2.5

def test_IceCream_Modify():
  """Tests IceCream Modify"""
  #default value
  a = IceCream()
  a.name = 'Vanilla'
  a.scoop_count = 2
  a.price_per_scoop = 2.5
  assert a.name == "Vanilla"
  assert a.scoop_count == 2
  assert a.price_per_scoop == 2.5
  #non-default value
  a = IceCream("Vanilla", 2, 2.5)
  a.name = 'Chocolate'
  a.scoop_count = 3
  a.price_per_scoop = 3.0
  assert a.name == "Chocolate"
  assert a.scoop_count == 3
  assert a.price_per_scoop == 3.0

def test_IceCream_cost():
    """Tests IceCream Order Cost"""
    order1 = Order()
    order1.add(IceCream("Pistachio", 2, .79))
    assert order1.order_cost() == 1.58

def test_IceCream_tax():
    """Tests IceCream Tax"""
    dessert1 = IceCream("Pistachio", 2, .79)
    assert float(dessert1.calculate_tax()) == 0.11

def test_IceCream_Packaging():
  """Tests IceCream Packaging"""
  dessert1 = IceCream("Vanilla", 2, .59)
  assert dessert1.packaging == "Bowl"

def test_Sundae_Attribute():
  """Tests Sundae Attributes"""
  #default value
  a = Sundae()
  assert a.name == ""
  assert a.scoop_count == 0
  assert a.price_per_scoop == 0.0
  assert a.topping_name == ""
  assert a.topping_price == 0.0
  #non-default value
  a = Sundae("Banana Split", 3, 1.99, "Whipped Cream", 0.59)
  assert a.name == "Banana Split"
  assert a.scoop_count == 3
  assert a.price_per_scoop == 1.99
  assert a.topping_name == "Whipped Cream"
  assert a.topping_price == 0.59

def test_Sundae_Modify():
  """Tests Sundae Modify"""
  #default value
  a = Sundae()
  a.name = "Banana Split"
  a.scoop_count = 3
  a.price_per_scoop = 1.99
  a.topping_name = "Whipped Cream"
  a.topping_price = 0.59
  assert a.name == "Banana Split"
  assert a.scoop_count == 3
  assert a.price_per_scoop == 1.99
  assert a.topping_name == "Whipped Cream"
  assert a.topping_price == 0.59
  #non-default value
  b = Sundae("Triple Gooberberry Sunrise", 4, 2.99, "nuts", 0.39)
  b.name = "Banana Split"
  b.scoop_count = 3
  b.price_per_scoop = 1.99
  b.topping_name = "Whipped Cream"
  b.topping_price = 0.59
  assert b.name == "Banana Split"
  assert b.scoop_count == 3
  assert b.price_per_scoop == 1.99
  assert b.topping_name == "Whipped Cream"
  assert b.topping_price == 0.59

def test_Sundae_cost():
    """Tests Sundae Order Cost"""
    order1 = Order()
    order1.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    assert order1.order_cost() == 3.36

def test_Sundae_tax():
    """Tests Sundae Tax"""
    dessert1 = Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)
    assert float(dessert1.calculate_tax()) == 0.24

def test_Sundae_Packaging():
  """Tests Sundae Packaging"""
  dessert1 = Sundae("Vanilla", 3, .59, "Hot Fudge", 1.29)
  assert dessert1.packaging == "Boat"

def test_interface_packaging():
  # default is Bag
  c = Candy("Candy Corn", 1.51, .25)
  assert c.packaging == "Bag"
  c.packaging = "Sack"
  assert c.packaging == "Sack"
  assert issubclass(Candy, Packaging)

def test_PayType():
  order1 = Order()
  #default is PayType.CASH
  assert order1.pay_method == PayType.CASH
  #alter to CARD
  order1.pay_method = PayType.CARD.name
  assert order1.pay_method == 'CARD'
  #alter to PHONE
  order1.pay_method = PayType.PHONE.name
  assert order1.pay_method == "PHONE"

def test_comparisons():
  candy1 = Candy("Candy Corn", 1.51, .25)
  candy2 = Candy("Gummy Bears", 1.51, .25)
  cookie1 = Cookie("Oreo", 25, 4.99)
  icecream1 = IceCream("Vanilla", 3, .69)
  sundae1 = Sundae("Vanilla Fudge", 3, .69, "Hot Fudge", 1.29)

  assert sundae1 > candy1
  assert candy1 < cookie1
  assert candy1 == candy2
  assert icecream1 <= sundae1
  assert candy1 >= candy2

def test_candy_Same_Item():
  candy1 = Candy("candy", 1, 1.5)
  candy2 = Candy("candy", 2, 1.5)
  cookie1 = Cookie("CC", 6, 3.99)
  assert candy1.is_same_as(candy2)

  bool = candy1.is_same_as(cookie1)
  assert bool is False

def test_cookie_Same_item():
  candy1 = Candy("candy", 1, 1.5)
  cookie2 = Cookie("CC", 2, 3.99)
  cookie1 = Cookie("CC", 6, 3.99)
  assert cookie1.is_same_as(cookie2) 

  bool = cookie1.is_same_as(candy1)
  assert bool is False

# 28 cases pass when running "pytest test_dessert.py -v" or "python -m pytest -v"