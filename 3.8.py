import string

dictionary = {letter: ord(letter.lower()) - ord('a') + 1 for letter in string.ascii_lowercase}

print(dictionary)