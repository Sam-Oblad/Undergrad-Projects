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


