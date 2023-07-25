string = input("Введите строку: ")

dictionary = {letter: string.count(letter) for letter in string if letter != ' '}

print(dictionary)
