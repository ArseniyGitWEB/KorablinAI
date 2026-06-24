# -*- coding: utf-8 -*-
"""
Вариант 1 из 9 для 10 практики.
1) Сумма и количество положительных элементов над главной диагональю.
2) В каждой строке матрицы поменять местами максимальный и минимальный
   элементы с первым и последним элементами строки соответственно.

Ввод данных из файла: ФИО_группа_vvod.txt
Вывод результатов в файл: ФИО_группа_vivod.txt
"""

import os

INPUT_FILE = "KorablinAI_group_vvod.txt"
OUTPUT_FILE = "KorablinAI_group_vivod.txt"

def read_matrix_from_file(filename):
    """
    Читает матрицу из файла.
    Формат файла:
    - Первая строка: два числа N M (размеры матрицы)
    - Затем N строк, каждая содержит M чисел
    """
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
        if not lines:
            raise ValueError("Файл пуст или содержит только пустые строки")

        first_line = lines[0].split()
        if len(first_line) != 2:
            raise ValueError("Первая строка должна содержать два числа: N и M")

        N = int(first_line[0])
        M = int(first_line[1])

        matrix = []
        for i in range(1, N + 1):
            if i >= len(lines):
                raise ValueError(f"Недостаточно строк для матрицы {N}x{M}")
            row = list(map(int, lines[i].split()))
            if len(row) != M:
                raise ValueError(f"Строка {i} должна содержать {M} чисел")
            matrix.append(row)

        return N, M, matrix


def write_results_to_file(filename, results):
    """Записывает результаты в файл."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("=" * 60 + "\n")
        f.write("ЗАДАНИЕ 1: Сумма и число положительных элементов\n")
        f.write("          над главной диагональю\n")
        f.write("=" * 60 + "\n")

        f.write(f"Сумма положительных элементов: {results['sum_positive']}\n")
        f.write(f"Количество положительных элементов: {results['count_positive']}\n")

        f.write("\n" + "=" * 60 + "\n")
        f.write("ЗАДАНИЕ 2: В каждой строке матрицы поменять местами\n")
        f.write("максимальный элемент с первым, минимальный – с последним\n")
        f.write("=" * 60 + "\n")

        f.write("Исходная матрица:\n")
        for row in results['original_matrix']:
            f.write(" ".join(map(str, row)) + "\n")

        f.write("\nПреобразованная матрица:\n")
        for row in results['transformed_matrix']:
            f.write(" ".join(map(str, row)) + "\n")


def task1(N, A):
    """Задание 1: сумма и количество положительных элементов над главной диагональю."""
    sum_positive = 0
    count_positive = 0
    for i in range(N):
        for j in range(N):
            if i < j and A[i][j] > 0:
                sum_positive += A[i][j]
                count_positive += 1
    return sum_positive, count_positive


def task2(N, M, B):
    """Задание 2: в каждой строке поменять макс с первым, мин с последним."""
    transformed = [row[:] for row in B]
    for i in range(N):
        max_idx = 0
        min_idx = 0
        for j in range(1, M):
            if transformed[i][j] > transformed[i][max_idx]:
                max_idx = j
            if transformed[i][j] < transformed[i][min_idx]:
                min_idx = j
        transformed[i][0], transformed[i][max_idx] = transformed[i][max_idx], transformed[i][0]
        transformed[i][M - 1], transformed[i][min_idx] = transformed[i][min_idx], transformed[i][M - 1]
    return transformed


def main():
    print(f"Чтение данных из файла: {INPUT_FILE}")

    if not os.path.exists(INPUT_FILE):
        print(f"ОШИБКА: Файл {INPUT_FILE} не найден!")
        print("\nСоздайте файл со следующим содержимым:")
        print("3 3")
        print("-1 2 -3")
        print("4 -5 6")
        print("7 -8 9")
        print("\nЗатем для второго задания (размер 2x3):")
        print("2 3")
        print("5 1 9")
        print("3 8 2")
        return

    try:
        print(f"Чтение первой матрицы (квадратная) для задания 1...")
        N, _, A = read_matrix_from_file(INPUT_FILE)

        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]

        idx = 0
        n1 = int(lines[idx].split()[0])
        m1 = int(lines[idx].split()[1])
        idx += 1
        A = []
        for _ in range(n1):
            A.append(list(map(int, lines[idx].split())))
            idx += 1

        if idx < len(lines):
            n2 = int(lines[idx].split()[0])
            m2 = int(lines[idx].split()[1])
            idx += 1
            B = []
            for _ in range(n2):
                B.append(list(map(int, lines[idx].split())))
                idx += 1
        else:
            print("В файле только одна матрица. Используем её для обоих заданий.")
            B = [row[:] for row in A]
            n2, m2 = n1, m1

        sum_positive, count_positive = task1(n1, A)

        transformed_B = task2(n2, m2, B)

        results = {
            'sum_positive': sum_positive,
            'count_positive': count_positive,
            'original_matrix': B,
            'transformed_matrix': transformed_B
        }

        write_results_to_file(OUTPUT_FILE, results)
        print(f"\nРезультаты записаны в файл: {OUTPUT_FILE}")
        print("Программа успешно выполнена!")

    except Exception as e:
        print(f"Ошибка при выполнении программы: {e}")


if __name__ == "__main__":
    main()