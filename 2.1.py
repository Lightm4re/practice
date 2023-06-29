import random

colors = ["красный", "синий", "зеленый", "желтый", "оранжевый"]

random_color = random.choice(colors)
print("Выберите цвет из списка:", colors)

while True:
    user_color = input("Ваш выбор: ")
    if user_color == random_color:
        print("Отлично!")
        break
    else:
        print("Неверно. Подумайте о других цветах")
        match random_color:
            case "красный":
                print("Подсказка: цвет вишни")
            case "синий":
                print("Подсказка: цвет неба")
            case "зеленый":
                print("Подсказка: цвет травы")
            case "желтый":
                print("Подсказка: цвет солнца")
            case "оранжевый":
                print("Подсказка: цвет мандаринов")
        print()
