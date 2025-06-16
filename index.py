import random

def get_user_choice():
    print("\nChoose your option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:

        choice = input("Invalid input! Please enter rock, paper, or scissors: ").lower()
    return choice

def get_computer_choice():

    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):

    if user == computer:
        return "tie"

    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user, computer, result):

    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    if result == "tie":

        print("It's a tie!")
    elif result == "user":

        print("You win!")
    else:
        print("Computer wins!")

def play_game():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors Game!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1

        elif winner == "computer":
            computer_score += 1

        print(f"\n Score => You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':

            print("\nThanks for playing! Goodbye! ")
            break

# Run the game
play_game()
