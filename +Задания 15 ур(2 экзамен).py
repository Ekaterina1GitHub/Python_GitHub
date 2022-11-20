                    # 2-ОЙ ЭКЗАМЕН
                    # ЗАДАНИЕ 1
# Условие:
# Добавьте на свой рабочий стол папку, в ней создайте 3 текстовых файла: test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
# После этого удалите созданную папку.
# Все операции выполнять с помощью встроенных функций библиотеки os.

# 1 способ:
# import os
#                                                   # 1.1. Cоздание пустой папки 'ЭКЗАМЕН 2' на рабочем столе
# os.chdir('C:\\Users\\Asus\\Desktop')
# print("Текущая директория: ", os.getcwd())
# os.mkdir('ЭКЗАМЕН 2')
                                                    # 1.2. Cоздание 3 текстовых файла в папке 'ЭКЗАМЕН 2'
# os.chdir('ЭКЗАМЕН 2')
# print('Текущая директория: ', os.getcwd())
# f1 = open('test_1.txt', 'w')
# f2 = open('test_2.txt', 'w')
# f3 = open('test_3.txt', 'w')
# f1.write('Задание 1, создание файла test_1.txt  с последующим переименованием его на rename_1.txt')
# f2.write('Задание 1, создание файла test_2.txt  с последующим переименованием его на rename_2.txt')
# f3.write('Задание 1, создание файла test_3.txt  с последующим переименованием его на rename_3.txt')
# f1.close()
# f2.close()
# f3.close()
                                                          # 1.3. Переименование файлов
# os.rename('test_1.txt','rename_1.txt')                    # переименов. файла с test_1.txt на rename_1.txt
# os.rename('test_2.txt','rename_2.txt')                    # переименов. файла с test_2.txt на rename_2.txt
# os.rename('test_3.txt','rename_3.txt')                    # переименов. файла с test_3.txt.txt на rename_3.txt

                                                           # 1.4 Удаление файлов
# try:
#     os.rmdir('C:\\Users\\Asus\\Desktop\\ЭКЗАМЕН 2')        # удалить папку 'ЭКЗАМЕН 2'
# except OSError:
#     os.remove('rename_1.txt')
#     os.remove('rename_2.txt')
#     os.remove('rename_3.txt')
                                                          # 1.5 Удаление папки с рабочего стола
# os.chdir('C:\\Users\\Asus\\Desktop')
# print('Текущая директория: ', os.getcwd())
# os.rmdir('C:\\Users\\Asus\\Desktop\\ЭКЗАМЕН 2')


# 2 способ:

import os
# os.mkdir('C:\\Users\\Asus\\Desktop\\ЭКЗАМЕН 2')              # 1.1. Cоздание пустой папки 'ЭКЗАМЕН 2' на рабочем столе

                                                               # 1.2. Cоздание 3 текстовых файла в папке 'ЭКЗАМЕН 2'
# f1 = open('C:\\Users\\Asus\\Desktop\\ЭКЗАМЕН 2\\test_1.txt', 'w')
# f2 = open('C:\\Users\\Asus\\Desktop\\ЭКЗАМЕН 2\\test_2.txt', 'w')
# f3 = open('C:\\Users\\Asus\\Desktop\\ЭКЗАМЕН 2\\test_3.txt', 'w')
# f1.close()
# f2.close()
# f3.close()

                                                               # 1.3. Переименование файлов
# os.rename('C:\\Users\\Asus\\Desktop\\ЭКЗАМЕН 2\\test_1.txt', 'C:\\Users\\Asus\\Desktop\\ЭКЗАМЕН 2\\rename_1.txt')
# os.rename('C:\\Users\\Asus\\Desktop\\ЭКЗАМЕН 2\\test_2.txt', 'C:\\Users\\Asus\\Desktop\\ЭКЗАМЕН 2\\rename_2.txt')
# os.rename('C:\\Users\\Asus\\Desktop\\ЭКЗАМЕН 2\\test_3.txt', 'C:\\Users\\Asus\\Desktop\\ЭКЗАМЕН 2\\rename_3.txt')

                                                              # 1.4 Удаление файлов и созданной папки
# os.remove('C:\\Users\\Asus\\Desktop\\ЭКЗАМЕН 2\\rename_1.txt')
# os.remove('C:\\Users\\Asus\\Desktop\\ЭКЗАМЕН 2\\rename_2.txt')
# os.remove('C:\\Users\\Asus\\Desktop\\ЭКЗАМЕН 2\\rename_3.txt')
# os.rmdir('C:\\Users\\Asus\\Desktop\\ЭКЗАМЕН 2')

                    # ЗАДАНИЕ 2
# Условие:
# Найти в списке те элементы, значение которых меньше среднего арифметического, взятого от всех элементов списка.

