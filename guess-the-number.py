import random
number = random.randint(0, 21)

guess = input('Guess what number I am thinking of: ')

if int(guess) == number:
    print('Your guess is correct.')
elif int(guess) > number:
    print('Your guess is greater than the number I am thinking of.')
else:
    print('Your guess is less than the number I am thinking of.')
