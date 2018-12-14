from adventurelib import *

# inventory = Bag([Item('a rotten apple', 'an apple')])


# @when('eat ITEM')
# def eat(item):
#     obj = inventory.take(item)
#     if not obj:
#         print(f'You do not have a {item}.')
#     else:
#         print(f'You eat the {obj}.')

# @when('inventory')
# def show_inventory():
#     print('You have:')
#     if not inventory:
#         print('nothing')
#         return
#     for item in inventory:
#         print(f'* {item}')

Item.colour = 'grey'
inventory = Bag([Item('mug')])
mug = Item('mug')
mug.colour = 'red'

@when('look at ITEM')
def look(item):
    obj = inventory.find(item)
    if not item:
        print(f"You do not have a {item}.")
    else:
        print(f"It's a sort of {obj.colour}-ish colour.")

start()