red_fruits = ['🍉', '🍓']
green_fruits = ['🥝', '🍐']
orange_fruits = ['🍊', '🍑']

red_fruits.append(green_fruits)
print("append() method:", red_fruits)

orange_fruits.extend(green_fruits)
print("extend() method:", orange_fruits)