import csv

start_year = input("Введите левую границу (год) поиска: ")
end_year = input("Введите правую границу (год) поиска: ")

try:
    start_year = int(start_year)
    end_year = int(end_year)
except ValueError:
    print("Ошибка ввода")
    exit()

books_in_range = []

with open('books.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        year = int(row[2])
        if start_year <= year <= end_year:
            books_in_range.append(row)

if len(books_in_range) == 0:
    print("Нет книг в заданном диапозоне")
else:
    print("Книги, выпущенные между", start_year, "и", end_year)
    for book in books_in_range:
        print(book[0])
