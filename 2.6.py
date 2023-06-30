distance = float(input("Сколько километров хотите проехать на автомобиле?: "))
fuel_consumption = float(input("Сколько литров топлива расходует автомобиль на 100 километров?: "))
fuel_in_tank = float(input("Сколько литров топлива в вашем баке?: "))

fuel_needed = distance / 100 * fuel_consumption

if fuel_needed <= fuel_in_tank:
    print("Проедете желаемое расстояние")
else:
    print("Не хватит топлива для преодоления желаемого расстояния")
