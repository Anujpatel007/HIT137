def extract_and_convert(input_string):
# Separate numbers and letters
for char in input_string:
    if char.isdigit():
            result["numbers"] += char
    elif char.isalpha():
            result["letters"] += char


# Example usage
input_string = '56aAww1984sktr235270aYmn145ss785fssq31D0'
result = extract_and_convert(input_string)

print("Number String:", result["numbers"])
print("Letter String:", result["letters"])