from math import sqrt
import turtle as tr

def func(x):
    """Кусочная функция из лаб. №2 (вариант 4)"""
    if x < 0:
        return -3 - 0.5 * x
    elif x < 3:
        return -sqrt(9 - x**2)
    elif x <= 6:
        return sqrt(9 - (x - 6)**2)
    else:
        return 3

# Границы графика
xmin, xmax = -10, 10
ymin, ymax = -4, 4

# Настройка окна
Dx = 900
Dy = Dx / ((xmax - xmin) / (ymax - ymin))
tr.setup(Dx, Dy)
tr.setworldcoordinates(xmin, ymin, xmax, ymax)
tr.title("График функции (вариант 4)")
tr.width(2)

# ---------- ОСИ ----------
# Ось X
tr.up(); tr.goto(xmin, 0); tr.down(); tr.goto(xmax, 0)
# Ось Y
tr.up(); tr.goto(0, ymin); tr.down(); tr.goto(0, ymax)

# Стрелки на осях
# Стрелка на X
tr.up(); tr.goto(xmax, 0); tr.down()
tr.goto(xmax - 0.4, 0.15); tr.up(); tr.goto(xmax, 0); tr.down()
tr.goto(xmax - 0.4, -0.15)
# Стрелка на Y
tr.up(); tr.goto(0, ymax); tr.down()
tr.goto(0.15, ymax - 0.15); tr.up(); tr.goto(0, ymax); tr.down()
tr.goto(-0.15, ymax - 0.15)

# Подписи осей
tr.up()
tr.goto(xmax - 0.3, -0.6)
tr.write("X", font=("Arial", 14, "bold"))
tr.goto(0.3, ymax - 0.3)
tr.write("Y", font=("Arial", 14, "bold"))

# ---------- ДЕЛЕНИЯ И ЦИФРЫ ----------
tr.color("black")
tr.width(1)

# Деления на оси X (шаг 2)
for i in range(xmin, xmax + 1, 2):
    if i == 0:
        continue
    tr.up(); tr.goto(i, 0); tr.down(); tr.goto(i, -0.2)
    tr.up(); tr.goto(i, -0.8)
    tr.write(str(i), align="center", font=("Arial", 8, "normal"))

# Деления на оси Y (шаг 1)
for i in range(ymin, ymax + 1):
    if i == 0:
        continue
    tr.up(); tr.goto(0, i); tr.down(); tr.goto(-0.25, i)
    tr.up(); tr.goto(-0.7, i - 0.15)
    tr.write(str(i), align="right", font=("Arial", 8, "normal"))

# Подпись нуля
tr.up(); tr.goto(-0.4, -0.7)
tr.write("0", align="right", font=("Arial", 8, "normal"))

# ---------- ГРАФИК ФУНКЦИИ ----------
tr.up()
tr.color("blue")
tr.width(3)
step = (xmax - xmin) / 1000
x = xmin
y = func(x)
tr.goto(x, y); tr.down()
while x <= xmax:
    x += step
    y = func(x)
    tr.goto(x, y)

tr.done()