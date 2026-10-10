from math import *

print('Введите Xbeg, Xend, Dx и Eps')
xb = float(input('Xbeg='))
xe = float(input('Xend='))
dx = float(input('Dx='))
eps = float(input('Eps='))

print("+---------+---------+-----+")
print("I    X    I    Y    I  N  I")
print("+---------+---------+-----+")

xt = xb
while xt <= xe:
    an = xt  # Первый член ряда (x)
    y = an  # Начальная сумма
    n = 1  # Номер текущего члена (начиная с 1, так как x - это первый член)

    while True:
        # Вычисляем следующий член ряда по рекуррентной формуле
        an = -an * xt * n / (n + 1)
        y = y + an
        n = n + 1
        if abs(an) < eps:
            break

    print("I{0: 8.2f} I{1: 8.3f} I{2: 3} I".format(xt, y, n))
    xt = xt + dx

print("+---------+---------+-----+")