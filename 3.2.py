fibonacci = lambda n: [fib(i) for i in range(n) if fib(i) < n]
fib = lambda n: n if n <= 1 else fib(n - 1) + fib(n - 2)

n = int(input("Введите число: "))
fib_list = fibonacci(n)
print("Числа Фибоначчи до числа", n, ":", fib_list)
