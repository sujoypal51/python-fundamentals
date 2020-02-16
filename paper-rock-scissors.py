import random

choices = ['paper', 'rock', 'scissors']

computer_score = 0
player_score = 0

while computer_score < 2 and player_score < 2:
    computer_choice = random.choice(choices)
    player_choice = input('What do you choose: paper, rock, or scissors? ')
    if computer_choice == player_choice:
        print('Tie game! Try again!')
    elif computer_choice == 'paper' and player_choice == 'rock':
        print('The computer scores!')
        computer_score += 1
    elif computer_choice == 'rock' and player_choice == 'scissors':
        print('The computer scores!')
        computer_score +=1
    elif computer_choice == 'scissors' and player_choice == 'paper':
        print('The computer scores!')
        computer_score += 1
    elif player_choice == 'paper' and computer_choice == 'rock':
        print('You score!')
        player_score += 1
    elif player_choice == 'rock' and computer_choice == 'scissors':
        print('You score!')
        player_score += 1
    elif player_choice == 'scissors' and computer_choice == 'paper':
        print('You score!')
        player_score += 1

if computer_score == 2:
    print('The computer wins!')
elif player_score == 2:
    print('You win!')