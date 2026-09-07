import math
""" exercise: 1
radius = float(input("Enter radius: "))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
 """

""" exercise: 2
side_A = float(input("Enter side A: "))
side_B = float(input("Enter side B: "))

side_C = math.sqrt(side_A ** 2 + side_B ** 2)

print(f"Hypotenuse: {side_C}")
"""

""" exercise: 3
angle = float(input("Enter angle in degrees: "))
radians = math.radians(angle)
sin = math.sin(radians)
cos = math.cos(radians)
tan = math.tan(radians)

print(f"sin = {sin:.2f}")
print(f"cos = {cos:.2f}")
print(f"tan = {tan:.2f}")
"""
""" exercise: 4
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2-x1) ** 2 + (y2 - y1)**2)

print(f"Distance: {distance:.1f}") 
"""


print("=== Scientific Calculator ===")
print("1. Square Root")
print("2. Power")
print("3. Factorial")
print("4. Log Base 10")
print("5. Ceiling")
print("6. Floor")

choice = input("Choose an option (1-6): ")

if choice == "1":
    number = float(input("Enter a number: "))
    if number >= 0:
        print(f"Square Root = {math.sqrt(number)}")
    else:
        print("Cannot calculate the square root of a negative number.")

elif choice == "2":
    base = float(input("Enter the base: "))
    exponent = float(input("Enter the exponent: "))
    print(f"Result = {math.pow(base, exponent)}")

elif choice == "3":
    number = int(input("Enter a whole number: "))
    if number >= 0:
        print(f"Factorial = {math.factorial(number)}")
    else:
        print("Factorial is only defined for non-negative integers.")

elif choice == "4":
    number = float(input("Enter a positive number: "))
    if number > 0:
        print(f"Log Base 10 = {math.log10(number)}")
    else:
        print("Logarithm is only defined for numbers greater than 0.")

elif choice == "5":
    number = float(input("Enter a decimal number: "))
    print(f"Ceiling = {math.ceil(number)}")

elif choice == "6":
    number = float(input("Enter a decimal number: "))
    print(f"Floor = {math.floor(number)}")

else:
    print("Invalid choice.")
