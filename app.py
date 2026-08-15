# whole numer
# import math
# student_count = 1000
# # decimals
# rating = 4.99
# # boolean
# is_active = True
# # string
# name = "Python Programming"

# print(student_count)


# # string
# course = "Python Programming"
# print(len(course))
# # specific char
# print(course[17])
# # start:end
# print(course[0:3])

# # scape sequence
# cours = "Python programming"
# print(course)

# first = "Gilbert"
# Last = "Engalan"
# # full = first + " " + Last

# # formated string
# full = f"{first} {Last}"
# print(full)


# print(cours.upper())
# print(cours.find("pro"))

# print(math.ceil(2.2))

# type conversion

# x = int(input('x : '))
# print(type(x))

# conditional statement

# temp = 10

# if temp > 30:
#     print('Its warm')
#     print('Drink water')
# elif temp < 20:
#     print("cold")
# print("Done")


# ternary operator

# age = 23
# message = "Eligible" if age >= 18 else "Not Eligible"

# print(message)


# loop if
# successful = True
# for number in range(3):
#     print('Attempt')
#     if successful:
#         print("success")
#         break
# else:
#     print('false')


# nested looop
# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")

# while loop
# number = 100

# while number > 0:
#     print(number)
#     number //= 2

# command = ''
# while command != "quit":
#     command = input('>')
#     print("ECHO", command)

# count = 0

# for number in range(2, 20, 2):
#     count += 1
#     print(number)

# print(f'we have {count} even numbers')


# 10.function
# def greet():
#     print('Hi there')
#     print('Welcome aboard')


# greet()


# 11 . arguments

# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome Abroad")

# greet("Gilbert", "Engalan")


# type of function
# return calculate value

# def get_greeting(name):
#     return f'hello {name}'


# message = get_greeting("gilbert")
# file = open("context.txt", 'w')
# file.write(message)


# argument keyword
# def increment(number, by):
#     return number+by


# print(increment(2, 1))


# default arguments

# def multiply(*numbers):
#     print(numbers)


# multiply(2, 3, 3, 3, 3, 3)


# collection
# set unorder {}
# list []
# tuple ()
# fruits = ('apple', 'orange', 'banana', 'coconut')
# # print(dir(fruits))
# # print(help(fruits))
# # print(len(fruits))

# # fruits.add('pineapple')
# # fruits.remove('apple')
# # fruits.pop()
# # fruits.clear()


# print(fruits)


# 2d list
# fruits = ['apple', 'orange', 'banana']
# vegetables = ['tomato', 'potato', 'onion']
# meats = ['chicken', 'pig', 'cow']

# groceries = [fruits, vegetables, meats]


# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()


import random as ran
capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Bejing",
            "Russia": "Moscow"}
# print(dir(capitals))
# print(help(capitals))


# print(capitals.get("Japan"))

# if capitals.get("Russia"):
#     print("that capital exists")
# else:
#     print("that capital doesn't exist")

# capitals.update({'Germany': 'Berlin'})

# print(capitals)
# keys method
# keys = capitals.keys()
# for key in capitals.keys():
#     print(key)

# values method
# values = capitals.values()
# for value in capitals.values():
#     print(value)

# items method
# items = capitals.items()
# for key, value in capitals.items():
#     print(f'{key} : {value}')


# example code how to generate random numbers
# random.shuffle() = []
# random.choice()
# random.random()
# low = 1
# high = 100

# number = ran.randint(low, high)
# print(number)


# default args fucntion exercise

# import time as t

# def count(end,start=0):
#     for x in range(start, end+1):
#         print(x)
#         t.sleep(1)
#     print('done')

# count(10,0)

# keyword args - preceded by identifier


# args and kwargs = keywords

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(1))


# kwargs

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")


# print(print_address(street="Sampaloc 1",
#                     city="Dasmarinas",
#                     province="Cavite",
#                     zip="4114"))


# iterables = return its element in loop

# number = [1, 2, 3, 4, 5]

# for num in reversed(number):
#     print(num, end="-")


# membership operators in python


# word = "APPLE"

# letter = input("Guess a letter in secret word: ").upper()

# if letter in word:
#     print(f"There is  a {letter}")
# else:
#     print(f"{letter} was not found")


# list comprehenstion

# doubles = [x * 2 for x in range(1, 11)]
# triples = [x * 3 for x in range(1, 11)]
# print(doubles)
# print(triples)


# grades = [61, 199, 99, 95, 19, 29]
# passing_grades = [grade for grade in grades if grade >= 60]
# failling_grades = [grade for grade in grades if grade < 60]

# print(passing_grades)
# print(failling_grades)


# match case statement

# def day_of_week(day):
#     match day:
#         case 1:
#             return "its monday"
#         case 2:
#             return 'its tuesday'
#         case 3:
#             return 'its wednesday'
#         case 4:
#             return 'its thrusday'
#         case 5:
#             return 'its friday'
#         case 6:
#             return 'its saturday'
#         case 7:
#             return 'its sunday'
#         case _:
#             return "invalid"


# print(day_of_week(1))


# print(help('modules'))
