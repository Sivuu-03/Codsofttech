import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_round():
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
    else:
        print("You lose!")
    return result

def play_game():
    user_score = 0
    computer_score = 0
    while True:
        result = play_round()
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            break
    print("Thank you for playing!")

# Start the game
play_game()
