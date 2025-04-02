# creating a rock, paper, scissors game
# ask the user to make a choice between rock, paper, or scissors


import random

emojis = {
    "r": "✊",
    "p": "✋",
    "s": "✌️",
}  # dictionary to store the emojis for each option
options = ("r", "p", "s")  # using tuple to store the options


def user_choice():
    while True:
        user_input = input("Rock,Paper,Scissors? (r/p/s): ").lower()
        if user_input in options:
            return user_input
        else:
            print("invalid input, please try again")


def display_choices(user_input, computer_input):
    print(
        f"you chose {emojis[user_input]} and the computer chose {emojis[computer_input]}"
    )  # displaying the choices of the user and the computer


def determine_winner(user_input, computer_input):
    if user_input == computer_input:
        print("it's a tie")

    elif (
        (user_input == "r" and computer_input == "s")
        or (user_input == "p" and computer_input == "r")
        or (user_input == "s" and computer_input == "p")
    ):
        print("you win")

    else:
        print("you lose")


def play_game():

    while True:
        choice_of_user = user_choice()

        computer_input = random.choice(
            options
        )  # using random module to choose a random option for the computer

        display_choices(
            choice_of_user, computer_input
        )  # displaying the choices of the user and the computer

        determine_winner(
            choice_of_user, computer_input
        )  # determining the winner of the game

        play_again = input(
            "do you want to play again? (y/n): "
        ).lower()  # asking the user if he wants to play again

        if play_again == "n":
            print("thank you for playing")
            break


play_game()  # calling the function to play the game
