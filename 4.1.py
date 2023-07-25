def get_largest_permutation(num):
    num_str = str(num)
    digits = sorted(num_str, reverse=True)
    largest_permutation = int(''.join(digits))
    return largest_permutation


num = int(input("Введите число: "))
largest_permutation = get_largest_permutation(num)
print("Наиб. число, при перестановки цифр", num, ":", largest_permutation)
