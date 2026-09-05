

# txt_data = "I like burger"

# file_path = "output.txt"

# #w = write
# #x = exists
# #a = appended to the file
# with open(file=file_path, mode="w") as file:
#     file.write(txt_data)
#     print(f"text file '{file_path}' was created")


# exmple for collection

# employees = ['Eugene', 'Squidward', 'Spongebob', 'Patrick']

# file_path = "output.txt"

# try:
#     with open(file=file_path, mode="w") as file:
#         # instead of file.write in collection it used loop for each
#         for employee in employees:
#             file.write("\n" + employee)
#         print(f"text file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")


# json type
# import json
# employee = {
#     "name": "Sponge Bob",
#     'age': 30,
#     'job': "cook"
# }

# file_path = "output.json"

# try:
#     with open(file_path, 'w') as file:
#         json.dump(employee, file, indent=4)
#         print(f"json file '{file_path}' was created")
# except FileExistsError:
#     print('That file already exists!')


# csv file

import csv
employee = [
    ["Name", 'Age', 'Job'],
    ['SpongeBOB', 30, 'cook'],
    ["Patrick", 39, 'cook2'],
    ['Sandy', 21, 'Scientist']]

file_path = "output.csv"

try:
    with open(file_path, 'w', newline="") as file:
        writer = csv.writer(file)
        #loop each employee to display
        for row in employee:
            writer.writerow(row)
        print(f'csv was created {file_path}')
except FileExistsError:
    print("That file already existed!")
