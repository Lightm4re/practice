import itertools

def get_permutations(lst):
    permutations = list(itertools.permutations(lst))
    return permutations

lst = input("Введите элементы списка через пробел: ").split()
permutations = get_permutations(lst)
print("Все перестановки списка:", permutations)