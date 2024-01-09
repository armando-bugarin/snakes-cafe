print('**************************************')
print('**    Welcome to the Snakes Cafe!   **')
print('**    Please see our menu below.    **')
print('**')
print('** To quit at any time, type "quit" **')
print('**************************************\n')

# Menu items
appetizers = ['Wings', 'Cookies', 'Spring Rolls']
entrees = ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden']
desserts = ['Ice Cream', 'Cake', 'Pie']
drinks = ['Coffee', 'Tea', 'Unicorn Tears']

# Create a dictionary to store the orders
orders = {}

# Print the menu
categories = {'Appetizers': appetizers, 'Entrees': entrees, 'Desserts': desserts, 'Drinks': drinks}
for category, items in categories.items():
    print(category)
    print('-------')
    for item in items:
        print(item)
    print()

print('***********************************')
print('** What would you like to order? **')
print('***********************************')

# Main loop to handle orders
while True:
    order = input('> ')
    
    # Check if the user wants to quit
    if order.lower() == 'quit':
        break
    
    # Check if the entered item is in the menu
    found = False
    for category, items in categories.items():
        if order in items:
            found = True
            break
    
    if found:
        # Add the order to the dictionary
        orders[order] = orders.get(order, 0) + 1
        print(f'** {orders[order]} order{"s" if orders[order] > 1 else ""} of {order} has been added to your meal **\n')
    else:
        print('** Sorry, the item is not on the menu. Please choose a valid item or type "quit" to exit. **\n')

print('Thanks for ordering from the Snakes Cafe!')
