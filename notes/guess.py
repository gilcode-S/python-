import random as ran

lowest = 1
highest = 100
guesses = 0
is_running = True

answer = ran.randint(lowest, highest)

print("PYTHON SIMPLE Guessing game")
print(f"select a number between {lowest} and {highest}")


while is_running:
    guess = input("enter your guess: ")

    # check if valid input
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest or guess > highest:
            print("that guess number is out of range")
            print(f"select a number between {lowest} and {highest}")
        elif guess < answer:
            print("too low try again")
        elif guess > answer:
            print("too high try again")
        else:
            print(f'correct! the answer was {answer}')
            print(f"Number of guess: {guess}")
            is_running = False
    else:
        print("Invalid guess")