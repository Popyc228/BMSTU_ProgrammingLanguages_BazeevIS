import numpy as np
from math import sqrt


def MakeMatr(n, a, b):
    """Инициализация квадратной матрицы NxN случайными числами в [a, b)"""
    return (b - a) * np.random.random(size=(n, n)) + a


def MidlDisp(Matr):
    """Вычисление среднего и дисперсии по всем элементам"""
    nRow, nCol = Matr.shape
    total = 0.0
    for i in range(nRow):
        for j in range(nCol):
            total += Matr[i][j]
    avg = total / Matr.size

    disp = 0.0
    for i in range(nRow):
        for j in range(nCol):
            disp += (Matr[i][j] - avg) ** 2
    disp = disp / (Matr.size - 1)
    return avg, disp


def CorrectMatr(Matr, avg, sigma):
    """Замена элементов, отклонение которых от среднего > sigma, на среднее"""
    nRow, nCol = Matr.shape
    for i in range(nRow):
        for j in range(nCol):
            if abs(Matr[i][j] - avg) > sigma:
                Matr[i][j] = avg
    return Matr


def PrintMatr(Matr):
    """Вывод матрицы на экран"""
    nRow, nCol = Matr.shape
    for i in range(nRow):
        for j in range(nCol):
            print("{0:7.3f}".format(Matr[i][j]), end=" ")
        print()
    print()


# Основная программа
n = int(input("Введите размер матрицы (NxN): "))
MyMatr = MakeMatr(n, -10, 10)  # диапазон [-10, 10)
print("Исходная матрица:")
PrintMatr(MyMatr)

avg, disp = MidlDisp(MyMatr)
sigma = sqrt(disp)
print("Среднее = {0:7.3f}".format(avg))
print("Дисперсия = {0:7.3f}, сигма = {1:7.3f}".format(disp, sigma))

NMatr = CorrectMatr(MyMatr, avg, sigma)
print("Скорректированная матрица:")
PrintMatr(NMatr)