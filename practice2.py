python
# -*- coding: utf-8 -*-
"""
Практика №2, задача 1.
Вычислить значение выражения:
s = (2*cos(x - 2/3) / (1/2 + sin^2(y))) * (1 + z^2 / (3 - z^2/5))
где x=14.26, y=-1.22, z=3.5e-2
Ожидаемый ответ: 0.749155
"""

import math

x = 14.26
y = -1.22
z = 3.5e-2   # 3.5 * 10^(-2)

cos_x = math.cos(x - 2/3)
sin_y = math.sin(y)
sin2_y = sin_y ** 2
denominator = 0.5 + sin2_y

first_part = (2 * cos_x) / denominator

z2 = z ** 2
second_part = 1 + z2 / (3 - z2 / 5)

s = first_part * second_part


print(f"s = {s:.6f}")