# 1 способ:
# import random
#
# c = [random.randint(0, 100) for i in range(10)]
# d = sum(c) / len(c)
# e = [ ]
#
# for i in c:
#     if i < d:
#         e.append(i)
#
# print("Список c 10 случайными элементами: ", c)
# print("Среднее арифметическое значение, взятое от всех элементов списка: ", d)
# print("Элементы, значение которых меньше среднего арифметического: ", e)

# 2 способ (через ф-ию mean()):
# import random
# import statistics         # м-ль статистики исп-ся для вып. всех стат. операций с данными.
#
# c = [random.randint(0, 100) for i in range(10)]
# o = statistics.mean(c)    # ф-ия mean() помогает вычислить ср. знач. набора значений, переданных в ф-ию.
#                           # ф-ия statistics.mean() принимает значения данных в кач-ве аргумента и возвращает ср. знач-е
#                           # переданных ей значений.
# e = []
# for i in c:
#     if i < o:
#         e.append(i)
#
# print("Список c 10 случайными элементами: ", c)
# print("Среднее арифметическое значение, взятое от всех элементов списка: ", o)
# print("Элементы, значение которых меньше среднего арифметического:", e)


                    # ЗАДАНИЕ 3
# Условие:
# Создайте 2 множества:
# - 1. Если они одинаковые: вывести что они равны
# - 2. Если 1 множество полностью состоит из второго: вывести сообщение 'множество 1 состоит из множества2'
# - 3. Если 2 множество полностью состоит из 1: вывести сообщение 'множество 2 состоит из множества 1'
# - 4. Если они пересекаются: вывести элементы в которых они пересекаются.
# - 5. Если не пересекаются: вывести сообщение об этом

# 1. Создание множества через модуль random
# import random
# a = set([random.randint(0, 8) for k1 in range(5)])
# print("Первое множество: ", a, type(a))
#
# b = set([random.randint(0, 8) for k2 in range(5)])
# print("Второе множество: ", b, type(b))

# 2. Создание множества через литерал {}:
# a = {5, 4, 3, 2, 1, 10, 11}
# print("Первое множество: ", a, type(a))
#
# b = {1, 2, 3}
# print("Второе множество: ", b, type(b))

                                            # 1.
# if a == b:
#     print('Множества равны: ', a, '=', b)
# else:                                       # 2. (1 способ решения)
#     if a >= b:
#         print(a >= b, ':', 'Множество 1 состоит из множества 2')
#                                             # 2. (2 способ решения)
#     if a.issuperset(b):                           # issuperset()-определяет, есть ли текущее множество надмнож. над др.
#         print(a.issuperset(b), ':', 'Множество 1 состоит из множества 2')
#     else:                                   # 3. (1 способ решения)
#         if a <= b:
#             print(a <= b, ':', 'Множество 2 состоит из множества 1')
#         if b.issuperset(a):                 # 3. (2 способ решения)
#             print(b.issuperset(a), ':', 'Множество 2 состоит из множества 1')
#
#
# if a & b:                                         # 4. (1 способ решения)
#     print("Пересечение: ", a & b)
# if a.intersection(b):                            # 4. (2 способ решения)
#     print("Пересечение: ", a.intersection(b))
# else:
#     print("Элементы 1 и 2 множества не пересекаются!")


                    # ЗАДАНИЕ 4
# Условие:
# Создайте словарь из строки ' An apple a day keeps the doctor away' следующим образом:
# в качестве ключей возьмите символы строки, а значениями пусть будут числа, соответствующие количеству вхождений
# данной буквы в строку

                    # 1 способ:
# a = ' An apple a day keeps the doctor away'
# a1 = ''.join(a.split(' '))                    # убрали все пробелы в строке
#
# b = {i: a1.count(i) for i in a1}
# print(b, type(b))

                    # 2 способ (через модуль collections):
# from collections import Counter               # collections.Counter - вид словаря, который позволяет считать кол-во
# b = ' An apple a day keeps the doctor away'   # неизменяемых объектов (в большинстве случаев, строк).
# b1 = ''.join(b.split(' '))
#
# c = Counter(b1)
# c = dict(c)
# print(c, type(c))

                    # ЗАДАНИЕ 5
# Условие:
# Ввести 10 чисел, данные числа добавить их во множество.

# 1 cпособ:
# n = 0                  # количество
# b = set([])            # пустое множество
#
# while n < 10:
#     a = int(input("Внесите число: "))      # переменная типа int
#     n += 1                                 # n = n + 1
#     b.add(a)
# print(b, type(b))

# 2 cпособ:
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
# 1 способ:
# time_s = songsdict['World in My Eyes'] + songsdict['Sweetest Perfection'] + songsdict['Personal Jesus'] + \
#          songsdict['Halo'] + songsdict['Waiting for the Night'] + songsdict['Enjoy the Silence'] + \
#          songsdict['Policy of Truth'] + songsdict['Blue Dress'] + songsdict['Clean']
# print("Общее время звучания всех песен: ", time_s)

