# Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
#v10
#-> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#-> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

n = int(input('Введите число '))
lst = [(i+1) for i in range(-(n+1), n)]
mix=lst
print(f'Исходный массив: {lst}')

for i in range(len(lst)):
    import random
    j = random.randint(0, i + 1)
    mix[i], mix[j] = mix[j], mix[i]
print('Перемешанный массив:', mix)