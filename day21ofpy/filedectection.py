#Python file detection 

import os # this allows us to use the os module

file_path = r"C:\Users\zahis\OneDrive\Desktop\test.txt"
if os.path.exists(file_path):
    print(f"File exists: {file_path}")
    if os.path.isfile(file_path):
        print(f"{file_path} is a file")
    elif os.path.isdir(file_path):
        print(f"{file_path} is a directory")
else:
    print(f"File does not exist: {file_path}")
    