# json file is key value pair 
import json

employees = {
    "name" :"syed zahid",
    "age": 30,
    "job":"developer"
}

file_path = r"C:\Users\zahis\OneDrive\Desktop\Nice.json"

try:
    with open(file_path, "w") as file:
        json.dump(employees, file, indent = 4)
        print(f"json file '{file_path}' created successfully.")
except FileExistsError:
    print(f"File '{file_path}' already exists.")
except Exception as e:
    print(f"An error occurred: {e}")