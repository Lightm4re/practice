import csv

num_entries = int(input("Сколько книг вы хотите добавить? "))
books = []
for _ in range(num_entries):
    book_input = input("Запишите данные книги ( название, автор, год) ")
    book_data = book_input.split(",")
    books.append(book_data)
with open('books.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(books)

print("Книги добавлены в файл")

desired_author = input("Введите автора для поиска:  ")

found_books = []
with open('books.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[1] == desired_author:
            found_books.append(row[0])

if len(found_books) == 0:
    print("Книги данного автора не найдены")
else:
    print("Книги, которые написал", desired_author)
    for book in found_books:
        print(book)