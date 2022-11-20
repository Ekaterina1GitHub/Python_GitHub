                    # 16. РЕШЕНИЕ ЗАДАЧ
                    # ЗАДАНИЕ 16.1
# Условие:
# Пользователь вводит два числа с клавиатуры. Вывести на экран yes, если они отличаются друг от друга на 135,
# иначе вывести на экран No;

# a = int(input("Введите первое число: "))    # переменная типа int 1
# b = int(input("Введите второе число: "))    # переменная типа int 2
#
# c1 = abs(a - b)                             # ф-ия abs() - встр. ф-ия, возвращающая абсолютное значение числа.
# c2 = abs(b - a)
# if c1 == 135 or c2 == 135:
#     print("Yes")
# else:
#     print("No")


                    # ЗАДАНИЕ 16.2 (79)
# Условие:
# Дано число. Если оно больше 100 или меньше -100 , то вывести на экран символ — , иначе вывести на экран символ +;

                                              # пер. a - зад. вручную либо через random
# a = int(input("Введите число: "))           # переменная типа int 1
# либо
# import random
# a = random.randint(-999, 999)
# print('Рандомное число: ', a)

# if a > 100 or a < -100:
#     print('—')
# else:
#     print('+')


                    # ЗАДАНИЕ 16.3 (80)
# Условие:
# Пользователь вводит три числа. Если все числа больше 10, то вывести на экран yes , иначе no.

# a1 = int(input("Введите первое число: "))         # переменная типа int 1
# a2 = int(input("Введите второе число: "))         # переменная типа int 2
# a3 = int(input("Введите третье число: "))         # переменная типа int 3
#
# if a1 > 10 and a2 > 10 and a3 > 10:
#     print('Yes')
# else:
#     print('No')


                    # ЗАДАНИЕ 16.4 (81)
# Условие:
# Дано три числа. Найти количество положительных чисел среди них.
# *Примечание: 0 - положит. число в Python

# a1 = int(input("Введите первое число: "))       # переменная типа int 1
# a2 = int(input("Введите второе число: "))       # переменная типа int 2
# a3 = int(input("Введите третье число: "))       # переменная типа int 3
#
#
# p = []                                          # список для положительных чисел
# if a1 >= 0:
#     p.append(a1)
# if a2 >= 0:
#     p.append(a2)
# if a3 >= 0:
#     p.append(a3)
# else:
#     if a1 < 0:
#         print('Число отрицательное: ', a1)
#     if a2 < 0:
#         print('Число отрицательное: ', a2)
#     if a3 < 0:
#         print('Число отрицательное: ', a3)
#
# print('Список положительных чисел: ', p)
# print('Количество положительных чисел из 3-ёх введённых: ', len(p))


                    # ЗАДАНИЕ 16.5
# Условие:
# Напишите программу, которая считывает целые числа с консоли по одному числу в строке.
# Для каждого введённого числа проверить: если число меньше 10, то пропускаем это число;
#  если число больше 100, то прекращаем считывать числа; в остальных случаях вывести это число обратно на консоль
#  в отдельной строке.

# while True:
#     a = int(input('Введите целое число: '))     # переменная типа int 1
#     if a < 10:
#         continue
#     if a > 100:
#         break
#     else:
#         print('Выведение целого числа: ', a)


                    # ЗАДАНИЕ 16.6
# Условие:
# В списке, содержащем положительные и отрицательные целые числа, вычислите сумму чётных положительных элементов.

# import random
# a = [random.randint(-100, 100) for i in range(10)]
# print('Список, содержащий положительные и отрицательные целые числа: ', a)
#
# b = []                                # список для доб-я чётных положительных элементов
# for i in a:
#     if i % 2 == 0 and i >= 0:
#         b.append(i)
# print('Список чётных положительных элементов: ', b)

                    #1-ый способ нахождения суммы:
# s = 0                                  # сумма
# for y in b:
#     s += y        # s = s + y
# print('Cумма чётных положительных элементов: ', s)

                    # 2-ой способ нахождения суммы:
# v = sum(b)
# print('Cумма чётных положительных элементов: ', v)


                    # ЗАДАНИЕ 16.6
