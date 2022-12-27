                    # 25. ПОДГОТОВКА К 3-ОМУ ЭКЗАМЕНУ
                    # Задачи к 3-ому экзамену

                    # 1 ЗАДАЧА (25.1)
# Условие:
# Реализовать калькулятор с 4 методами: Сумма, вычитание, умножение, деление. Метод принимает 2 аргумента и
# возвращает результат. Невалидные данные должны быть обработаны.
# *Примечание: валидный калькулятор - сложение цифр

# class Calculator:
#                                                                  # Написание валидатора:
#     def validate_numbers(self, first_number, second_number):     # ф-ия isinstance (возвращает либо True, либо False)
#         is_valid_first_number = isinstance(first_number, int) or isinstance(first_number, float)
#         is_valid_second_number = isinstance(second_number, int) or isinstance(second_number, float)
#         if is_valid_first_number and is_valid_second_number:     # Если 1-ое и 2-ое число валидные:
#             print('Valid')                                       # то вывод сообщения 'Valid'
#         else:                                                    # иначе, если числа невалидные:
#             raise Exception('Not Valid')                         # вызвать исключение с помощью оператора raise
                                                                   # 'Not Valid'
# Для применения м-да def validate_numbers, его нужно прописать в каждый из м-дов

    # def sum(self, first_number, second_number):
    #     self.validate_numbers(first_number, second_number)
    #     return first_number + second_number
    #
    # def diff(self, first_number, second_number):
    #     self.validate_numbers(first_number, second_number)
    #     return first_number - second_number
    #
    # def div(self, first_number, second_number):
    #     self.validate_numbers(first_number, second_number)
    #     if second_number == 0:
    #         return 'ERROR'
    #     else:
    #         return first_number / second_number
    #
    # def mult(self, first_number, second_number):
    #     self.validate_numbers(first_number, second_number)
    #     return first_number * second_number

# Проверка работы валидатора:

# calc = Calculator()                    # Создание экземпляра Класса

# print(calc.sum(1,2))                   # Результат: Valid - данные валидные
#                                        # Результат: 3 = 1 + 2

# print(calc.diff(15,5))                 # Результат: Valid - данные валидные
#                                        # Результат: 10 = 15 - 5

# print(calc.div(10,2))                  # Результат: Valid - данные валидные
#                                        # Результат: 5.0 = 10 / 2

# print(calc.mult(6,8))                  # Результат: Valid - данные валидные
#                                        # Результат: 48 = 6 * 8

# print(calc.div(10,0))                   # Результат: Valid - данные валидные
#                                         # Результат: ERROR

# Проверка:
# print(calc.sum(1,'строка'))             # Результат: raise Exception('Not Valid')
#                                         # Результат: Exception: Not Valid


                    # 2 ЗАДАЧА (25.2)
# Условие:
# Вы идете в путешествие, надо подсчитать сколько у денег у каждого студента.
# Класс студент описан следующим образом:
# class Student:
#   def __init__(self, name, money):
#       self.name = name
#       self.money = money
# Необходимо понять у кого больше всего денег и вернуть его имя. Если у студентов денег поровну вернуть: “all”.

# class Student:
#     def __init__(self, name, money):
#         self.name = name
#         self.money = money
#                                               # Cоздание 3-ёх объектов (3 экземпляра Класса Student) студентов:
# student1 = Student('Ekaterina', 500)
# student2 = Student('Elena', 550)
# student3 = Student('Irina', 500)
#                                              # Cоздание списка студентов:
# students = [student1, student2, student3]    # Список students вкл. в себя экз-ры Класса student1, student2, student3

# 1 способ:
# moneys = []
# for student in students:
#     moneys.append(student.money)           # Обращение к свойству money / получение денег студента
# print(moneys)                              # Результат: [500, 500, 500]

# 2 cпособ:
# moneys = [student1.money, student2.money, student3.money]
# print(moneys)                              # Результат: [500, 500, 500]

