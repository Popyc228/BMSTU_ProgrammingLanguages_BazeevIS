from math import log
import turtle as tr

def ln_series(x, eps=1e-3):
    """Вычисление ln(1+x) через ряд Тейлора с точностью eps"""
    if x <= -1 or x > 1:
        return None
    an = x        # первый член ряда
    s = an        # сумма
    n = 1
    while abs(an) > eps:
        an = -an * x * n / (n + 1)
        s += an
        n += 1
    return s

# Границы графика
xmin, xmax = -0.9, 0.9
ymin, ymax = -3.5, 1.5

# Настройка окна
Dx = 800
Dy = Dx / ((xmax - xmin) / (ymax - ymin))
tr.setup(Dx, Dy)
tr.setworldcoordinates(xmin, ymin, xmax, ymax)
tr.title("ln(1+x) через ряд (вариант 4)")
tr.width(2)

# ---------- ОСИ ----------
tr.up(); tr.goto(xmin, 0); tr.down(); tr.goto(xmax, 0)
tr.up(); tr.goto(0, ymin); tr.down(); tr.goto(0, ymax)

# Стрелки
tr.up(); tr.goto(xmax, 0); tr.down()
tr.goto(xmax - 0.04, 0.1); tr.up(); tr.goto(xmax, 0); tr.down()
tr.goto(xmax - 0.04, -0.1)
tr.up(); tr.goto(0, ymax); tr.down()
tr.goto(0.02, ymax - 0.15); tr.up(); tr.goto(0, ymax); tr.down()
tr.goto(-0.02, ymax - 0.15)

# Подписи
tr.up()
tr.goto(xmax - 0.05, -0.35)
tr.write("X", font=("Arial", 14, "bold"))
tr.goto(0.02, ymax - 0.2)
tr.write("Y", font=("Arial", 14, "bold"))

# ---------- ДЕЛЕНИЯ И ЦИФРЫ ----------
tr.color("black")
tr.width(1)

# По оси X с шагом 0.2
i = -0.8
while i <= 0.81:
    if abs(i) < 0.01:
        i += 0.2
        continue
    tr.up(); tr.goto(i, 0); tr.down(); tr.goto(i, -0.15)
    tr.up(); tr.goto(i, -0.35)
    tr.write("{0:.1f}".format(i), align="center", font=("Arial", 8, "normal"))
    i += 0.2

# По оси Y с шагом 1
for i in range(-3, 2):
    if i == 0:
        continue
    tr.up(); tr.goto(0, i); tr.down(); tr.goto(-0.03, i)
    tr.up(); tr.goto(-0.05, i - 0.07)
    tr.write(str(i), align="right", font=("Arial", 8, "normal"))

# Подпись нуля
tr.up(); tr.goto(-0.03, -0.25)
tr.write("0", align="right", font=("Arial", 8, "normal"))

# ---------- ГРАФИК ЧЕРЕЗ РЯД (красный) ----------
tr.up()
tr.color("red")
tr.width(3)
step = (xmax - xmin) / 500
x = xmin
y = ln_series(x)
if y is not None:
    tr.goto(x, y); tr.down()
while x <= xmax:
    x += step
    y = ln_series(x)
    if y is not None:
        tr.goto(x, y)

# ---------- ЭТАЛОННЫЙ ln(1+x) (синий) ----------
tr.up()
tr.color("blue")
tr.width(1)
x = xmin
y = log(1 + x)
tr.goto(x, y); tr.down()
while x <= xmax:
    x += step
    if 1 + x > 0:
        y = log(1 + x)
        tr.goto(x, y)

# Легенда
tr.up()
tr.color("red")
tr.goto(-0.8, 1.2)
tr.write("Ряд Тейлора", font=("Arial", 10, "bold"))
tr.color("blue")
tr.goto(-0.8, 0.9)
tr.write("ln(1+x)", font=("Arial", 10, "bold"))

tr.done()