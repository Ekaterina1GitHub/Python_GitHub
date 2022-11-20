                    # РАЗБОР ЗАДАНИЙ
                    # 2-ОГО ЭКЗАМЕНА

                    # ЗАДАНИЕ 1
# Условие:
# Добавьте на свой рабочий стол папку, в ней создайте 3 текстовых файла: test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
# После этого удалите созданную папку.
# Все операции выполнять с помощью встроенных функций библиотеки os.

import os

# os.mkdir(r'C:/Users/Asus/Desktop/tasks_folder')              # 1.1. Cоздание пустой папки на рабочем столе
                                                               # 1.2. Cоздание 3 текстовых файлов в папке
# with open(r'C:/Users/Asus/Desktop/tasks_folder/test_1.txt', 'w') as f1:
#     print(f1)
# with open(r'C:/Users/Asus/Desktop/tasks_folder/test_2.txt', 'w') as f2:
#     print(f2)
# with open(r'C:/Users/Asus/Desktop/tasks_folder/test_3.txt', 'w') as f3:
#     print(f3)

                                                               # 1.3. Переименование файлов
# os.rename(r'C:/Users/Asus/Desktop/tasks_folder/test_1.txt',
#           r'C:/Users/Asus/Desktop/tasks_folder/rename_1.txt')
# os.rename(r'C:/Users/Asus/Desktop/tasks_folder/test_2.txt',
#           r'C:/Users/Asus/Desktop/tasks_folder/rename_2.txt')
# os.rename(r'C:/Users/Asus/Desktop/tasks_folder/test_3.txt',
#           r'C:/Users/Asus/Desktop/tasks_folder/rename_3.txt')

                                                              # 1.4 Удаление файлов и созданной папки
# os.remove(r'C:/Users/Asus/Desktop/tasks_folder/rename_1.txt')
# os.remove(r'C:/Users/Asus/Desktop/tasks_folder/rename_2.txt')
# os.remove(r'C:/Users/Asus/Desktop/tasks_folder/rename_3.txt')
# os.rmdir(r'C:/Users/Asus/Desktop/tasks_folder')


                    # ЗАДАНИЕ 2
# Условие:
# Найти в списке те элементы, значение которых меньше среднего арифметического, взятого от всех элементов списка.

# from random import randint
#
# a = [randint(0, 99) for i in range(10)]
# b = sum(a)/len(a)
# print("Список c 10 случайными элементами: ", a)
# print("Среднее арифметическое значение, взятое от всех элементов списка: ", b)
# print("Элементы, значение которых меньше среднего арифметического: ")
#
# for i in a:
#     if i < b:
#         print(i, end=' ')


                    # ЗАДАНИЕ 3
# Условие:
# Создайте 2 множества:
# - 1. Если они одинаковые: вывести что они равны
# - 2. Если 1 множество полностью состоит из второго: вывести сообщение 'множество 1 состоит из множества2'
# - 3. Если 2 множество полностью состоит из 1: вывести сообщение 'множество 2 состоит из множества 1'
# - 4. Если они пересекаются: вывести элементы в которых они пересекаются.
# - 5. Если не пересекаются: вывести сообщение об этом

# from random import randint
#
# a = []
# b = []
#
# for i in list(range(10)):
#     a.append(randint(1, 10))
#     b.append(randint(1, 10))
#     s1 = set(a)
#     s2 = set(b)
# print("Первое множество: ", s1)
# print("Второе множество: ", s2)

# s1 = {5, 4, 3, 2, 1, 10, 11}
# s2 = {1, 2, 3}
#
# if s1 == s2:
#     print('Множества равны')
# elif s2.issubset(s1):                                         # set.issubset(other) или set <= other - все элементы set принадлежат other.
#     print('Множество 1 состоит из множества 2')
# elif s1.issubset(s2):
#     print('Множество 2 состоит из множества 1')
# if not s1.isdisjoint(s2):                                     # set.isdisjoint(other) - истина, если set и other не имеют общих элементов.
#     print(f'Множества пересекаются: {s1.intersection(s2)}')
# else:
#     print('Множества не пересекаются')


                    # ЗАДАНИЕ 4
