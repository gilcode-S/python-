
menu = {"pizza": 3.00,
        'nachos': 2.00,
        'popcorn': 3.00,
        'fries': 2.00,
        'chips': 1.00,
        'pretzel': 2.00,
        'soda': 3.00,
        'lemonade': 2.00}

cart = []
total = 0


print("--------------MENU---------------")
for key, value in menu.items():
    print(f'{key:10} : ${value:.2f}')
print("---------------------------------")


while True:
    food = input("select an item (q to quit): ").lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("--------------YOUR ORDER---------------")
for food in cart:
    total = total + menu.get(food)
    print(food, end=' ')


print()
print(f'Total is : ${total:.2f}')
