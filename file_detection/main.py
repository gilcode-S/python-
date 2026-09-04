# py file detection

import os

# relative file path same path
# file_path = "test.txt"

# if os.path.exists(file_path):
#     print(f"The location '{file_path}' exist")
# else:
#     print("That location doesnt exist")


# absolute file path
file_path = "C:/Users/Gilbert/OneDrive/Desktop/test"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exist")

    if os.path.isfile(file_path):
        print('That is a file')
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location doesnt exist")
