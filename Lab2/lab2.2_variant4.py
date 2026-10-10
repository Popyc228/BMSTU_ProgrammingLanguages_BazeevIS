from math import *

flag = 0

R = float(input('Введите радиус R: '))
x = float(input('X='))
y = float(input('Y='))

if (y >= 0 and x**2 + y**2 <= R**2) or (x <= 0 and y <= 0 and y >= -R and y <= x):
    flag = 1
else:
    flag = 0

print("Точка X={0:.2f} Y={1:.2f}".format(x, y), end=" ")
if flag:
    print("попадает", end=" ")
else:
    print("не попадает", end=" ")
print("в область.")