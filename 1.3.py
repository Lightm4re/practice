num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))
if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        print("Числа в порядке убывания", num1, num2, num3)
    else:
        print("Числа в порядке убывания", num1, num3, num2)
elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        print("Числа в порядке убывания", num2, num1, num3)
    else:
        print("Числа в порядке убывания", num2, num3, num1)
else:
    if num1 >= num2:
        print("Числа в порядке убывания", num3, num1, num2)
    else:
        print("Числа в порядке убывания", num3, num2, num1)
