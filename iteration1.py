#iteration1
import random

options = ["rock", "paper", "scissors"]
computer_option = random.choice(options)

user_option = input("Enter your choice (rock, paper, scissors): ").lower()

print("You chose:", user_option)
print("Computer chose:", computer_option)

if user_option == computer_option:
    print("It's a tie!")
elif (user_option == "rock" and computer_option == "scissors") or \
        (user_option == "paper" and computer_option == "rock") or \
        (user_option == "scissors" and computer_option == "paper"):
    print("You win!")
else:
    print("You lose!")
