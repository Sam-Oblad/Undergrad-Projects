from dessert import *

def test_customer():
    customer1 = Customer("Joe")
    assert customer1.customer_name == 'Joe'
    assert customer1.customer_id == 1000
    assert customer1.order_history == []


def test_cust_id():
    customer2 = Customer("Johnny")
    customer3 = Customer("Sam")
    customer4 = Customer("Bob")
    assert customer2.customer_id == 1001
    assert customer3.customer_id == 1002
    assert customer4.customer_id == 1003
    