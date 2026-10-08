fi = open("lab6.2.txt", "rt")
n = int(fi.readline().strip())
line = fi.readline().strip()
mas = [float(x) for x in line.split()]
fi.close()

original = mas[:]

# Задание 1: сумма с нечетными номерами (индексы 0, 2, 4...)
sum_odd = 0.0
for i in range(n):
    if i % 2 == 0:
        sum_odd += mas[i]

# Задание 2: сумма между первым и последним отрицательными
first_neg = -1
last_neg = -1
for i in range(n):
    if mas[i] < 0:
        if first_neg == -1:
            first_neg = i
        last_neg = i

sum_between = 0.0
if first_neg != -1 and last_neg != -1 and first_neg < last_neg:
    for i in range(first_neg + 1, last_neg):
        sum_between += mas[i]

# Задание 3: сжатие (удалить |x| <= 1)
j = 0
for i in range(n):
    if abs(mas[i]) > 1.0:
        mas[j] = mas[i]
        j += 1
for i in range(j, n):
    mas[i] = 0.0

fo = open("lab6.2_out.txt", "wt")
fo.write("Исходный массив:\n")
for i in range(n):
    fo.write("{0:8.3f}".format(original[i]))
fo.write("\n\n")
fo.write("Сумма с нечетными номерами: {0:8.3f}\n".format(sum_odd))
fo.write("Сумма между первым и последним отриц.: {0:8.3f}\n".format(sum_between))
fo.write("\nСжатый массив:\n")
for i in range(n):
    fo.write("{0:8.3f}".format(mas[i]))
fo.write("\n")
fo.close()
print("Результат в lab6.2_out.txt")