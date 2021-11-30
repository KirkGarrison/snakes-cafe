menuHeader = '''**************************************
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

menu = {
  'Appetizers': {'wings': 0, 'cookies': 0, 'spring Rolls': 0},
  'Entrees': {'salmon': 0, 'steak': 0, 'meat tornado': 0, 'a literal garden': 0},
  'Desserts': {'ice Cream': 0, 'cake': 0, 'pie': 0},
  'Drinks': {'coffee': 0, 'tea': 0, 'unicorn tears': 0}
}

for obj in menu:
    print(obj, ' ')
    for item in menu[obj]:
        print(item)
    print (' ')

print(menuHeader)

order_promt = '''***********************************
** What would you like to order? **
***********************************'''
print(order_promt)

customer_order = input('> ').lower()

while customer_order != "quit":
    for key in menu.keys():
        if customer_order in menu[key].keys():
            menu[key][customer_order]+= 1
            if menu[key][customer_order] == 1:
                print(f'** {menu[key][customer_order]} order of {customer_order} has been added to your meal **')
                break
            else:
                print(f'** {menu[key][customer_order]} orders of {customer_order} have been added to your meal **')
                break
    else:
        print('Item not on the Menu. Please try again')
    customer_order = input().lower()

