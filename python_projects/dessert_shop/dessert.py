"""dessert.py"""
from abc import ABC, abstractmethod
from packaging import Packaging
from payment import PayType
from same_item import SameItem
import functools
from typing import *

nums = [] # assigns unique customer ID
i = 1000
for _ in range(999):
    nums.append(i)
    i +=1

@functools.total_ordering
class DessertItem(Packaging, ABC):
    """Dessert Super Class"""
    tax_percent = 7.25

    def __init__(self, name: str = ""):
        self.name = name

    @property
    def packaging(self):
        return self.__packaging

    @packaging.setter
    def packaging(self, val):
        self.__packaging = val

    @abstractmethod
    def calculate_cost(self):
        """superclass returns cost of item"""

    def calculate_tax(self):
        """returns actual tax of item"""
        tax = self.calculate_cost() * (DessertItem.tax_percent / 100)
        return "{:.2f}".format(tax)

    def _is_valid_operand(self, other):
        return (hasattr(self, "calculate_cost") and hasattr(other, "calculate_cost"))

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.calculate_cost() < other.calculate_cost()

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.calculate_cost() == other.calculate_cost()
    
    def is_same_as(self, other):
        pass


class Candy(DessertItem, SameItem):
    """Candy SubClass"""

    def __init__(self, name: str = "", candy_weight: float = 0.0, price_per_pound: float = 0.0, packaging="Bag"):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
        self.packaging = packaging

    def calculate_cost(self):
        return (self.candy_weight * self.price_per_pound)

    def __str__(self):
        cost = f"${'{:.2f}'.format((self.calculate_cost()))}"
        tax = f"[Tax: ${(self.calculate_tax())}]"
        return f"{self.name} ({self.packaging})\n     {self.candy_weight} lbs @ ${self.price_per_pound}/lb:" + "{0:>18} {1:>15}".format(cost, tax)

    def is_same_as(self, other:"Candy")->bool:
        return isinstance(other, Candy) and other.name == self.name and self.price_per_pound == other.price_per_pound


class Cookie(DessertItem, SameItem):
    """Cookie SubClass"""

    def __init__(self, name: str = "", cookie_quantity: int = 0, price_per_dozen: float = 0.0, packaging="Box"):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen
        self.packaging = packaging

    def calculate_cost(self):
        return ((self.cookie_quantity / 12) * self.price_per_dozen)

    def __str__(self):
        cost = f"${'{:.2f}'.format((self.calculate_cost()))}"
        tax = f"[Tax: ${(self.calculate_tax())}]"
        return f"{self.name} ({self.packaging})\n     {self.cookie_quantity} Cookie(s) @ ${self.price_per_dozen}/dozen:" + "{0:>12} {1:>15}".format(cost, tax)

    def is_same_as(self, other:"Cookie")->bool:
        return isinstance(other, Cookie) and other.name == self.name and self.price_per_dozen == other.price_per_dozen


class IceCream(DessertItem):
    """IceCream SubClass"""

    def __init__(self, name: str = "", scoop_count: int = 0, price_per_scoop: float = 0.0, packaging="Bowl"):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        self.packaging = packaging

    def calculate_cost(self):
        return (self.scoop_count * self.price_per_scoop)

    def __str__(self):
        cost = f"${'{:.2f}'.format((self.calculate_cost()))}"
        tax = f"[Tax: ${(self.calculate_tax())}]"
        return f"{self.name} ({self.packaging})\n     {self.scoop_count} Scoop(s) @ ${self.price_per_scoop}/scoop:" + "{0:>12} {1:>15}".format(cost, tax)


class Sundae(IceCream):
    """Sundae SubSubclass"""

    def __init__(self, name: str = "", scoop_count: int = 0, price_per_scoop: float = 0.0, topping_name: str = '', topping_price: float = 0.0, packaging="Boat"):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price
        self.packaging = packaging

    def calculate_cost(self):
        return ((self.scoop_count * self.price_per_scoop) + self.topping_price)

    def __str__(self):
        cost = f"${'{:.2f}'.format(self.calculate_cost())}"
        tax = f"[Tax: ${self.calculate_tax()}]"
        string = f"{self.name} ({self.packaging})\n     {self.scoop_count} Scoop(s) @ ${self.price_per_scoop}/scoop\n     {self.topping_name} topping @ ${self.topping_price}:" + \
            "{0:>12} {1:>15}".format(cost, tax)
        return string

class Order():
    """Order Class"""

    def __init__(self, pay_method=PayType.CASH):
        self.order = []  # attribute
        self.pay_method = pay_method  # attribute
    
    def sort(self):
        return self.order.sort()

    @property
    def pay_method(self):
        return self.__pay_type

    @pay_method.setter
    def pay_method(self, val):
        self.__pay_type = val

    def add(self, new_dessert_item):
        """adds a single dessertitem argument to the order list"""
        if isinstance(new_dessert_item, IceCream) or isinstance(new_dessert_item, Sundae):
            self.order.append(new_dessert_item)
        elif isinstance(new_dessert_item, Candy):
            flag = False
            for item in self.order:
                if (item.is_same_as(new_dessert_item)):
                    flag = True
                    item.candy_weight += new_dessert_item.candy_weight
                    break
            if not flag:
                self.order.append(new_dessert_item)
        elif isinstance(new_dessert_item, Cookie):
            flag = False
            for item in self.order:
                if (item.is_same_as(new_dessert_item)):
                    flag = True
                    item.cookie_quantity += new_dessert_item.cookie_quantity
                    break
            if not flag:
                self.order.append(new_dessert_item)

    def item_count(self):
        """prints how many items are in the order list"""
        num = len(self.order)
        return num

    def order_cost(self):
        """calculates subtotal for the order"""
        sub_total = 0
        for item in self.order:
            sub_total += (item.calculate_cost())
        return round(sub_total, 2)

    def order_tax(self):
        """calculates tax for the order"""
        tax_rate = DessertItem.tax_percent / 100
        total_tax = self.order_cost() * tax_rate
        return round(total_tax, 2)

    def get_order_list(self):
        order_list = []
        total = (f"${('{:.2f}'.format((self.order_cost() + self.order_tax())))}")
        subtotal = f"${self.order_cost()}"
        tax = f"[Tax: ${self.order_tax()}]"
        order_list.append("\n----------------------------Reciept---------------------------\n")
        for item in self.order:
            order_list.append((str(item)))
        order_list.append("\n--------------------------------------------------------------")
        order_list.append(
            f"Total number of items in order: {self.item_count()}\n")
        order_list.append(f"Subtotal: {subtotal:>33} {tax:>15}")
        order_list.append(f"Total: {total:>36}")
        order_list.append("--------------------------------------------------------------")
        order_list.append(f"Paid with {self.pay_method}")
        order_list.append("--------------------------------------------------------------")
        return order_list

    def __str__(self):
        string = "\n".join(self.get_order_list())
        return string

class Customer:
    def __init__(self, customer_name: str):
        self.customer_name = customer_name
        self.order_history: List[Order] = []
        self.customer_id: int = nums.pop(0)

    def add2history(self, order: Order)->object:
        self.order_history.append(order)
        return Customer
