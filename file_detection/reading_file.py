

import json
import csv

file_path = "output.csv"

try:
    with open(file_path, 'r') as file:
        content = csv.reader(file)
        for line in content:
            print(line)

except FileNotFoundError:
    print("That file was not found!")
