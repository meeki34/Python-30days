# validation of string input

# 1. the users should input a string
# 2. the string should not be empty
# 3. the string should not contain any digits

def validate_string(input_string):
    if not isinstance(input_string, str):
        return "Input must be a string."
    if not input_string:
        return "String cannot be empty."
    if any(char.isdigit() for char in input_string):
        return "String cannot contain digits."
    return "Valid string."

print(validate_string("Hello World!"))  # Output: Valid string.
print(validate_string(""))  # Output: String cannot be empty.