# 2 способ:
# s = 0    # сумма
# for i1 in songsdict.values():
#     s += i1          # s = s + i1
# print("Общее время звучания всех песен: ", s)


# 2.
# a = []      # пустой список
# for i in songsdict:
#     if songsdict[i] > 5.00:
#         a.append(i)
# print("Список песен, время звучаниях которых больше 5 минут: ", a)

# 3.
# b = {i3: songsdict[i3] for i3 in songsdict.keys() if not ' ' in i3}
# print('Новый словарь песен, название которых состоит из 1 слова: ', b)


                    # ЗАДАНИЕ 7
# Условие:
# Дана строка. Сохранить в ней только первые вхождения символов, удалив все остальные. Результат вывести в виде кортежа.

# 1 способ:
# s = input('Введите текст в строку: ')                      # переменная типа str
#
# s1 = [v for i, v in enumerate(s) if v not in s[:i]]        # выведение первых вхождений символов
# s1 = tuple(s1)                                             # ф-ия enumerate()-позв. получить индекс эл-та и его значение.
# print('Первые вхождения символов: ', s1, type(s1))

# 2 способ:
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

# 1 cпособ:

# import random
# arr = [random.randint(0, 99) for i in range(15)]
# print('Исходный массив: ', arr)

# a = int(input('Введите нижнюю границу a удаляемого диапазона: '))
# b = int(input('Введите верхнюю границу b удаляемого диапазона: '))
#
#
# for y in range(a, b+1):
#     if y in arr:
#         arr.remove(y)
#         arr.append(0)
# print('Преобразованный массив: ', arr)

# 2 cпособ:
# from random import random
# N = 10
# arr = []
# a = int(input('Нижняя граница массива: '))
# b = int(input('Верхняя граница массива: '))
# for i in range(N):
#     n = int(random()*(b-a)) + a
#     arr.append(n)
# print('Массив:', arr)
# print('Удаляемый диапазон: ')
# a = int(input('Нижняя граница: '))
# b = int(input('Верхняя граница: '))
# i = 0
# m = N
# while i < m:
#     if a <= arr[i] <= b:
#         del arr[i]
#         m -= 1
#     else:
#         i += 1
# for i in range(m, N):
#     arr.append(0)
# print('Преобразованный массив:', arr)


                    # ЗАДАНИЕ 9
# Условие:
# Вычислить количество отрицательных элементов под главной диагональю матрицы.

# import random
# from itertools import islice
#
# N = int(input('Введите количество строк в матрице, равное количеству столбцов (матрица квадратная): '))
# M = N        # создадим квадратную матрицу, в которой M=N (N - строки, M - столбцы).
#
# c = []                                                # пустой список для добавления всех элементов, входящих в матрицу
# print('КВАДРАТНАЯ МАТРИЦА: ')
# for i in range(N):
#     for y in range(M):
#         a = random.randint(-50, 50)
#         c.append(a)
#         print(a, end='\t')
#     print()

# print('Выведение всех элементов заданной матрицы в списке: ', c)
#
# d = []                                             # пустой список
# for l in range(N):
#     d.append(N)
# print('Заготовка для созд. влож. списков: ', d)       # действие, для подготовки создания 4 вложенных списков в списке.
# e = iter(c)   # ф-ия iter()- возвращ. итератор и создаёт объект, кот. может повторяться по 1 элементу за раз.
# f = [list(islice(e, elem)) for elem in d]
# print('Список (Кол-во влож.списков=M=N):', f)
                           # Главная диагональ квадратной матрицы проходит из левого верхнего угла в правый нижний угол.
# count = 0                                                   # кол-во отриц. эл-тов под гл. диагональю матрицы
# for z in range(N):
#     for z2 in range(N):                                     # усл.:  f[z][z2] < 0 ( выводит 0 по всей матрице)
#         if f[z][z2] < 0 and z2 < z:                         # усл.: z2 < z (эл-ты лежат ниже гл. диагонали)
#             count += 1                                      # count = count + 1
# print('Количество отрицательных элементов под главной диагональю матрицы: ', count)


                    # ЗАДАНИЕ 10
# Условие:
# Найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный
# элементы в сумму не включать.

                                                        # Пусть элементы будут расположены в списке
# import random
# a = [random.randint(0, 25) for i in range(10)]
# a1 = min(a)    # минимальный элемент
# a2 = max(a)    # максимальный элемент
# print('Список: ', a)
# print('Min:', a1)
# print('Max:', a2)
#
# s = 0
# c = []
# for y in range(a1+1, a2):
#     s += y     # s = s + y
#     c.append(y)
# print('Список с элементами, находящимися между min и max элементами: ', c)
# print('Cумма элементов, находящихся между min и max элементами: ', s)
