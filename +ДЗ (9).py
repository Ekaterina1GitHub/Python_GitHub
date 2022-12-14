                    # ЗАДАНИЕ 9.1 (ДЗ)
# Условие:
# Ввод с клавиатуры. Если строка введённая с клавиатуры - это числа, то поделить первое на
# второе. Обработать ошибку деления на ноль. Если второе число 0, то программа запрашивает
# ввод чисел заново. Также если были введены буквы, то обработать исключение.

# 1 способ*:
# while True:
#     try:
#         a = str(input("Введите данные: "))
#         b = int(a[0]) / int(a[1])
#         print("Деление: ", b)
#         if int(a[1]) > 0:
#             break
#     except ValueError:
#         print("Вы ввели не число! Нельзя вводить строки!")
#     except ZeroDivisionError:
#         print("ОШИБКА! На 0 делить нельзя!")
#         b = 0
#         print("Результат :", b)

# 2 способ (из презентации):
# while True:
#     a = input("Введите первое число: ")
#     b = input("Введите второе число: ")
#
#     try:
#         result = int(a) / int (b)
#     except ValueError:
#         print("Поддерживаются только числа!")
#     except ZeroDivisionError:
#         print("На ноль делить нельзя!")
#     else:
#         print(result)
#         break
