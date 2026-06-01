import random


def play_hangman():
    # 1. Predefined list of 5 words
    word_bank = ["python", "program", "laptop", "script", "coding"]

    # Randomly select a secret word from the list
    secret_word = random.choice(word_bank)

    # Track guessed letters using a set
    guessed_letters = set()

    # Track how many incorrect guesses are left
    turns_left = 6

    print("=========================================")
    print("       Welcome to Hangman Game!          ")
    print("=========================================")
    print("Rules: Guess the secret word one letter at a time.")
    print("You can afford 6 wrong guesses. Good luck!\n")

    # The main game loop
    while turns_left > 0:
        # Display the current state of the word (e.g., p _ t h _ _ )
        displayed_word = []
        for letter in secret_word:
            if letter in guessed_letters:
                displayed_word.append(letter)
            else:
                displayed_word.append("_")

        # Convert the list of characters back into a readable string
        current_progress = " ".join(displayed_word)
        print(f"Word to guess: {current_progress}")
        print(f"Incorrect guesses left: {turns_left}")
        print(
            f"Letters guessed so far: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}"
        )

        # Check if the player won (no more underscores left)
        if "_" not in displayed_word:
            print("\nCongratulations! You guessed the word correctly!")
            print(f"The word was: {secret_word.upper()}\n")
            return

        # Get the player's letter input
        guess = input("Guess a letter: ").strip().lower()

        # Input validation: ensure it's exactly 1 letter and from the alphabet
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please type a single alphabetical letter.\n")
            continue

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.\n")
            continue

        # Add the valid new guess to our tracking set
        guessed_letters.add(guess)

        # Check if the guess is right or wrong
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.\n")
        else:
            print(f"Oops! '{guess}' is not in the word.\n")
            turns_left -= 1

    # If the loop ends, it means turns_left reached 0 (Game Over)
    print("=========================================")
    print("GAME OVER! You ran out of turns.")
    print(f"The secret word was: {secret_word.upper()}")
    print("=========================================")


# Run the game
if __name__ == "__main__":
    play_hangman()
