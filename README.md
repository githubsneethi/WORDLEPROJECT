This Python project presents a terminal-based implementation of the popular Wordle game, focusing on modular design, string manipulation, and dynamic user interaction. The program employs various Python modules to provide core functionalities such as randomized word selection from a text file and input validation. The game randomly selects a five-letter target word and challenges the user to guess it within a limited number of attempts, offering color-coded feedback using ANSI escape codes on letter accuracy and position after each guess. The project closely resembles the original Wordle game while being lightweight and extensible.

The project demonstrates practical application of fundamental programming concepts such as control structures, loops, conditionals, string operations, exception handling, and modularization. The use of external modules like random for randomness, os for terminal control, and string for character operations enhances the clarity and maintainability of the codebase. The game flow ensures robustness by validating user input against a predefined word list and handling edge cases.

Key Features:
Randomized Word Selection: Uses the random module to choose a new target word from a predefined list, ensuring varied gameplay each time.

Terminal UI Handling: The os.system('cls' or 'clear') function is used to clear the console after each guess, offering a clean and readable interface. The importing of the OS module is a good example of using modules in the program.

Modular Structure: Organized into functions such as get_random_word(), validate_input(), check_guess(), and display_feedback() to improve readability and facilitate future updates.
 Inspired by the popular Wordle game, this version includes themed word categories such as College Wordle, Films, Books, Songs, and Sports, making it more diverse in topics as compared to the original Wordle game.
The game uses the following features:
Color-coded feedback using the colorama library:


🟩 Green for correct letters in the correct position.


🟨 Yellow for correct letters in the wrong position.


⬜ Gray for letters not in the word.


Robust input validation, ensuring guesses are exactly 5 letters and present in the word list.


A clean and interactive experience using screen clearing and structured feedback.


Modular code structure with functions for word loading, evaluation, validation, and gameplay logic.


By combining basic control structures, file handling, string manipulation, and user feedback, this game serves as an engaging application of fundamental Python programming concepts. Furthermore, it involves complex algorithms that select random words and ask the user to guess it, making it a fairly moderate-to-difficult word game unlike other word games.
