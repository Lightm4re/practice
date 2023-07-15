vowels = "aeiouy"
string = input("Введите строку: ")

dictionary = {letter: letter in vowels for letter in string}

print(dictionary)