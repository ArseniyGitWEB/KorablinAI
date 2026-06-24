python
# -*- coding: utf-8 -*-
"""
Задание 1.
Даны два целых числа A и B (A ≤ B). Выведите все числа от A до B включительно.
"""

A = int(input())
B = int(input())

for i in range(A, B + 1):
    print(i)


