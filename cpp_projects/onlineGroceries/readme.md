# Online Grocery OOP
## Write a program that does the following:
1. Read “customers.txt”. Put the customer records into a (global) vector.
2. Read “items.txt”. Put the item records into a vector.
3. Display a message stating how many customers there are, and how many items there are.
4. Prompt the user for a customer number. Search for the customer record.
- If the customer is not found, exit the program with an appropriate message.
- (You may assume that the user always enters a number.)
5. Prompt for the item number to purchase.
a. Display the item description and price.
b. Keep track a running totals of items bought, and amount spent.
c. If the item is not found, display an appropriate message and continue.
d. (You may assume that the user always enters a number.)
6. Continue asking for items until the user enters a 0 for the item number.
7. Display a message with the number of items purchases and the total cost.
- The total cost should be displayed as a typical money number with a $ sign and
dollars and cents. For example, if the total is $2.00, display it as $2.00. Not $2. This
means you will have to use a bit of output stream formatting.
### -------------------------------------------------------------------------
Orders.txt holds 2 lines per order. The first line contains the customer id, order number, order
date, and then a variable-length list of item_id–quantity pairs:
762212,1,2020-03-15,10951-3,64612-2,57544-1,80145-1,27515-2,16736-1,79758-2,29286-2,51822-3,39096-1,32641-3, ...
In the line above 3 items of product #10951 were ordered, 2 of product #64612, etc. Note that all
fields in all files are comma-separated, and that the item_id–quantity pairs in orders.txt are
separated by a dash.
The second line contains payment information in the form of payment code, and payment
information. There are 3 types of payments:
- 1 = credit card (card number and expiration date)
- 2 = PayPal (paypal_id only)
- 3 = wire transfer (bank_id and account_id)


Calculate the totals and output all customer data in this format:


### ===========================  
Order #1, Date: 2020-03-15  
Amount: $100.23, Paid by Credit card 373975319551257, exp. 12-2023  
Customer ID #762212:  
Yolanda McAlarney, ph. 505-136-7715, email: ymcalarney2u@wordpress.com  
705 Corscot Hill  
Albuquerque, NM 87190  
Order Detail:  
Item 10951: "Syrup - Monin Swiss Choclate", 3 @ 3.00  
Item 16736: "Wine - Red Cooking", 1 @ 2.00  
Item 16974: "Pastry - Lemon Danish - Mini", 3 @ 1.19  
Item 23022: "Beef - Short Ribs", 1 @ 5.00  
Item 26461: "Bread - Crumbs Bulk", 1 @ 3.00  
Item 26860: "Waffle Stix", 2 @ 2.99  
Item 27515: "Longos - Burritos", 2 @ 4.00  
Item 29286: "Lemonade - Strawberry 591 Ml", 2 @ 2.25  
Item 32641: "Pie Filling - Cherry", 3 @ 0.89  
Item 39096: "Oil - Peanut", 1 @ 0.95  
Item 51822: "Pasta - Rotini Colour Dry", 3 @ 1.19  
Item 57544: "Peach - Halves", 1 @ 0.79  
Item 63725: "Black Currants", 3 @ 0.79  
Item 64007: "Juice - Propel Sport", 2 @ 1.99  
Item 64612: "Pie Shells 10", 2 @ 7.00  
Item 75536: "Quail - Whole Boneless", 2 @ 8.79  
Item 79758: "Beef Flat Iron Steak", 2 @ 5.49  
Item 80145: "Bread - Country Roll", 1 @ 2.29  