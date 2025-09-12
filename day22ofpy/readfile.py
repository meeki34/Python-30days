# python reading files (.txt,.json,csv)
import json

file_path = "C:\\Users\\zahis\\OneDrive\\Desktop\\Nice.json"

try:
    with open(file_path, "r") as file:# return an object 
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e} ")
except PermissionError:
    print(f"Permission denied to access '{file_path}'.")
except Exception as e:
    print(f"An error occurred: {e}")