import random

while True:
    print("I am thinking of a number between 1 and 20. Guess what number I am thinking of")
    number = random.randint(1, 20)

    chances = 6

    while chances >0:

        guess = int(input())

        if guess == number:

            print("Congratulation YOU WON!!!")
            break

        elif guess < number:
            print("Your guess was too low: Guess a number higher than", guess)

        else:
            print("Your guess was too high: Guess a number lower than", guess)
        chances -= 1

        print("Chances Left: ",chances)

    if not chances < 10:
        print("YOU LOSE!!! The number is", number)

    ans = input("Do you want to play again (y/n) : ")

    if ans != 'y':
        break

print("\n      T H A N K S     F O R     P L A Y I N G     ! ! ! ! !\n")
