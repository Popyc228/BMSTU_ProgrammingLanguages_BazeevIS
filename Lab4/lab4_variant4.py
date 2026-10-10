from random import *

# Ввод количества элементов
n = int(input("Элементов в массиве (N<=30) N: "))
if n > 30:
    n = 30
elif n < 5:
    n = 5

# Генерация массива и вывод начального состояния
print("Начальное состояние")
mas = []
for i in range(n):
    mas.append(uniform(-5, 5))
    print("{0: 7.3f}".format(mas[i]), end=" ")
print()

# Сумма элементов с нечетными номерами
sum_odd = 0.0
for i in range(n):
    if i % 2 == 0:
        sum_odd = sum_odd + mas[i]

# Поиск первого и последнего отрицательных элементов
first_neg = -1
last_neg = -1
for i in range(n):
    if mas[i] < 0:
        if first_neg == -1:
            first_neg = i
        last_neg = i

# Сумма элементов между первым и последним отрицательными
sum_between = 0.0
if first_neg != -1 and last_neg != -1 and first_neg < last_neg:
    for i in range(first_neg + 1, last_neg):
        sum_between = sum_between + mas[i]

# Сжатие массива (удаление элементов с модулем <= 1)
j = 0
for i in range(n):
    if abs(mas[i]) > 1.0:
        mas[j] = mas[i]
        j = j + 1

# Заполнение освободившихся позиций нулями
for i in range(j, n):
    mas[i] = 0.0

# Вывод конечного состояния и результатов
print("Конечное состояние")
for i in range(n):
    print("{0: 7.3f}".format(mas[i]), end=" ")
print()
print("Сумма с нечетными номерами: {0:7.3f}".format(sum_odd))
print("Сумма между первым и последним отриц.: {0:7.3f}".format(sum_between))