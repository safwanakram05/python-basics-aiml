
unique_names = set()

print('Please enter names one at a time..')
print("Type 'done' when you are done")

while True:
    name = input("Enter a name: ")
    if name == 'done':
        break
    unique_names.add(name)


print("You entered the following names....")

for name in sorted(unique_names):
    print(name)




