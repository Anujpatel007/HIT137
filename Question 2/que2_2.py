def extract_and_convert(input_string):
  
    # start a dictionery of all the results
    result = {
        "numbers": "",
        "letters": "",
        "even_numbers": "",
        "upper_case_letters": "",
        "ascii_even_numbers": [],
        "ascii_upper_case_letters": []
    }

    # Separation of numbers and letters
    for char in input_string:
        if char.isdigit():
            result["numbers"] += char
        elif char.isalpha():
            result["letters"] += char

    # Converting the even numbers to ASCII even numbers
    for num in result["numbers"]:
        if int(num) % 2 == 0:
            result["even_numbers"] += num
            result["ascii_even_numbers"].append(ord(num))

    # Convert upper-case letters to ASCII upper-case letters
    for char in result["letters"]:
        if char.isupper():
            result["upper_case_letters"] += char
            result["ascii_upper_case_letters"].append(ord(char))

    return result

# Example usage
input_string = '56aAww1984sktr235270aYmn145ss785fssq31D0'
result = extract_and_convert(input_string)

print("Number String:", result["numbers"])
print("Letter String:", result["letters"])
print("Even Number String:", result["even_numbers"])
print("Upper-case Letter String:", result["upper_case_letters"])
print("ASCII Values of Even Numbers:", result["ascii_even_numbers"])
print("ASCII Values of Upper-case Letters:", result["ascii_upper_case_letters"])