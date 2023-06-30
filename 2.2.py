programs = ["Орел и решка", "Импровизация", "Comedy Club", "Что? Где? Когда?"]
print("Текущий список передач:")
for program in programs:
    print(program)

newprogram = input("Введите название новой передачи: ")
position = int(input("Введите позицию, на которой она должна быть вставлена: "))

programs.insert(position - 1, newprogram)
print("Обновленный список передач:")
for program in programs:
    print(program)