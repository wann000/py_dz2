# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22
def sum_odd(lst):
    s = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            s += lst[i]
    print('Исходный массив',lst)
    print(f"Сумма равна: {s}")

lst=[0, 1, 0, 1, 0, 1]
#lst = list(map(int, input("Введите числа через пробел:\n").split()))
sum_odd(lst)