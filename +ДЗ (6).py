                     # ЗАДАНИЕ 6.1 (ДЗ)
# Условие:
# Дан список list = [15, 48, 'hello', 6, 19, 'world']
# Все числа этого списка проверить на чётность.
# Если число чётное, то посчитать сумму его цифр.
# Если нечётное, то заменить его на 1 в списке.
# Все слова: посчитать кол-во гласных и согласных.
# Вывести всё на экран.

# list = [15, 48, 'hello', 6, 19, 'world']
        # 1
# S = 0                     # сумма
# C = list.copy()           # копия списка list, в котором будет производиться замена нечётных цифр.
# print("Исходный список: ", C, '\n')
        # 2
# Glasnie = 0
# Soglasnie = 0

# for i in list:
#     if type(i) is int and i % 2 == 0:
#         print('Число чётное:', i)
#         i = str(i)
#         for w in i:
#             w = int(w)
#             S = S + w
#             # **print("Сумма цифр чётных чисел: ", S) -  в конце!
#     else:
#         if type(i) is int and i % 2 != 0:
#             print('Число нечётное: ', i)
#             C1 = C.index(i)
#             C[C1] = 1
#             # **print("Замена нечётного числа на 1: ", C)  -  в конце!
#         else:
#             if type(i) is str:
#                 for y in i:
#                     if y == "a" or y == 'u' or y == 'o' or y == 'i' or y == 'e' or y == 'y':
#                         print("Гласная буква: ", y)
#                         Glasnie = Glasnie + 1
#                         # *print("Количество всех гласных букв: ", Glasnie)  -  в конце!
#                     else:
#                         if y == 'h' or y == 'l' or y == 'w' or y == 'r' or y == 'l' or y == 'd':
#                             print("Согласная буква :", y)
#                             Soglasnie = Soglasnie + 1
#                             # *print("Количество согласных букв: ", Soglasnie)  -  в конце!
#
# print("Сумма цифр чётных чисел: ", S)
# print("Замена всех нечётных чисел на 1: ", C)
# print("Количество всех гласных букв: ", Glasnie)
# print("Количество всех согласных букв: ", Soglasnie)


                    # 2 способ (из презентации):
# list = [15, 48, 'hello', 6, 19, 'world']
# l = 0
# h = 0
# d = 0
#
# for i in list:
#     if type(i) is int:
#         if i % 2 == 0:
#             i = str(i)
#             for k in i:
#                 k = int(k)
#                 l += k
#             print(i, "Сумма цифр: ", l, "\n")
#         else:
#             index = list.index(i)
#             list[index] = 1
#     elif type(i) is str:
#         for r in i:
#             if r in "aeoiu":
#                 h += 1
#             else:
#                 d += 1
#         print(i, '\n', 'Количество гласных: ', h)

