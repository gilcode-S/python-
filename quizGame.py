questions = ('What is the capital of France?',
             'How many days are there in a week?',
             'What is 5 + 3?',
             'What color is the sky on a clear day?',
             'What do plants need to make their own food?')

options = (
    ("A. London", "B. Madrid", "C. Paris", "D. Rome"),
    ("A. 1", "B. 2", "C. 3", "D. 7"),
    ("A. 8", "B. 3", "C. 5", "D. 10"),
    ("A. Green", "B. Red", "C. Yellow", "D. Blue"),
    ("A. Milk", "B. Sunlight, water, and carbon dioxide", "C. Candy", "D. Oil")
)

answers = ('C', 'D', 'A', 'D', 'B')
guesses = []

score = 0
question_num = 0


for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
        print(f'{answers[question_num]} is the correct answer')
    question_num += 1


print("-------------------------")
print('        Result           ')
print("-------------------------")

print('answers: ', end=" ")
for answer in answers:
    print(answer, end=" ")

print()

print('guesses: ', end=" ")
for guess in guesses:
    print(guess, end=" ")

print()


score = int(score / len(questions) * 100)
print(f'your score is: {score}%')
