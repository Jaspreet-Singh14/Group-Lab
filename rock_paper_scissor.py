mport random
# Define the options for the game
options = ["rock", "paper", "scissors"]

# Loop for continuous play
while True:
    # Get the computer's choice
    computerOption = random.choice(options)

    # Print the computer's choice
    print("Computer chose:", computerOption)

    # Get the user's choice
    userOption = input("Enter your choice (rock, paper, scissors): ").lower()

    # Print the user's choice
    print("You chose:", userOption)

    # Determine the winner
    if userOption == computerOption:
        print("It's a tie!")
    elif userOption == "rock":
        if computerOption == "paper":
print("Computer wins!")
        else:
            print("You win!")
    elif userOption == "paper":
        if computerOption == "scissors":
            print("Computer wins!")
        else:
            print("You win!")
    elif userOption == "scissors":
        if computerOption == "rock":
            print("Computer wins!")
        else:
            print("You win!")
    else:
        print("Invalid choice. Please choose rock, paper, or scissors.")

    # Ask the user if they want to play again
import random
# Define the options for the game
options = ["rock", "paper", "scissors"]
while True:
    # Get the computer's choice
    computerOption = random.choice(options)
import random
# Define the options for the game
options = ["rock", "paper", "scissors"]

# Loop for continuous play
while True:
    # Get the computer's choice
    computerOption = random.choice(options)

    # Print the computer's choice
    print("Computer chose:", computerOption)

    # Get the user's choice
    userOption = input("Enter your choice (rock, paper, scissors): ").lower()

    # Print the user's choice
    print("You chose:", userOption)
# Determine the winner
    if userOption == computerOption:
        print("It's a tie!")
    elif userOption == "rock":
        if computerOption == "paper":

    # Print the computer's choice
    print("Computer chose:", computerOption)

    # Get the user's choice
    userOption = input("Enter your choice (rock, paper, scissors): ").lower()

    # Print the user's choice
    print("You chose:", userOption)

    # Determine the winner
    if userOption == computerOption:
        print("It's a tie!")elif userOption == "rock":
        if computerOption == "paper":
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break


      

# Loop for continuous play

