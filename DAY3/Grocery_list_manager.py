grocery_list = []

while True:
    item = input('Enter grocery items and when done, type done, then enter..\n')
    if item == 'done':
        break
    grocery_list.append(item)

print("Here is your final grocery list...")
for item in grocery_list:
    print(item)
