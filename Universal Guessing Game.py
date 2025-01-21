import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))
    number_to_guess = random.randint(lower_bound, upper_bound)
    attempts = 0

    print(f"Guess the number between {lower_bound} and {upper_bound}.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

def word_guessing_game():
    print("Welcome to the Word Guessing Game!")
    word_list = ["python", "elephant", "galaxy", "mountain", "rainbow", "developer"]
    word_to_guess = random.choice(word_list).lower()
    attempts = 0

    print("Guess the word! Here are some hints:")
    print(f"The word has {len(word_to_guess)} letters.")

    guessed_word = ['_'] * len(word_to_guess)

    while True:
        print("Current word: ", " ".join(guessed_word))
        guess = input("Enter a letter or the full word: ").lower()
        attempts += 1

        if len(guess) == 1:
            if guess in word_to_guess:
                print("Good job! That letter is in the word.")
                for index, letter in enumerate(word_to_guess):
                    if letter == guess:
                        guessed_word[index] = guess
                if '_' not in guessed_word:
                    print(f"Congratulations! You guessed the word '{word_to_guess}' in {attempts} attempts.")
                    break
            else:
                print("Sorry, that letter is not in the word.")
        elif len(guess) == len(word_to_guess):
            if guess == word_to_guess:
                print(f"Congratulations! You guessed the word '{word_to_guess}' in {attempts} attempts.")
                break
            else:
                print("Sorry, that's not the correct word.")
        else:
            print("Invalid input. Please guess a single letter or the full word.")

def main():
    print("Welcome to the Universal Guessing Game!")
    while True:
        print("Choose a game mode:")
        print("1. Number Guessing Game")
        print("2. Word Guessing Game")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            number_guessing_game()
        elif choice == '2':
            word_guessing_game()
        elif choice == '3':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
