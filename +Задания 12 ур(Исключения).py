                    # 12. ИСКЛЮЧЕНИЯ
                    # 12.1. (Пример)
# Самый простейший пример исключения - деление на ноль:
# a = 100 / 0
# print(a)                    # Результат: ZeroDivisionError: division by zero

                    # 12.2.1. (Пример / Конструкция try - except)
try:
    k = 1 / 0                            # в try - указываем, где будет ошибка!
except ZeroDivisionError:
    k = 0                               # в except - указываем, что хотим выводить, если ошибка сработает!

print(k)                     # Результат: 0


                    # 12.2.2. (Пример / Конструкция try - except)
# try:
#     k = 1 / 0                             # в try - указываем, где будет ошибка!
# except ZeroDivisionError:
#     k = 1                                 # в except - указываем, что хотим выводить, если ошибка сработает!
#
# print(k)                     # Результат: 1


                    # 12.2.3. (Пример / Конструкция try - except)
# try:
#     k = 1 / 0                             # в try - указываем, где будет ошибка!
# except ArithmeticError:
#     k = 0                                 # в except - указываем, что хотим выводить, если ошибка сработает!
#
# print(k)                     # Результат: 0


                    # 12.2.4. (Пример / Конструкция try - except)
# my_dict = {"a": 1, "b": 2, "c": 3}
#
# try:
#     value = my_dict["d"]
# except KeyError:
#     print("Ключа не существует!")


                    # 12.2.5. (Пример / Конструкция try - except)
# my_list = [1, 2, 3, 4, 5]
#
# try:
#     my_list[6]                   # обращаемся к 6 индексу в списке
# except IndexError:
#     print("Этого индекса нет в списке!")


                    # 12.2.6. (Пример / Конструкция try - except)
# my_dict = {"a": 1, "b": 2, "c": 3}
#
# try:
#     value = my_dict["d"]
# except IndexError:
#     print("Такого индекса не существует!")
# except KeyError:
#     print("Этого ключа нет в словаре!")
# except:                                        # как else - иначе
#     print("Произошла другая ошибка!")


                    # 12.2.7. (Пример / Конструкция try - except)
# my_dict = {"a": 1, "b": 2, "с": 3}
#
# try:
#     value = my_dict["d"]
# except (IndexError, KeyError):
#     print("Произошла ошибка IndexError или KeyError!")


                    # 12.3. (Пример / Оператор finally)
                    # 12.3.1.
# my_dict = {"a": 1, "b": 2, "c": 3}
#
# try:
#     value = my_dict["d"]
# except KeyError:
#     print("Произошла ошибка KeyError!")
# finally:
#     print("Оператор Finally выполнен!")


                    # 12.3.2.
# my_dict = {"a": 1, "b": 2, "c": 3}
#
# try:
#     value = my_dict["b"]                         # открыли доступ к существующему ключу, поэтому ошибка не возникла!
# except KeyError:
#     print("Произошла ошибка KeyError!")
# finally:
#     print("Оператор Finally выполнен!")          # Результат: Оператор Finally выполнен!


                    # 12.4. (Пример / Else  в try - except)
# my_dict = {"a": 1, "b": 2, "с": 3}
#
# try:
#     value = my_dict["a"]                 # открыли доступ к существующему ключу, поэтому ошибка не возникла!
# except KeyError:
#     print("Произошла ошибка KeyError!")
# else:
#     print("Ошибок не произошло!")       # else выполнится, если блоки try и except не сработают


                    # 12.5. (Пример / Else, finally в try - except)
                    # 12.5.1.
# my_dict = {"a": 1, "b": 2, "с": 3}
#
# try:
#     value = my_dict["a"]
# except KeyError:
#     print("Произошла ошибка KeyError!")
# else:
#     print("Ошибок не произошло!")       # else выполнится, если блоки try и except не сработают
# finally:
#     print("Оператор finally выполнен!")


                    # 12.5.2.
# my_dict = {"a": 1, "b": 2, "с": 3}
#
# try:
#     value = my_dict["d"]
# except KeyError:
#     print("Произошла ошибка KeyError!")
# else:
#     print("Ошибок не произошло!")
# finally:
#     print("Оператор finally выполнен!")


                    # ЗАДАНИЕ 1 (12.6)
# Условие:
# Введите два числа с клавиатуры. Поделите одно на другое.
# Обработайте ошибку деления на ноль, если ошибок нет, то результат деления возвести в квадрат.
# Также используйте оператор finally.

                    # способ 1*:
# a = int(input("Введите первое число: "))                               # переменная типа int 1
# b = int(input("Введите второе число: "))                               # переменная типа int 2
#
# try:
#     c = a / b
#     print("Результат деления: ", c)
# except ZeroDivisionError:
#     print("ОШИБКА! На 0 делить нельзя!")
# else:
#     print("Результат деления в квадрате: ", c**2)
# finally:
#     print("Задание выполнено!")

                    # способ 2 (из презентации):
# try:
#     a = input("Введите первое число: ")
#     b = input("Введите второе число: ")
#     result = int(a)/int(b)
# except ZeroDivisionError:
#     print("Что-то пошло не так...")
# else:
#     print("Результат в квадрате: ", result**2)
# finally:
#     print("Конец!")


                    # ЗАДАНИЕ 2 (12.7)
# Условие:
# Введите два числа с клавиатуры. Поделите одно на другое.
# Обработайте деления на ноль, преобразования и общее исключение.

                    # 1 способ*:
# try:
#     a = int(input("Введите первое число: "))  # переменная типа int 1
#     b = int(input("Введите второе число: "))  # переменная типа int 2
#     c = a / b
#     print("Результат деления: ", c)
# except ZeroDivisionError:                                      # деление на 0
#     print("ОШИБКА! На 0 делить нельзя!")
# except ValueError:                                            # преобразования
#     print("Вы ввели не целое число! Нельзя вводить строки!")
# except Exception:                                             # общее исключение
#     print("Любая ошибка!")


                    # 2 способ (из презентации):
# try:
#     number1 = int(input("Введите первое число: "))
#     number2 = int(input("Введите второе число: "))
#     print("Результат деления: ", number1 / number2)
# except ValueError:
#     print("Преобразование прошло неудачно")
# except ZeroDivisionError:
#     print("Попытка деления числа на ноль")
# except Exception:
#     print("Общее исключение")
# print("Завершение программы")
