import random

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    global user_score, computer_score
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)
    
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

def main():
    print("Welcome to Rock-Paper-Scissors Game!")
    rounds = int(input("How many rounds would you like to play? "))
    
    for _ in range(rounds):
        play_game()
        print(f"Your score: {user_score}, Computer's score: {computer_score}")
        
    print("\nGame over!")
    if user_score > computer_score:
        print("Congratulations, you won!")
    elif user_score < computer_score:
        print("Computer wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
