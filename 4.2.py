def find_palindromes(string):
    def is_palindrome(substring):
        return substring == substring[:: - 1]
    palindromes = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            if is_palindrome(substring):
                palindromes.append(substring)

    return palindromes


input_string = input("Введите строку: ")
result = find_palindromes(input_string)

if len(result) == 0:
    print("В заданной строке нет палиндромов.")
else:

    print("Палиндромы в заданной строке:")
    for palindrome in result:
        if len(palindrome) > 1:
            print(palindrome)
