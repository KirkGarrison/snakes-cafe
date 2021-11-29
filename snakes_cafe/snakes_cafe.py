menu = '''**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears'''

print(menu)

order_promt = '''***********************************
** What would you like to order? **
***********************************'''
print(order_promt)

customer_order = input('> ').lower()
# order_cart = ''
# item_quantity = 0

while customer_order != "quit":
    order_cart += customer_order
    print('** 1 order of ' + customer_order + ' have been added to your meal **')
    item_quantity += 1
    break
if customer_order == order_cart:
    print('** 2 orders of ' + customer_order + ' have been added to your meal **')
    item_quantity += 1
else:
    customer_order != order_cart
    print('** 1 order of ' + customer_order + ' have been added to your meal **')
    item_quantity += 1
    customer_order
    
print(str(item_quantity) + ' orders of ' + order_cart)





# customer_order2 = input('> ')
# if customer_order == customer_order2:
#     print('** 2 orders of ' + customer_order + ' have been added to your meal **')
#     item_quantity += 1
# else:
#     customer_order != customer_order2
#     print('** 1 order of ' + customer_order2 + ' have been added to your meal **')


# customer_order3 = input('> ')
# if customer_order == customer_order2 or customer_order3:
#     print('** 3 orders of ' + customer_order + ' have been added to your meal **')
#     item_quantity += 1
# else:
#     customer_order != customer_order2 or customer_order3
#     print('** 1 order of ' + customer_order3 + ' have been added to your meal **')

# if customer_order == customer_order2:
#     order_cart = customer_order
# else:
#     customer_order != customer_order2
#     order_cart += ' ' + customer_order2
# if customer_order == customer_order2 or customer_order3:
#     order_cart = ' ' + customer_order

    




# def custom_order():
#     customer_order = input('> ')
#     order_cart = 0
#     for order_cart in customer_order:
#         # print('** 1 order of ' + customer_order + ' have been added to your meal **')
#         order_cart += customer_order:
#         return order_cart
#         print('** 1 order of ' + order_cart + ' have been added to your meal **')
#     if customer_order == order_cart:
#         print('** 2 orders of ' + customer_order + ' have been added to your meal **')
    
# custom_order()
         
