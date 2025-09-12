# python reading files (.txt,.json,csv)
import json
import csv
file_path = "C:\\Users\\zahis\\OneDrive\\Desktop\\Nice.json"

try:
    with open(file_path, "r") as file:# return an object 
        content = csv.reader(file)
        for line in content:
            print(line)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e} ")
except PermissionError:
    print(f"Permission denied to access '{file_path}'.")
except Exception as e:
    print(f"An error occurred: {e}")