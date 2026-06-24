# -*- coding: utf-8 -*-
"""
Вариант 1 .
Задание 1: сумма и количество положительных элементов над главной диагональю.
Задание 2: в каждой строке матрицы поменять местами максимальный и минимальный
           элементы с первым и последним элементами строки соответственно.
"""
print("=" * 60)
print("ЗАДАНИЕ 1: Сумма и число положительных элементов над главной диагональю")
print("=" * 60)

N = int(input("Введите размер квадратной матрицы N: "))

A = []
print("Введите элементы матрицы построчно:")
for i in range(N):
    row = []
    for j in range(N):
        row.append(int(input(f"A[{i}][{j}] = ")))
    A.append(row)

print("\nИсходная матрица A:")
for row in A:
    print(" ".join(map(str, row)))

sum_positive = 0
count_positive = 0
for i in range(N):
    for j in range(N):
        if i < j and A[i][j] > 0:
            sum_positive += A[i][j]
            count_positive += 1

print(f"\nСумма положительных элементов над главной диагональю: {sum_positive}")
print(f"Количество положительных элементов над главной диагональю: {count_positive}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: В каждой строке матрицы поменять местами")
print("максимальный элемент с первым, минимальный – с последним")
print("=" * 60)

N2 = int(input("Введите количество строк N: "))
M = int(input("Введите количество столбцов M: "))

B = []
print("Введите элементы матрицы построчно:")
for i in range(N2):
    row = []
    for j in range(M):
        row.append(int(input(f"B[{i}][{j}] = ")))
    B.append(row)

print("\nИсходная матрица B:")
for row in B:
    print(" ".join(map(str, row)))

for i in range(N2):
    max_idx = 0
    min_idx = 0
    for j in range(1, M):
        if B[i][j] > B[i][max_idx]:
            max_idx = j
        if B[i][j] < B[i][min_idx]:
            min_idx = j
    
    B[i][0], B[i][max_idx] = B[i][max_idx], B[i][0]
    
    B[i][M-1], B[i][min_idx] = B[i][min_idx], B[i][M-1]

print("\nПреобразованная матрица B:")
for row in B:
    print(" ".join(map(str, row)))