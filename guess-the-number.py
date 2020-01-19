import random
number = random.randint(0, 21)
number_of_guesses = 0
guess = input('I am thinking of a number between 1 and 20. Guess what number I am thinking of: ')
while number_of_guesses < 6:
    number_of_guesses += 1
    if int(guess) == number:
        print('Your guess is correct.')
    else:
        if int(guess) > number:
            print('Your guess is greater than the number I am thinking of.')
        elif int(guess) < number:
            print('Your guess is less than the number I am thinking of.')
        guess = input('Guess again!')




