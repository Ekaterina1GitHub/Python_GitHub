                    # 19. ВВЕДЕНИЕ В ООП (КЛАССЫ)
                    # 19.1 Пример
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'I am a cat. My name is {self.name}. I am {self.age} years old.')
#
#     def make_sound(self):
#         print('Meow')
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'I am a dog. My name is {self.name}. I am {self.age} years old.')
#
#     def make_sound(self):
#         print('Bark')
#
# cat1 = Cat('Kitty', 2.5)
# dog1 = Dog('Fluffy', 4)
#
# for animal in (cat1, dog1):
#     animal.make_sound()
#     animal.info()
#     animal.make_sound()


                    # 19.2 Пример / Классы и объекты в Python
# Cоздание пустого класса:
# class Human:        # Cинтаксис: class<название класса>:
#     pass            #            <тело класса>


# Создание объекта класса:
# my_human = Human     # Синтаксис: <имя объекта>=<имя класса>()


                    # 19.3 Пример / Список атрибутов класса / объекта можно получить с помощью команды dir()
# print(dir(Human))

                    # 19.4 Пример / Добавление функционала
                                       # __init__ -встроен. атрибуты всегда идут с 2-мя нижними подчёркиваниями
# class Human:                           # (self, name, age) - параметры, которые будут у Класса
#     def __init__(self, name, age):     # self - ссылка на Класс
#         self.name = name               # привязка заданных характеристик к классу Human
#         self.age = age                 # привязка заданных характеристик к классу Human
#                                        # init - встр.атрибут, отвечающий за осн-ую характеристику Класса.
#     def walk(self, km):                # ф-ция гулять
#         if km > 5:
#             return f'Я не могу пройти {km} км'
#         else:
#             return f'Я могу пройти {km} км'
#
# my_human = Human('Ekaterina', 29)
# print(dir(Human))


                    # 19.5 Пример / Статические и динамические поля
# class Car:
#                                 # Статические поля - поля, которые будут заданы  сразу по умолчанию при создании класса
#     defaulf_color = 'Grey'
#     defaulf_weight = 5000
#                                 # Встр. атрибуты содержат 2 __ перед и после своего имени (напр., __init__)
#     def __init__(self, color, model): # слово self - не зарезервир., можно использ-ть любое слово в качестве параметра
#         self.color = color     # Динамические поля - известны во время создания объекта (экземпляра)
#         self.model = model     # Привязываем к Классу цвет и модель  через self.color и self.model
#
#     def turn_on(self):         # м-д turn_on -включена или выключена машина
#         pass                   # Пустым м.б. либо весь Класс, либо отдельная ф-ия в Классе.
#
# print(dir(Car))               # Результат: список со встроенными атрибутами вначале и пользовательскими - в конце.


                    # ЗАДАНИЕ 1 (19.6)
# Условие:
# Создайте Класс Example. В нём пропишите 3 (метода) ф-ии.
# Две переменные задайте статически, две динамически.
# Первая ф-ия: создайте переменную и выведите её
# Вторая ф-ия: верните сумму 2-ух статических переменных.
# Третья ф-ия: верните результат возведения первой динамической переменной во вторую динамическую переменную.
# Создайте объект класса.
# Напечатайте обе ф-ии.
# Напечатайте переменную a.
#
# class Example:                               # Создание Класса Example
#                                              # Статические переменные (2 шт.):
#     a = 3
#     b = 30
#                                              # Динамические переменные (2 шт.):
#     def __init__(self, c, d):
#         self.c = c
#         self.d = d
#
#     def f1(self):                                     # 1-ый м-д(ф-ия)
#         self.e = 3
#         print(self.e)
#
#     def f2(self):                                     # 2-ой м-д(ф-ия)
#         return self.a + self.b
#
#     def f3(self):                                     # 3-ий м-д(ф-ия)
#         return self.c ** self.d
#
# my_example = Example(20, 2)               # Создание объекта класса
# print(my_example.f2())                    # Результат: 3 + 30 = 33
# print(my_example.f3())                    # Результат: 20 ** 2 = 400
# print(my_example.a)                       # Результат: 3
# my_example.f1()

# Проверка:
# my_example1 = Example(10, 2)
# print(my_example1.f3())                    # Результат: 10 ** 2 = 100


                    # ЗАДАНИЕ 2 (19.7)
# Условие:
# Калькулятор.
# Создайте класс, где реализованы ф-ии(м-ды) математических операций.
# А также ф-ия для ввода данных.

# 1 способ*:
# class Calculadora:
#
#     def __init__(self):
#         self.input()
#
#     def input(self):
#         self.a = float(input("Введите первое число вещественного типа: "))  # переменная типа float 1
#         self.b = float(input("Введите второе число вещественного типа: "))  # переменная типа float 2
#
#     def suma(self):
#         return self.a + self.b
#
#     def sustraccion(self):
#         return self.a - self.b
#
#     def multiplicacion(self):
#         return self.a * self.b
#
#     def division_entera(self):
#         return self.a // self.b
#
#     def restro_de_la_division(self):
#         return self.a % self.b
#
#     def exponenciacion(self):
#         return self.a ** self.b
#
#     def division(self):
#         if self.b > 0:
#             return self.a / self.b
#         else:
#             try:
#                  self.a / 0
#             except ZeroDivisionError:
#                 return "На ноль делить нельзя!"                    # Обработка ошибки: деление на ноль
#
# while True:
#     c = str(input("Введите арифметическую операцию (+, -, *, /, //, %, **): "))     # переменная типа string
#
#     my_calculadora = Calculadora()   # если данная запись стоит в цикле, то запрашиваются повторно перем. a и b
#
#     if c == "0":
#         print('Работа программы завершена: Вы ввели 0!')
#         break
#     elif c == '+':
#         print(my_calculadora.suma())
#     elif c == '-':
#         print(my_calculadora.sustraccion())
#     elif c == '*':
#         print(my_calculadora.multiplicacion())
#     elif c == '//':
#         print(my_calculadora.division_entera())
#     elif c == '%':
#         print(my_calculadora.restro_de_la_division())
#     elif c == '**':
#         print(my_calculadora.exponenciacion())
#     elif c == '/':
#         print(my_calculadora.division())

# 2 способ (из презентации):
# class TheExample:
#     def __init__(self):
#         self.func4()
#
#     def func(self):
#         return self.a + self.b
#
#     def func1(self):
#         return self.a - self.b
#
#     def func2(self):
#         return self.a * self.b
#
#     def func3(self):
#         if self.b == 0:
#             return 'error'
#         else:
#             return self.a / self.b
#
#     def func4(self):
#         self.a = int(input('Введите первое число: '))
#         self.b = int(input('Введите второе число: '))
#
# while True:
#     print('+, -, *, /: ')
#     x = input()
#     print('Numbers: ')
#     example = TheExample()
#     if x == '6':
#         break
#     if x == '+':
#         print(example.func())
#     if x == '-':
#         print(example.func1())
#     if x == '*':
#         print(example.func2())
#     if x == '/':
#         print(example.func3())

