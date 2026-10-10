import turtle as tr
from random import uniform
from math import pi

R = float(input("Введите радиус R: "))

def inside(x, y):
    """Проверка попадания точки в заштрихованную область"""
    # Верхний полукруг радиуса R с центром (0, 0)
    if y >= 0 and x**2 + y**2 <= R**2:
        return True
    # Нижний треугольник: (0,0), (-R,-R), (0,-R)
    if x <= 0 and y <= 0 and y >= -R and y <= x:
        return True
    return False

# Границы области генерации
xmin, xmax = -R, R
ymin, ymax = -R, R

# Настройка окна
Dx = 700
Dy = Dx / ((xmax - xmin) / (ymax - ymin))
tr.setup(Dx, Dy)
tr.setworldcoordinates(xmin, ymin, xmax, ymax)
tr.title("Метод Монте-Карло (вариант 4)")
tr.width(2)

# ---------- ГЕНЕРАЦИЯ ТОЧЕК ----------
Nmax = 10000
Nf = 0
tr.up()
tr.tracer(0, 0)

for _ in range(Nmax):
    x = uniform(xmin, xmax)
    y = uniform(ymin, ymax)
    if inside(x, y):
        tr.goto(x, y)
        tr.dot(3, "green")
        Nf += 1

tr.tracer(1, 0)

# ---------- ОСИ ----------
tr.color("black")
tr.width(2)
tr.up(); tr.goto(xmin, 0); tr.down(); tr.goto(xmax, 0)
tr.up(); tr.goto(0, ymin); tr.down(); tr.goto(0, ymax)

# Стрелки
tr.up(); tr.goto(xmax, 0); tr.down()
tr.goto(xmax - 0.1*R, 0.05*R); tr.up(); tr.goto(xmax, 0); tr.down()
tr.goto(xmax - 0.1*R, -0.05*R)
tr.up(); tr.goto(0, ymax); tr.down()
tr.goto(0.05*R, ymax - 0.1*R); tr.up(); tr.goto(0, ymax); tr.down()
tr.goto(-0.05*R, ymax - 0.1*R)

# Подписи осей
tr.up()
tr.goto(xmax - 0.1*R, -0.15*R)
tr.write("X", font=("Arial", 14, "bold"))
tr.goto(0.05*R, ymax - 0.1*R)
tr.write("Y", font=("Arial", 14, "bold"))

# ---------- ДЕЛЕНИЯ И ЦИФРЫ ----------
tr.width(1)
step_x = max(1, int(R / 3))
for i in range(-int(R), int(R) + 1, step_x):
    if i == 0:
        continue
    tr.up(); tr.goto(i, 0); tr.down(); tr.goto(i, -0.05*R)
    tr.up(); tr.goto(i, -0.12*R)
    tr.write(str(i), align="center", font=("Arial", 8, "normal"))

for i in range(-int(R), int(R) + 1, step_x):
    if i == 0:
        continue
    tr.up(); tr.goto(0, i); tr.down(); tr.goto(-0.05*R, i)
    tr.up(); tr.goto(-0.1*R, i - 0.02*R)
    tr.write(str(i), align="right", font=("Arial", 8, "normal"))

# Подпись нуля
tr.up(); tr.goto(-0.05*R, -0.12*R)
tr.write("0", align="right", font=("Arial", 8, "normal"))

# ---------- ОЦЕНКА ПЛОЩАДИ ----------
S_rect = (xmax - xmin) * (ymax - ymin)
S_mc = S_rect * Nf / Nmax
S_real = (pi/2 + 0.5) * R**2
err = abs(S_mc - S_real) / S_real * 100

tr.up()
tr.color("blue")
tr.goto(xmin + 0.1*R, ymax - 0.15*R)
mes = "N={0}\nNf={1}\nS_mc={2:.3f}\nS_real={3:.3f}\nErr={4:.2f}%".format(
    Nmax, Nf, S_mc, S_real, err)
tr.write(mes, font=("Arial", 11, "bold"))

tr.done()
print("Оценка площади: {0:.4f}".format(S_mc))
print("Точная площадь: {0:.4f}".format(S_real))
print("Ошибка: {0:.2f}%".format(err))