# Python reading files (.txt, .json, .csv)
import json
import csv

file_path = "../writing_files/output.csv"
# file_path = "../writing_files/output.json"
# file_path = "../writing_files/output.txt"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
            # use bracket notation to access individual columns
            # print(line[0])
        # if file is json
        # content = json.load(file)
        # if file is text
        # content = file.read()
        # print(content)
        # use bracket notation to access individual properties
        # print(content["name"])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You don't have permission to read that file")
