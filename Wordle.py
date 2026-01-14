import random
import os
from colorama import Fore, Back, Style, init

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_dictionary(file_path):
    with open(file_path) as f:
        return [line.strip().lower() for line in f if line.strip()]

def is_valid_guess(guess, guesses):
    return guess in guesses

def evaluate_guess(guess, word):
    feedback = [""] * 5
    word_chars = list(word)
    guess_chars = list(guess)

    for i in range(5):
        if guess_chars[i] == word_chars[i]:
            feedback[i] = f"{Back.GREEN}{Fore.BLACK}{guess_chars[i].upper()}{Style.RESET_ALL}"
            word_chars[i] = None

    for i in range(5):
        if feedback[i] == "":
            if guess_chars[i] in word_chars:
                feedback[i] = f"{Back.YELLOW}{Fore.BLACK}{guess_chars[i].upper()}{Style.RESET_ALL}"
                word_chars[word_chars.index(guess_chars[i])] = None
            else:
                feedback[i] = f"{Fore.LIGHTBLACK_EX}{guess_chars[i].upper()}{Style.RESET_ALL}"

    return " ".join(feedback)

def wordle_game(guesses_list):
    secret_word = random.choice(guesses_list)
    max_attempts = 6

    for attempt in range(1, max_attempts + 1):
        guess = input(f"\nGuess {attempt}: ").lower()

        if len(guess) != 5:
            print(f"Please enter a 5-letter word.")
            continue

        if not is_valid_guess(guess, guesses_list):
            print("Invalid guess. Please enter a valid English word.")
            continue

        if guess == secret_word:
            clear_screen()
            print(f"{Back.GREEN}{Fore.BLACK}{guess.upper()}{Style.RESET_ALL} ✅ Correct Answer!")
            break

        feedback = evaluate_guess(guess, secret_word)
        print("Feedback:", feedback)

    else:
        clear_screen()
        print("❌ Incorrect Guesses.")
        print(f"The word was: {secret_word.upper()}")


clear_screen()
print("""Welcome to Wordle!
A player must guess a five-letter word related to academics within 6 attempts.
Green: indicates correct letters in the right position,
Yellow: signals correct letters in the wrong position,
Gray means the letter isn't in the word.
Strategize, refine guesses, and solve the puzzle!
""")

print("What kind of Wordle would you like?")
x = int(input("""1. College Wordle
2. 5-Letter Films
3. Book Wordle
4. Songs Wordle
5. Sports Wordle\n"""))

file_options = {
    1: "wordle.txt",
    2: "filmdle.txt",
    3: "bookdle.txt",
    4: "songdle.txt",
    5: "sportsdle.txt"
}

if x not in file_options:
    raise ValueError("Please input a valid integer from 1 to 5.")

words = load_dictionary(file_options[x])

clear_screen()
print(‘‘‘Color Code:
🟩 Green: correct letter, correct position
🟨 Yellow: correct letter, incorrect position
⬜ Gray: letter not in the word’’’)

wordle_game(words)
