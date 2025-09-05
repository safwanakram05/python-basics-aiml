numbers = input('Enter a list of numbers, comma separated\n')

numbers_list = [int(num.strip()) for num in numbers.split(",")]
for num in numbers_list:
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')