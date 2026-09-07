
# display number 1 - 10
# for number in range(1, 11):
#     print(number)

# display even numbers
# for number in range(1, 22):
#     if number % 2 == 0:
#         print(number)


# multiplication table
# number = int(input('number: '))
# count = 0
# for numbers in range(10):
#     count += 1
#     numbers = number*count
#     print(f'{number} x {count} = {numbers}')


# count down

# for number in range(11, 1, -1):
#     number -= 1
#     print(number)


# print('Blast OFF')


# secret_num = 6
# num = int(input('Guess the number: '))
# while num != 6:
#     print('try again')
#     guess = int(input('Guess again: '))

#     if guess == secret_num:
#         print('Correct! you guessed the secret number')
#         break


rows = 5

for i in range(rows):
    spaces = " " * (rows - i - 1)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)
