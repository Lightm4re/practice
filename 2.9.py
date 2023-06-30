num = int(input("Введите натуральное число: "))
numstr = str(num)

indfromend = len(numstr) - numstr.index(max(numstr)) - 1
indfromstart = numstr.index(max(numstr))

print("Порядковый номер максимальной цифры от конца числа:", indfromend)
print("Порядковый номер максимальной цифры от начала числа:", indfromstart)
