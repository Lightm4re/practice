num = int(input("Введите число: "))
num_str = str(num)
length = len(num_str)

sum = 0
for digit_str in num_str:
    digit = int(digit_str)
    sum += digit ** length

if sum == num:
    print("Число является числом Армстронга")
else:
    print("Число не является числом Армстронга")
