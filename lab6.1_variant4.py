from math import *

def f1(a, x):
    y = (tan(x**2/2 - 1)**2 + (2*cos(x - pi/6)) / (1/2 + sin(a)**2))
    return y

def f2(x):
    y = pow(2, log(3 - cos(pi/4 + 2*x), 3 + sin(x)) / (1 + tan(2*x/pi)**2))
    return y

fi = open("lab6.1.txt", "rt")
fo = open("lab6.1_out.txt", "wt")

# пропускаем две строки заголовка
fi.readline()
fi.readline()

# шапка таблицы
fo.write("+============+============+============+============+\n")
fo.write("I     A      I     X      I     F1     I     F2     I\n")
fo.write("+============+============+============+============+\n")

for line in fi:
    if line.strip() == "":
        continue
    b, c = line.split()
    a = float(b)
    x = float(c)
    fo.write("I {0:10.2f} I {1:10.2f} I {2:10.4f} I {3:10.4f} I\n".format(a, x, f1(a, x), f2(x)))

fo.write("+============+============+============+============+\n")
fi.close()
fo.close()
print("Результат в файле lab6_out.txt")