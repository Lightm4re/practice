def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

k = int(input("Введите конечное число: "))
numbers = [num for num in range(2, k) if not isprime(num)]
print(numbers)