import random  # Import the random module

# Generate a secret number
secret_number = random.randint(1, 10)

# Initialize guess counter
guess_count = 0
guessed_correctly = False

while not guessed_correctly:
    # Get user's guess
    guess = int(input("Enter your guess (1-10): "))
    guess_count += 1  # Increment guess counter

    # Match the guess using match-case and guards
    match guess:
        case _ if guess == secret_number:
            print("🎉 Congratulations, you guessed it!")
            guessed_correctly = True
        case _ if guess > secret_number:
            print("📈 Oops, your guess is a bit high. Try again!")
        case _ if guess < secret_number:
            print("📉 Nope, your guess is a bit low. Give it another shot!")
        case _:
            print("Something unexpected happened.")

# Display the number of guesses it took
print(f"You guessed the number in {guess_count} tries!")

# Offer to play again
play_again = input("Do you want to play again? (yes/no): ").strip().lower()
if play_again == "yes":
    print("Restart the program to play again!")  # Simple restart instruction
else:
    print("Thanks for playing!")