# 1 cпособ:
# if moneys[0] == moneys[1] == moneys[2]:
#     print('All')                           # Результат: All

# 2 способ:
# count = moneys.count(moneys[0])            # перем. с кол-вом 1-ого эл-та списка
# if count == len(students):                 # если кол-во цифр 100 (3) = длине списка со студентами (3)
#     print('all')

# 3 способ:
# if max(moneys) == min(moneys):
#     print('All')                           # Результат: All
# else:
#     max_money = 0
#     name_student = ''                      # Без пробела (строка неизм. тип данных)
#     for student in students:               # student содержит имена всех студентов и деньги
#         if student.money > max_money:      # через student можно обращаться к деньгам и к имени
#             max_money = student.money
#             name_student = student.name
#     print(f'Cтудент с наибольшим количеством денег {name_student} ---> {max_money}')


                    # 4 ЗАДАЧА (25.4)
# Условие:
# Создайте класс Students, содержащий поля: фамилия и инициалы, номер группы, успеваемость (массив из пяти элементов).
# Создать класс School: Добавить возможность для добавления студентов в школу; Добавить возможность вывода фамилий
# и номеров групп студентов, имеющих оценки, равные только 5 или 6. Добавить возможность вывода учеников заданной группы
# Добавить возможность вывода учеников претендующих на автомат(средний балл >= 7).

# class Students:                                                # Оценки - список из 5 цифр
#
#     def __init__(self, name, group, progress):
#         self.name = name
#         self.group = group
#         self.progress = progress

    # Чтобы print(school.get_list_of_students()) не выводило: [<__main__.Students object at 0x0000020B80C67F40>,
    # <__main__.Students object at 0x0000020B80C67D00>, <__main__.Students object at 0x0000020B80C67C70>],
    # необходимо добавить метод __repr__(вернёт имя студента):

#     def __repr__(self):
#         return self.name
#
# class School:
#
#     def __init__(self, students):           # Cоздание характеристики
#         self.students = students
#
#                                             # Доб-е студента м-дом add_student в школу:
#     def add_student(self, student):
#         self.students.append(student)       # Доб-е студента в список students
#
#     def get_list_of_students(self):
#         return self.students                # М-д get_list_of_students - будет выводить студентов
#
#     def remove(self, student, group):       # М-д remove - будет удалять ученика / уд-е по имени и группе
#         if student.group == group:          # student.group - у студента есть м-д group
#             self.students.remove(student)
#
#                                             # Выведение имён студентов:
#     def print_names(self):
#         for student in self.students:
#             print(student.name)
#                                             # Вывод учеников группы (вывод имён по группе):
#     def print_group(self, group):
#         st = []
#         for student in self.students:
#             if student.group == group:
#                 st.append(student)
#         return st
#
#     def get_list_automate_students(self, auto_mark=7):              # М-д, выводящий автомат
#         list_automate = []
#         for student in self.students:
#             arifm = sum(student.progress) / len(student.progress)
#             if arifm >= auto_mark:
#                 list_automate.append(student)
#         return list_automate
#
#     def get_list_of_students_with_needed_mark(self, grades):       # Вывод учеников с конкретными оценками:
#         list_student = self.students.copy()                        # Копир-е в пер. list_student списка студентов
#         for student in self.students:
#             for mark in student.progress:
#                 if mark not in grades:
#                     list_student.remove(student)
#                     break
#         return list_student
#
# student1 = Students('Ekaterina', '196 группа', [10, 10, 10, 10, 10])
# student2 = Students('Dmitriy', '187 группа', [5, 5, 5, 5, 5])
# student3 = Students('Victor', '187 группа', [8, 9, 7, 8, 8])
#
# school = School([])
#
# school.add_student(student1)
# school.add_student(student2)
# school.add_student(student3)
#
# print(school.get_list_of_students())                               # Результат: [Ekaterina, Dmitriy, Victor]
# print(school.get_list_automate_students())                         # Результат: [Ekaterina, Victor]
# print(school.get_list_of_students_with_needed_mark([5]))           # Результат: [Dmitriy]
# print(school.print_group('187 группа'))                            # Результат: [Dmitriy, Victor]


                    # 7 ЗАДАЧА (25.7)
