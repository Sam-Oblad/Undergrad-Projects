"""dessert_shop.py"""
from dessert import Order, Candy, Cookie, IceCream, Sundae, Customer
from payment import PayType
from typing import Dict
from random import randint
import os
from time import sleep

clear = lambda: os.system('clear')
objs = [Order() for i in range(1000)]
customer_db: Dict[str,Customer] = {}
ORDER = objs.pop()

def reset_order():
    global ORDER
    ORDER = objs.pop()

def main_menu():
    clear()
    print("Welcome to the Dessert Shop!")
    print("------------------------------------------------\n")
    print(" 1: Candy \n 2: Cookie \n 3: Ice Cream \n 4: Sundae \n 5: Admin Module \n 6: Quit")
    inp = input("\nWhat would you like to add to the order? (1-6)\nPress enter for done:\n\n")
    if inp == "":
        user_prompt_payment()
    elif inp == '1':
        user_prompt_candy()
    elif inp == '2':
        user_prompt_cookie()
    elif inp == '3':
        user_prompt_icecream()
    elif inp == '4':
        user_prompt_sundae()
    elif inp == '5':
        admin_module()
    elif inp =='6':
        quit()
    else:
        print("\n------------------------------------------------")
        print("\nInvalid Input: Please enter 1-4 or enter if you're finished")
        print("\n------------------------------------------------\n")
        sleep(3)
        main_menu()

def user_prompt_candy():
    while True:
        try:
            candy_type = str(input("\nEnter the name of your candy: "))
        except ValueError:
            print("Please try entering the candy name again. . . \n")
            continue
        else:
            break
    while True:
        try:
            candy_weight = float(input("Enter the weight of the candy: "))
        except ValueError:
            print("Please try entering the weight again . . .\n")
            continue
        else:
            break
    while True:
        try:
            candy_price = float(input("Enter the price per pound: "))
        except ValueError:
            print("Please try entering the price again . . . \n")
            continue
        else:
            break
    ORDER.add(Candy(candy_type, candy_weight, candy_price))
    main_menu()

def user_prompt_cookie():
    while True:
        try:
            cookie_type = str(input("\nEnter the name of your cookie: "))
        except ValueError:
            print("Please try entering the cookie name again. . . \n")
            continue
        else:
            break
    while True:
        try:
            cookie_amount = int(input("Enter the number of cookies: "))
        except ValueError:
            print("Please try entering the amount again . . .\n")
            continue
        else:
            break
    while True:
        try:
            cookie_price = float(input("Enter the price per dozen: "))
        except ValueError:
            print("Please try entering the price again . . . \n")
            continue
        else:
            break
    ORDER.add(Cookie(cookie_type,cookie_amount, cookie_price))
    main_menu()

def user_prompt_icecream():
    while True:
        try:
            ice_cream_type = str(input("\nEnter the name of your ice cream: "))
        except ValueError:
            print("Please try entering the ice cream name again. . . \n")
            continue
        else:
            break
    while True:
        try:
            scoop_amount = int(input("Enter the number of scoops: "))
        except ValueError:
            print("Please try entering the amount again . . .\n")
            continue
        else:
            break
    while True:
        try:
            scoop_price = float(input("Enter the price per scoop: "))
        except ValueError:
            print("Please try entering the price again . . . \n")
            continue
        else:
            break
    ORDER.add(IceCream(ice_cream_type, scoop_amount, scoop_price))
    main_menu()

def user_prompt_sundae():
    while True:
        try:
            ice_cream_type = str(input("\nEnter the name of your ice cream: "))
        except ValueError:
            print("Please try entering the ice cream name again. . . \n")
            continue
        else:
            break
    while True:
        try:
            scoop_amount = int(input("Enter the number of scoops: "))
        except ValueError:
            print("Please try entering the amount again . . .\n")
            continue
        else:
            break
    while True:
        try:
            scoop_price = float(input("Enter the price per scoop: "))
        except ValueError:
            print("Please try entering the price again . . . \n")
            continue
        else:
            break
    while True:
        try:
            topping = str(input("Enter the name of your topping: "))
        except ValueError:
            print("Please try entering the price again . . . \n")
            continue
        else:
            break
    while True:
        try:
            topping_price = float(input("Enter the price for the topping: "))
        except ValueError:
            print("Please try entering the price again . . . \n")
            continue
        else:
            break
    ORDER.add(Sundae(ice_cream_type,scoop_amount, scoop_price, topping, topping_price))
    main_menu()

