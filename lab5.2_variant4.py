from random import randint

def MakeIntMatr(n):
    """Создаёт целочисленную квадратную матрицу NxN случайными числами от -5 до 5"""
    matr = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(randint(-5, 5))
        matr.append(row)
    return matr

def PrintIntMatr(matr):
    """Вывод матрицы"""
    n = len(matr)
    for i in range(n):
        for j in range(n):
            print("{0:4d}".format(matr[i][j]), end=" ")
        print()
    print()

def ProductNoNegRows(matr):
    """Произведение элементов в строках без отрицательных чисел"""
    n = len(matr)
    result = []
    for i in range(n):
        has_neg = False
        for j in range(n):
            if matr[i][j] < 0:
                has_neg = True
                break
        if not has_neg:
            prod = 1
            for j in range(n):
                prod *= matr[i][j]
            result.append((i, prod))
    return result

def MaxSumParallelMainDiag(matr):
    """Максимум среди сумм элементов диагоналей, параллельных главной"""
    n = len(matr)
    max_sum = None
    # Диагонали выше главной (сдвиг k от 1 до n-1)
    for k in range(1, n):
        s = 0
        for i in range(n - k):
            s += matr[i][i + k]
        if max_sum is None or s > max_sum:
            max_sum = s
    # Диагонали ниже главной (сдвиг k от 1 до n-1)
    for k in range(1, n):
        s = 0
        for i in range(n - k):
            s += matr[i + k][i]
        if max_sum is None or s > max_sum:
            max_sum = s
    return max_sum

# Основная программа
n = int(input("Введите размер квадратной матрицы: "))
matr = MakeIntMatr(n)
print("Исходная матрица:")
PrintIntMatr(matr)

prods = ProductNoNegRows(matr)
print("Произведения в строках без отрицательных элементов:")
if prods:
    for idx, p in prods:
        print("Строка {0}: произведение = {1}".format(idx, p))
else:
    print("Нет строк без отрицательных элементов.")

max_s = MaxSumParallelMainDiag(matr)
if max_s is not None:
    print("Максимум среди сумм диагоналей, параллельных главной: {0}".format(max_s))
else:
    print("Диагоналей, параллельных главной, нет (матрица 1x1).")