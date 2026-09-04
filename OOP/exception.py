

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("you cant divide by zero")
except ValueError:
    print('Enter only number pls')
except Exception:
    print("something went wrong")
finally:
    print('Do some clean up here')