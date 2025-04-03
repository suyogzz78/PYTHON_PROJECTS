import random
from words import words
import string
from hangman_visual import lives_visual_dict


def valid_user_input(words):
    word = random.choice(words)
    while ' ' in word or '_' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = valid_user_input(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)  # It is used to display all the letters in the alphabet in uppercase
    used_letters = set()  # letters that the user has guessed

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives left and you have used these letters:", " ".join(used_letters))
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print(lives_visual_dict[lives])
        print("Current word:", " ".join(word_list))
        print("")

        # User input
        user_input = input("Guess a letter: ").upper()
        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)  # Remove the guessed letter
                print("")  # Print a blank line for readability
            else:
                lives -= 1  # Decrease lives for incorrect guess
                print("Your letter", user_input, "is not in the word.")
        elif user_input in used_letters:
            print("You have already guessed the letter", user_input)
        else:
            print("Invalid character")

    # End of game
    if lives == 0:
        print(lives_visual_dict[lives])
        print("You died, sorry. The word was", word)
    else:  # This only triggers when len(word_letters) == 0
        print("YAY! You guessed the word", word, "!!")


if __name__ == "__main__":
     hangman()
