python
# -*- coding: utf-8 -*-
"""
Вариант 1 (из занятия 8 – функции и процедуры).
Задание 1: программа для вычисления площади разных геометрических фигур.
Задание 2: для 3 массивов найти сумму и среднее арифметическое.
"""

import math

print("=" * 60)
print("ЗАДАНИЕ 1: Площади геометрических фигур")
print("=" * 60)

def rectangle_area(a, b):
    """Площадь прямоугольника со сторонами a и b."""
    return a * b

def triangle_area(base, height):
    """Площадь треугольника по основанию и высоте."""
    return 0.5 * base * height

def circle_area(radius):
    """Площадь круга по радиусу."""
    return math.pi * radius ** 2

print("Выберите фигуру:")
print("1 - прямоугольник")
print("2 - треугольник (по основанию и высоте)")
print("3 - круг")

choice = int(input("Ваш выбор (1/2/3): "))

if choice == 1:
    a = float(input("Введите длину стороны a: "))
    b = float(input("Введите длину стороны b: "))
    s = rectangle_area(a, b)
    print(f"Площадь прямоугольника = {s:.2f}")
elif choice == 2:
    base = float(input("Введите длину основания: "))
    height = float(input("Введите высоту: "))
    s = triangle_area(base, height)
    print(f"Площадь треугольника = {s:.2f}")
elif choice == 3:
    radius = float(input("Введите радиус: "))
    s = circle_area(radius)
    print(f"Площадь круга = {s:.2f}")
else:
    print("Неверный выбор!")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: Сумма и среднее арифметическое для 3 массивов")
print("=" * 60)

def sum_and_avg(arr):
    """Возвращает сумму и среднее арифметическое списка."""
    total = sum(arr)
    avg = total / len(arr) if len(arr) > 0 else 0
    return total, avg

arrays = []
for i in range(3):
    print(f"\nВвод массива {i+1}:")
    n = int(input("Введите размер массива (не более 15): "))
    if n > 15:
        n = 15
        print("Размер уменьшен до 15.")
    arr = []
    for j in range(n):
        arr.append(int(input(f"Введите элемент {j+1}: ")))
    arrays.append(arr)

for idx, arr in enumerate(arrays, start=1):
    total, avg = sum_and_avg(arr)
    print(f"\nМассив {idx}: {arr}")
    print(f"Сумма элементов = {total}")
    print(f"Среднее арифметическое = {avg:.2f}")