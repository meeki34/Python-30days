# json file is key value pair 
import json
import csv

employees = [["name", "age", "job"],
             ["syed zahid", 30, "developer"],
             ["Ramesh",21,"developer"]]

file_path = r"C:\Users\zahis\OneDrive\Desktop\Nice.json"

try:
    with open(file_path, "w") as file:
        write = csv.writer(file)
        for row in employees:
            write.writerow(row)
        print(f"csv file '{file_path}' created successfully.")
except FileExistsError:
    print(f"File '{file_path}' already exists.")
except Exception as e:
    print(f"An error occurred: {e}")