def rot13(string):
    encoded_string = ''
    for char in string:
        if char.isalpha():
            if char.islower():
                encoded_char = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            else:
                encoded_char = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            encoded_char = char
        encoded_string += encoded_char
    return encoded_string


text = input("Введите строку: ")
encoded_text = rot13(text)
print("Закодированная строка:", encoded_text)
