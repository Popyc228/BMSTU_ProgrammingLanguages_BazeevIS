import numpy as np
from random import randint

n = int(input("Введите размер матрицы: "))

# Генерируем матрицу и сохраняем в файл
matr = np.zeros((n, n), dtype=int)
for i in range(n):
    for j in range(n):
        matr[i][j] = randint(-5, 5)

fh = open("lab6.3_out.txt", "wt")
np.savetxt(fh, matr, fmt="%4d")
fh.close()

# Читаем матрицу из файла
fh = open("lab6.3_out.txt", "rt")
matr = np.loadtxt(fh, dtype=int, ndmin=2)
fh.close()

# Задание 1: произведение в строках без отрицательных
prods = []
for i in range(n):
    has_neg = False
    for j in range(n):
        if matr[i][j] < 0:
            has_neg = True
            break
    if not has_neg:
        p = 1
        for j in range(n):
            p *= matr[i][j]
        prods.append((i, p))

# Задание 2: максимум среди сумм диагоналей, параллельных главной
max_sum = None
for k in range(1, n):
    s = 0
    for i in range(n - k):
        s += matr[i][i + k]
    if max_sum is None or s > max_sum:
        max_sum = s
for k in range(1, n):
    s = 0
    for i in range(n - k):
        s += matr[i + k][i]
    if max_sum is None or s > max_sum:
        max_sum = s

# Записываем результаты
fo = open("lab6.3_out.txt", "wt")
fo.write("Исходная матрица:\n")
for i in range(n):
    for j in range(n):
        fo.write("{0:5d}".format(matr[i][j]))
    fo.write("\n")

fo.write("\nПроизведения в строках без отрицательных:\n")
if prods:
    for idx, p in prods:
        fo.write("Строка {0}: произведение = {1}\n".format(idx, p))
else:
    fo.write("Нет строк без отрицательных элементов.\n")

if max_sum is not None:
    fo.write("\nМаксимум среди сумм диагоналей: {0}\n".format(max_sum))
else:
    fo.write("\nНет диагоналей, параллельных главной.\n")

fo.close()
print("Результат в lab6.3_out.txt")