# Условие:
# Создайте словарь из строки ' An apple a day keeps the doctor away' следующим образом:
# в качестве ключей возьмите символы строки, а значениями пусть будут числа, соответствующие количеству вхождений
# данной буквы в строку

# a = ' An apple a day keeps the doctor away'
# d = {i: a.count(i) for i in a}
# print(d)


                    # ЗАДАНИЕ 5
# Условие:
# Ввести 10 чисел, данные числа добавить их во множество.

# q = set()     # пустое множество
#
# for i in range(10):
#     a = int(input("Внесите число: "))      # переменная типа int
#     q.add(a)
# print(q, type(q))


                    # ЗАДАНИЕ 6
# Условие:
# Есть словарь песен группы Depeche Mode violator songsdict =
# { 'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30,
# 'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88,'Blue Dress': 4.18, 'Clean': 5.68 }
# 1. Выведите общее время звучания всех песен.
# 2. Создайте список песен, время звучаниях которых больше 5 минут.
# 3. Создайте новый словарь тех песен, в название которых состоит из одного слова.

# songsdict = { 'World in My Eyes': 4.76,
#               'Sweetest Perfection': 5.43,
#               'Personal Jesus': 4.56,
#               'Halo': 4.30,
#               'Waiting for the Night': 6.07,
#               'Enjoy the Silence': 4.6,
#               'Policy of Truth': 4.88,
#               'Blue Dress': 4.18,
#               'Clean': 5.68 }

# 1.                           (Результат п.1: 4.76 + 5.43 + 4.56 + 4.30 + 6.07 + 4.6 + 4.88 + 4.18 + 5.68 = 44.46)
# s = 0    # сумма
# for value in songsdict.values():
#     s += value          # s = s + value
# print("Общее время звучания всех песен: ", s)

# 2.
# a = []      # пустой список
# for key, value in songsdict.items():
#     if value > 5.00:
#         a.append(key)
# print("Список песен, время звучаниях которых больше 5 минут: ", a)

# 3.
# b = {}
# for key in songsdict:
#     if ' ' not in key:
#         b[key] = songsdict[key]
# print('Новый словарь песен, название которых состоит из 1 слова: ', b)


                    # ЗАДАНИЕ 7
# Условие:
# Дана строка. Сохранить в ней только первые вхождения символов, удалив все остальные. Результат вывести в виде кортежа.

# s = input('Введите текст в строку: ')                       # переменная типа str
#
# a = []
# for i in s:
#     if i not in a:
#         a.append(i)
# a = tuple(a)
# print('Первые вхождения символов: ', a, type(a))


                    # ЗАДАНИЕ 8
# Условие:
# Сжать массив, удалив из него все элементы, величина которых находится в интервале [а, b].
# Освободившиеся в конце массива элементы заполнить нулями.

# from random import randint
# a = [randint(1, 99) for i in range(10)]
# print('Исходный массив: ', a)
#
# for i in range(50, 99):
#     if i in a:
#         a.remove(i)
#         a.append(0)
# print('Преобразованный массив: ', a)


                    # ЗАДАНИЕ 9
# Условие:
# Вычислить количество отрицательных элементов под главной диагональю матрицы.

# from random import randint
#
# n = 3
# m = 3
#
# matrix = [[0] * m for i in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = randint(-20, 20)
#         print(matrix[i][j], end=' ')
#     print()
#
# count = 0
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] < 0 and j < i:
#             count += 1
# print('Количество отрицательных элементов под главной диагональю матрицы: ', count)


                    # ЗАДАНИЕ 10
# Условие:
# Найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный
# элементы в сумму не включать.

# a = int(input('Введите начало последовательности: '))
# z = int(input('Введите конец последовательности: '))
#
# s = 0
#
# for i in range(a+1, z):
#     s += i
# print(s)
