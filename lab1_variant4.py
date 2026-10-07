from math import*

alpha = float(input("Введите значение alpha (в радианах): "))

z1 = (2 * cos(alpha) * sin(2 * alpha) - sin(alpha)) / (cos(alpha) - 2 * sin(alpha) * sin(2 * alpha))
z2  = tan(3 * alpha)

print("z1 = {0:4f}".format(z1))
print("z2 = {0:4f}".format(z2))