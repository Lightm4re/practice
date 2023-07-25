import csv

books_data = [
    ["Книга", "Автор", "Год"],
    ["Гарри Поттер", "Д.К. Роулинг", "1997"],
    ["Метро 2033", "Д. Глуховский", "2005"],
    ["Метро 2034", "Д. Глуховский", "2009"],
    ["Ведьмак. Последнее желание", "А. Сапковский", "1986"]
]

with open('books.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(books_data)
