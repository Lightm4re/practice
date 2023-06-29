points = int(input("Введите количество очков: "))

if points == 3:
    result = "Выигрыш"
elif points == 1:
    result = "Ничья"
elif points == 0:
    result = "Проигрыш"
else:
    result = "Неверное количество очков"

print("Результат игры:", result)