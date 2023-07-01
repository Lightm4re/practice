import random

length = int(input("Введите длину списка: "))
start = int(input("Введите начальное значение диапазона: "))
end = int(input("Введите конечное значение диапазона: "))

num = [random.randint(start, end) for i in range(length)]
print("Список чисел: ")
print(num)
aver = lambda numbers: sum(numbers) / len(numbers)
print ("Среднее значение списка: ")
print(aver(num))
