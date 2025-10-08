from operator import eq


lista_1 = [1, 2, 3, 4, 5, 6, 7, 8]
lista_2 = [2, 2, 3, 1, 2, 6, 7, 9]


def igual(a, b):
    return a == b

total_1 = list(map(eq, lista_1, lista_2))


total = sum(map(lambda x, y: x == y, lista_1, lista_2))

print(total_1)
print(total)