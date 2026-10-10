from math import *

print('Введите Xbeg, Xend и Dx')
xb = float(input('Xbeg='))
xe = float(input('Xend='))
dx = float(input('Dx='))

print("Xbeg={0: 7.2f} Xend={1: 7.2f}".format(xb, xe))
print("Dx={0: 7.2f}".format(dx))
print("+---------+---------+")
print("I    X    I    Y    I")
print("+---------+---------+")

xt = xb
while xt <= xe:
    if xt < 0:
        y = -3 - 0.5 * xt
    elif xt < 3:
        y = -sqrt(9 - xt**2)
    elif xt <= 6:
        y = sqrt(9 - (xt - 6)**2)
    else:
        y = 3
    print("I{0: 8.2f} I{1: 8.2f} I".format(xt, y))
    xt += dx

print("+---------+---------+")