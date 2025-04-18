# Python writing files (.txt, .json, .csv)
import json
import csv

employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}

employees = [["Name", "Age", "Job"],
                ["Spongebob", 30, "Cook"],
                ["Patrick", 37, "Unemployed"],
                ["andy", 27, "Scientist"]]
# employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]
txt_data = "I like pizza!"

file_path = "output.csv"

try:
    with open(file=file_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        # if output is a json file
        # json.dump(employee, file, indent=4)
        # if input is a list
        # for employee in employees:
        #     file.write(employee + "\n")
        # if input is a string
        # file.write("\n" + txt_data)
        # print(f"txt file '{file_path}' was created")
        # print(f"json file '{file_path}' was created")
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")
except TypeError:
    print("")