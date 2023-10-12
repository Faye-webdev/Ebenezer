import random

def get_user_choice():
    while True:
        user_choice = input('Enter your choice: ').capitalize()
        if user_choice in ['Rock', 'Paper', 'Scissors']:
            return user_choice
        else:
            print('Enter a valid choice.')

def get_computer_choice():
    computer_choice = ['Rock', 'Paper', 'Scissors']
    return random.choice(computer_choice)

def determine_winner(user_choice, computer_choice, wins, losses):
    if user_choice == computer_choice:
        print("It's a tie")
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
         print('You win!')
         wins += 1
    else:
        print('Computer wins!')
        losses += 1
    return wins, losses

def play_game():

    wins = 0
    losses = 0
    print('Welcome to the game!')
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f'Your choice: {user_choice}')
        print(f"Computer's choice: {computer_choice}")

        wins, losses = determine_winner(user_choice, computer_choice, wins, losses)

        print(f"Wins: {wins}, Losses: {losses}")

        play_again = input('Do you want to play again? (yes/no): ').lower()
        if play_again != 'yes':
             break

play_game()


    


