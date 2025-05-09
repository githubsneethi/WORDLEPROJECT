import random

with open("wordle.txt", "r") as file:
    words = [line.strip().lower() for line in file if line.strip()]

WORD = random.choice(words)
WORD_LENGTH = 5

GREEN_BG = "\033[42m"
YELLOW_BG = "\033[43m"
GRAY_FG = "\033[90m"
RESET = "\033[0m"

for guess_num in range(1, 7):
    guess = input(f"\nGuess {guess_num}: ").lower()
    if len(guess) != WORD_LENGTH:
        print(f"Please enter a {WORD_LENGTH}-letter word.")
        continue

    if guess == WORD:
        print(f"{GREEN_BG}{guess.upper()}{RESET}  Correct Answer.")
        break

    feedback = [""] * WORD_LENGTH
    word_chars = list(WORD)
    guess_chars = list(guess)

    for i in range(WORD_LENGTH):
        if guess_chars[i] == word_chars[i]:
            feedback[i] = f"{GREEN_BG}{guess_chars[i].upper()}{RESET}"
            word_chars[i] = None  

    for i in range(WORD_LENGTH):
        if feedback[i] == "":
            if guess_chars[i] in word_chars:
                feedback[i] = f"{YELLOW_BG}{guess_chars[i].upper()}{RESET}"
                word_chars[word_chars.index(guess_chars[i])] = None 
            else:
                feedback[i] = f"{GRAY_FG}{guess_chars[i].upper()}{RESET}"

    print("Feedback: ", " ".join(feedback))

else:
    print("Incorrect Guesses.")
print(f"The word was: {WORD.upper()}")
