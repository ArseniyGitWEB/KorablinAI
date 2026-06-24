python
# -*- coding: utf-8 -*-
"""
Вариант 1.
Дана строка, содержащая русскоязычный текст.
Найти количество слов, начинающихся с буквы "е".
"""

s = input("Введите строку: ")

words = s.split()
count = 0

for word in words:
    clean_word = word.strip('.,!?;:()"\'')
    if clean_word.lower().startswith('е'):
        count += 1

print("Количество слов, начинающихся с 'е':", count)



