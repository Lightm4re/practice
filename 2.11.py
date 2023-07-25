a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))

for num in range(a, b + 1):
    sum += num

print("Сумма всех целых чисел от", a, "до", b, "включительно:", sum)
