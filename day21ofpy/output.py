# Python writing files (.txt, .json, .csv)
# https://docs.python.org/3/library/functions.html#open

txt_data = "I like pizza"
file_path = r"F:\Python 30 days\newfile\output.txt"

try:
    with open (file_path, "x") as file:
        file.write(txt_data)
        print(f"Txt file {file_path} was created")
except FileExistsError:
    print(f"File {file_path} already exists")
# x = 

# w = write
# a = append
# r = read
# t = text
# b = binary