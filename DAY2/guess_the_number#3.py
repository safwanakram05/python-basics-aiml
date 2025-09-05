#Guess the number
print("There's a secret number between 1 to 50 hidden in this program, try guessing it!!!!")

secret_number = 17
guess = None
guess_count = 0

while guess != secret_number:
    guess = int(input())
    guess_count += 1
    if guess < secret_number:
        print('Too low')
    elif guess > secret_number:
        print('Too high')
    elif guess == secret_number:
        print('Yesss, its 17!!!')
print(f'You took {guess_count} tries to guess..')



