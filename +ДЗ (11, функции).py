                    # ЗАДАНИЕ 11.1 (ДЗ)
# Условие:
# Простейший калькулятор с введёнными 2-мя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и 2 числа. Операции являются функциями.
# Обработать ошибку: "Деление на ноль"
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).

# 1 cпособ*:
# def calculadora():
#     while True:
#         a = float(input("Введите первое число вещественного типа: "))                   # переменная типа float 1
#         b = float(input("Введите второе число вещественного типа: "))                   # переменная типа float 2
#         c = str(input("Введите арифметическую операцию (+, -, *, /, //, %, **): "))     # переменная типа string
#
#         if c == "0":
#             break                      # завершение программы
#         elif c == '+':
#             print(a + b)               # операция сложения (+)
#         elif c == '-':
#             print(a - b)               # операция вычитания (-)
#         elif c == '*':
#             print(a * b)               # операция умножения (*)
#         elif c == "//":
#             print(a // b)              # операция деления нацело (//)
#         elif c == "%":
#             print(a % b)               # операция остаток от деления (%)
#         elif c == "**":
#             print(a ** b)              # операция возведение в степень b числа a (**)
#         else:
#             if c == "/" and b > 0:     # операция деления (/)
#                 print(a / b)
#             else:
#                 try:
#                     a / 0
#                 except ZeroDivisionError:
#                     print("На ноль делить нельзя!")      # Обработка ошибки: деление на ноль
#
# calculadora()

# 2 cпособ:
# def suma(): return a + b
# def sustraccion(): return a - b
# def multiplicacion(): return a * b
# def division_entera(): return a // b
# def restro_de_la_division(): return a % b
# def exponenciacion(): return a ** b
# def division(): return a / b
#
# while True:
#     a = float(input("Введите первое число вещественного типа: "))                   # переменная типа float 1
#     b = float(input("Введите второе число вещественного типа: "))                   # переменная типа float 2
#     c = str(input("Введите арифметическую операцию (+, -, *, /, //, %, **): "))     # переменная типа string
#
#     if c == "0":
#         break
#     elif c == '+':
#         print(suma())
#     elif c == '-':
#         print(sustraccion())
#     elif c == '*':
#         print(multiplicacion())
#     elif c == '//':
#         print(division_entera())
#     elif c == '%':
#         print(restro_de_la_division())
#     elif c == '**':
#         print(exponenciacion())
#     else:
#         if c == '/' and b > 0:
#             print(division())
#         else:
#             try:
#                  a / 0
#             except ZeroDivisionError:
#                 print("На ноль делить нельзя!")      # Обработка ошибки: деление на ноль

# 3 cпособ (из презентации):
# print('two numbers: ')
# a = float(input('1: '))
# b = float(input('2: '))
# print('+', '-', '*', '/', '0-exit')
# print('operator: ')
#
# def plus(a, b):
#     return a + b
#
# def minus(a, b):
#     return a - b
#
# def proisv(a, b):
#     return a * b
#
# def delen(a, b):
#     if b == 0:
#         return 'error'
#     else:
#         return a / b
#
# while True:                                   # все арифметич.операции - выводятся через цикл / перем. a и b - вне цикла
#     x = input()
#     if x == '0':
#         break
#     else:
#         if x == '+':
#             print('result: ', plus(a, b))
#         if x == '-':
#             print('result: ', minus(a, b))
#         if x == '*':
#             print('result: ', proisv(a, b))
#         if x == '/':
#             print('result: ', delen(a, b))
#         print('operator: ')