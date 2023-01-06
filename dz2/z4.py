#4. Напишите программу, которая принимает на вход 2 числа.
#Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
#Найдите произведение элементов на указанных позициях(не индексах).
#Enter the value of N: 5
#Position one: 1
#Position two: 2
#-> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
#-> 20

#Enter the value of N: 4
#Position one: 20
#Position two: 22
#-> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
#-> There are no values for these indexes!
n = int(input('Введите число '))
p1 = int(input('Введите № первой позиции '))
p2 =int(input('Введите № второй позиции '))
lst = [(i+1) for i in range(-(n+1), n)]
print(f'Последовательность: {lst}')
for i in range(len(lst)):
    mult = lst[p1 -1]*lst[p2 - 1]
print(f'Mult of elements: {lst[p1 -1]} * {lst[p2 -1]} =', mult)