# Условие:
# Напишите программу, которая считывает с клавиатуры два числа a и b, считает и выводит на консоль среднее
# арифметическое всех чисел из отрезка [a;b], которые кратны числу 3. В приведенном ниже примере среднее
# арифметическое считается для чисел на отрезке [−5;12]. Всего чисел, делящихся на 3, на этом отрезке 6:
# − 3 , 0 , 3 , 6 , 9 , 12. Их среднее арифметическое равно 4.5.

# a = int(input("Начало отрезка: "))    # переменная типа int 1
# b = int(input("Конец отрезка: "))    # переменная типа int 2
#
# c = []
# for i in range(a, b+1):
#     if i % 3 == 0:
#         c.append(i)
# print('Числа отрезка, кратные 3: ', c)
#                     #1-ый способ нахождения среднего арифметического:
# d = sum(c) / len(c)
# print('Cреднее арифметическое всех чисел из отрезка, которые кратны числу 3: ', d)
#                     # 2-ой способ нахождения среднего арифметического:
# import statistics
# o = statistics.mean(c)
# print('Cреднее арифметическое всех чисел из отрезка, которые кратны числу 3: ', o)


                    # ЗАДАНИЕ 16.7
# Условие:
# Сложите цифры целого семизначного числа.

# import random
#
# a = random.randint(1000000, 9000000)
# print('Целое семизначное число: ', a)
#
# num_1 = a // 1000000
# num_2 = (a//100000) % 10
# num_3 = (a//10000) % 10
# num_4 = (a//1000) % 10
# num_5 = (a//100) % 10
# num_6 = (a//10) % 10
# num_7 = a % 10
# print('Сумма цифр целого 7-значного числа: ', num_1 + num_2 + num_3 + num_4 + num_5 + num_6 + num_7)


                    # ЗАДАНИЕ 16.8
# Условие:
# Ввести строку. Если длина строки больше  или равна 10 символов, то создать новую строку с 3 восклицательными
# знаками в конце  ('!!!') и вывести на экран. Если меньше 10, то вывести на экран второй символ строки.

# a = input('Введите текст: ')         # переменная типа str
#
# if len(a) >= 10:
#     print(a, '!!!')
# else:
#     print(a[1])


                    # ЗАДАНИЕ 16.9 (4)
# Условие:
# Создать строку, разделить ее на элементы списка, и вывести все элементы данного списка, но так чтобы к данным
# элементам на концах был !

# a = input('Введите текст в строку: ')         # переменная типа str
#
# print('! '. join(a.split(' ')) + '!')


                    # ЗАДАНИЕ 16.10 (6)
# Условие:
# Есть список слов(строки) добавить на конец к ним слово _world и перевести в строку по запятой.
#
# a = input('Введите слова в строку через ",": ')        # переменная типа string
# print('Строка: ', a)
# b = a.split(',')
# print('Список: ', b)
#
# c = []                                               # список для доб-я слова _world на конец каждой строки
# for i in b:
#     c.append(i + '_world')
# print('Список с добавленным на конец каждой строки словом "_world": ', c)
#
# d = ','.join(c)                                     # преобразование списка в строку
# print('Перевод списка в строку по запятой: ', d)


                    # ЗАДАНИЕ 16.11 (7)
# Условие:
# Cоздать список чисел(рандомных количеством 10 штук), в новый список добавть нечетные элементы

# import random
# a = [random.randint(-100, 100) for i in range(10)]
# print('Список, содержащий положительные и отрицательные целые числа: ', a)
#
# b = []                                # список для доб-я нечетных элементов
# for i in a:
#     if i % 2 != 0:
#         b.append(i)
# print('Список c нечётными элементами: ', b)


                    # ЗАДАНИЕ 16.12 (8)
# Условие:
# Cоздать список из элементов в диапазоне от 50 до 70 и вывести только те, которые больше 65,
# вывод необходимо реализовать в кортеже

                    # 1-ый способ создния списка элементов диапазоне от 50 до 70:
# import random
# a = [random.randint(50, 70) for i in range(20)]      # список из элементов в диапазоне от 50 до 70
# print('Список из элементов в диапазоне от 50 до 70: ', a)
#
                     # 2-ой способ создния списка элементов диапазоне от 50 до 70:
# a = [i for i in range(50, 71)]
# print('Список из элементов в диапазоне от 50 до 70: ', a)

# b = []
# for y in a:
#     if y > 65:
#         b.append(y)
# b = tuple(b)
# print('Кортеж с элементами, значения которых больше 65: ', b, type(b))

