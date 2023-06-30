a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

discriminant = b**2 - 4*a*c

if discriminant < 0:
    print("Корней нет")
elif discriminant == 0:
    root = -b / (2*a)
    print("Корень уравнения:", root)
else:
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    print("Корни уравнения:", root1, "и", root2)
