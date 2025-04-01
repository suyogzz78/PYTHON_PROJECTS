# Creating a number guessing name

import random  # Used to generate random numbers

# Generate a random number between 1 and 100
actual_number = random.randint(1, 100)

# Initialize the number of attempts
attempts = 0

print("Welcome to the Number Guessing Game!")
print("Try to guess the number between 1 and 100.")

while True:
    try:
  
        guess = int(input("Enter your guess: "))
        
        attempts += 1#counts the number of attempt user takes

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        if guess == actual_number:
            print(f"Congratulations! You guessed the number correctly in {attempts} attempts.")
            break
        elif guess > actual_number:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")
    except ValueError:
        # Handle the case where the user enters a non-integer value
        print("Invalid input. Please enter a valid integer.")