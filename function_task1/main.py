def add_string_letters_to_array(string: str) -> list:
    letters_array = []
    string_length = len(string)
    letter_index = 0
    while letter_index <= string_length - 1:
        current_letter = string[letter_index]
        if current_letter.isalpha() and current_letter != "m" and current_letter != "n" and current_letter != "M" and current_letter != "N":
            letters_array.append(current_letter)
        letter_index = letter_index + 1

        if len(letters_array) >= 100:
            break
    return letters_array

print(add_string_letters_to_array("Hello World!"))