def user_prompt_payment():
        clear()
        user_input_name = input("Please enter your name: ")
        
        if user_input_name in customer_db:
            current_cust = customer_db[user_input_name]
            current_cust.add2history(ORDER)
        else:
            customer = Customer(user_input_name)
            customer.add2history(ORDER)
            customer_db[user_input_name] = customer
            
        clear()
        print("What form of payment would you like to select?")
        user_input_num = input(" 1. Cash\n 2. Card\n 3. Phone\n Enter payment method: ")
        if user_input_num == '1':
            ORDER.pay_method = PayType.CASH.name
        elif user_input_num == '2':
            ORDER.pay_method = PayType.CARD.name
        elif user_input_num == '3':
            ORDER.pay_method = PayType.PHONE.name
        else:
            print("====================================\n")
            print("Please enter 1, 2, or 3, respectively to conitnue\n")
            user_prompt_payment()
        ORDER.sort()
        clear()
        print(ORDER)
        print(f"Customer Name: {customer_db[user_input_name].customer_name}      Customer ID: {customer_db[user_input_name].customer_id}     Total Orders: {len(customer_db[user_input_name].order_history)}")
        new_order()

def new_order():
    user_input = input("\nWould you like to start another order?\n Return 'y' for yes . . .")
    if user_input == "y":
        reset_order()
        main_menu()
    else:
        clear()
        quit()

def admin_module():
    inp = input("""
ADMIN MODULE
1: Shop Customer List
2: Customer Order History
3: Best Customer
4: Exit Admin Module
What would you like to do? (1-4):
""")
    if inp == '1':
        clear()
        scl()
    elif inp == '2':
        coh()
    elif inp == '3':
        bc()
    elif inp == '4':
        main_menu()

def scl():
    for _ in range(len(customer_db)):
        names = [(keys) for keys in customer_db.keys()]
        objects = [(values) for values in customer_db.values()]
        customer_ids = []
        for c_object in objects:
            customer_ids.append(c_object.customer_id)
    data = list(zip(names, customer_ids))
    print("Customer Order History:")
    print("--------------------------------------------------------------")
    for name, id in data:
        print(f"Customer Name: {name}                  Customer ID: {id}")
    admin_module()

def coh():
    i = 1
    inp = input("Please enter the name of the customer: \n")
    if inp in customer_db:
        cust_object = customer_db[inp]
        cust_name = cust_object.customer_name
        cust_id = cust_object.customer_id
        customer_orders = []
        customer_orders.append(cust_object.order_history)
        clear()
        print(f"Customer Name: {cust_name}                         Customer ID: {cust_id}")
        print("--------------------------------------------------------------")
        for order in customer_orders:
            for _ in order:
                print(f"Order #: {i}{_}")
                i += 1
        sleep(2)
        admin_module()
    else: 
        print("Customer Does Not Exsist\nCurrent Customers On File:")
        sleep(2)
        scl()
    
def bc():
    num_of_orders = {}
    order_numbers = []
    cust_objects = [(values) for values in customer_db.values()]
    for cust_object in cust_objects:
        order_numbers.append(len(cust_object.order_history))
        num_of_orders[cust_object.customer_name] =  len(cust_object.order_history)
    highest_order = max(order_numbers)
    key_list = list(num_of_orders.keys())
    value_list = list(num_of_orders.values())
    ind = value_list.index(highest_order)
    print(f"{key_list[ind]} has the highest amount of orders at {highest_order}!")
    admin_module()


def main():
    """program starts here"""
    main_menu()
if __name__ == "__main__":
    main()
