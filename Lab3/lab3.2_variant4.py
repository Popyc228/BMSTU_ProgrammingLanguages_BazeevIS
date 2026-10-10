from math import *
from random import *

R = float(input('Введите радиус R: '))
flag = 0

print("   X       Y     Res")
print("-------------------")

for n in range(10):
    # Генерируем координаты в пределах от -R до R
    x = uniform(-R, R)
    y = uniform(-R, R)

    # Проверка попадания в область (полукруг или треугольник)
    if (y >= 0 and x ** 2 + y ** 2 <= R ** 2) or (x <= 0 and y <= 0 and y >= -R and y <= x):
        flag = 1
    else:
        flag = 0

    print("{0: 7.2f} {1: 7.2f}".format(x, y), end=" ")
    if flag:
        print("Yes")
    else:
        print("No")