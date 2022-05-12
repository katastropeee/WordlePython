import random
from typing import List
from logic import WordG
from colorama import Fore
from letter_state import LetterState


def main():
    word_set = load_word_set("words.txt")
    secret = random.choice(list(word_set))
    print(word_set)
    print(Fore.CYAN + "Welcome to Word Guesser, a clone of Wordle game built in Python Language" + Fore.RESET)
    wordie = WordG(secret)

    while wordie.can_attempt:
        x = input("\nType your guess: ")
        if len(x) != wordie.WORD_LENGTH:
            print(Fore.RED + f"Word must be {wordie.WORD_LENGTH} characters" + Fore.RESET)
            continue
        wordie.attempt(x)
        display_results(wordie)
    if wordie.is_solved:
        print(Fore.MAGENTA + "Congratulations! \n"
                             "You have solved the puzzle!" + Fore.RESET)
    else:
        print(Fore.MAGENTA + "You failed to solve the puzzle")
        print("The correct answer is " + secret)


def display_results(wordie: WordG):
    print("\nYour result so far ... ")
    print(f"You have {wordie.remaining_attempts} attempts remaining\n")

    lines = []
    for word in wordie.attempts:
        result = wordie.guess(word)
        colored_result_str = convert_result_to_color(result) + " "
        lines.append(colored_result_str)

    for _ in range(wordie.remaining_attempts):
        lines.append("_ " * wordie.WORD_LENGTH)

    border_box(lines)


def load_word_set(path: str):
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set


def convert_result_to_color(result: List[LetterState]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        colored_letter = color + letter.character + Fore.RESET

        result_with_color.append(colored_letter)
    return " ".join(result_with_color)


def border_box(lines: List[str], size: int = 9, pad: int = 1):
    content_length = size + pad * 2
    # top = "┌" + "─" * content_length + "┐"
    # bottom = "└" + "─" * content_length + "┘"
    # fancy border
    top = "╔" + "═" * content_length + "╗"
    bottom = "╚" + "═" * content_length + "╝"
    print(top)
    for line in lines:
        print("║ " + line + "║")
        # print("│ " + line + "│")
    print(bottom)


if __name__ == "__main__":
    main()