# Условие:
# Создать 4 фрукта. Апельсин, яблоко, мандарин, банан. У всех фруктов есть сорт, список витаминов, цена, имя.
# У апельсина, мандарина, банана есть метод очистить. У яблока метод порезать. У банана есть характеристика:
# кол-во калия. Создать 4 объекта фрукта и использовать все доступные методы и характеристики.
# При вызове метода очистить, должно писаться имя фрукта.
# Например:
# apple = Apple('sort', [a, b, c], 120, 'apple')
# apple.clear()
# >> 'apple очищен'

# АПЕЛЬСИН:
# class Orange:                                    # За основу родительского Класса взяли апельсин
#                                                  # у апельсина есть все м-ды, которые есть у др. фруктов
#     def __init__(self, sort, vitamins, price, name):
#         self.sort = sort
#         self.vitamins = vitamins
#         self.price = price
#         self.name = name
#
#     def clear(self):                            # М-д "очистить" для апельсина, мандарина, банана
#         return f'{self.name} is clear'
#
#     def __repr__(self):                        # Внутр.атриб. __repr__ - позволяет вывести сообщение об данном Объекте
#         return f'sort {self.sort}, vitamin {self.vitamins}, price {self.price}, name - {self.name}'

# ЯБЛОКО:
# class Apple(Orange):                           # Класс Apple наследуем от Orange
#
#     def cut(self):                             # М-д "порезать" для яблока
#         return f'{self.name} is cut'

# МАНДАРИН:
# class Tangerine(Orange):
#     pass                                      # Пустой Класс Tangerine, т.к. он такой же, как и Класс Orange

# БАНАН:
# class Banana(Orange):
#
#     def __init__(self, sort, vitamins, price, name, num_of_kalium):
#         super().__init__(sort, vitamins, price, name)
#         self.num_of_kalium = num_of_kalium              # Характеристика кол-во калия для банана
#
#     def __repr__(self):                        # Внутр.атриб. __repr__ - позволяет вывести сообщение об данном Объекте
#         return f'sort {self.sort}, vitamin {self.vitamins}, price {self.price}, name - {self.name}, ' \
#                f'num of kalium {self.num_of_kalium}'
#
#                                                # Cоздание экземпляров (объектов) Класса:
# orange = Orange('Verna', ['a', 'b1', 'c'], 100, 'Orange')
# apple = Apple('Antonovka', ['a', 'b', 'c'], 120, 'Apple')
# tangerine = Tangerine('Klementin', ['a'], 150, 'Tangerine')
# banana = Banana('Baby', ['b', 'b1'], 200, 'Banana', 300)

                                             # Вызов методов:
                                             # М-д очистить (апельсина, мандарина, банана):
# print(orange.clear())                        # Результат: Orange is clear
# print(tangerine.clear())                     # Результат: Tangerine is clear
# print(banana.clear())                        # Результат: Banana is clear
#                                              # М-д порезать (яблоко):
# print(apple.cut())                           # Результат: Apple is cut
#
# print(orange)                             # Результат: sort Verna, vitamin ['a', 'b1', 'c'], price 100, name - Orange
# print(apple)                              # Результат: sort Antonovka, vitamin ['a', 'b', 'c'], price 120, name - Apple
# print(tangerine)                          # Результат: sort Klementin, vitamin ['a'], price 150, name - Tangerine
# print(banana)                             # Результат: sort Baby, vitamin ['b', 'b1'], price 200, name - Banana,
#                                           # num of kalium 300
