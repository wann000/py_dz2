# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

from cmath import pi

d = int(input('Введите точность числа Пи '))
print(f'Число Пи с заданной точностью {d} равно {round(pi,d)}')
z=1/3
print(f'Число Пи с заданной точностью {d} равно {round(z,d)}')