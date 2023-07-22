def find_combinations(nums, target_sum):
    result = []
    combination = []
    find_combinations_helper(nums, target_sum, 0, combination, result)
    return result

def find_combinations_helper(nums, target_sum, start_index, combination, result):
    if sum(combination) == target_sum:
        result.append(combination[:])

    for i in range(start_index, len(nums)):
        combination.append(nums[i])
        find_combinations_helper(nums, target_sum, i + 1, combination, result)
        combination.pop()

nums = []
n = int(input("Введите количество чисел: "))
for i in range(n):
    num = int(input("Введите число: "))
    nums.append(num)
target_sum = int(input("Введите требуемую сумму: "))
combinations = find_combinations(nums, target_sum)

if len(combinations) == 0:
    print("Нет комбинаций, сумма которых равна заданному числу.")
else:
    print("Уникальные комбинации чисел, сумма которых равна заданному числу:")
    for combination in combinations:
        print(combination)