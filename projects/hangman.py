# hangman
import random as ran

words = ('apple', 'orange', 'banana', 'coconut', 'pineapple')

# asc art
# dic of key: () -> tumple
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" 0 ",
                   "   ",
                   "   "),

               2: (" 0 ",
                   " | ",
                   "   "),
               3: (" 0 ",
                   "/| ",
                   "   "),
               4: (" 0 ",
                   "/|\\",
                   "   "),
               5: (" 0 ",
                   "/|\\",
                   "/  "),
               6: (" 0 ",
                   "/|\\",
                   "/ \\"), }


# loop

def display_man(wrong_guesses):
    # loop to display the exact wrong choice
    for line in hangman_art[wrong_guesses]:
        print(line)


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))


def main():
    answer = ran.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    # while loop
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)

        guess = input("Enter a letter: ").lower()

        #input validation
        if len(guess) != 1 or not guess.isalpha():
            print('Invalid input')
            continue

        #display set letters
        if guess in guessed_letters:
            print(f"{guess} is already guessed!")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            # loop will interate once for each char in the answer
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN")
            is_running = False


if __name__ == "__main__":
    main()
