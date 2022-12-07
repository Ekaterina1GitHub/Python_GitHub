                    # 20. ВВЕДЕНИЕ В ООП (КЛАССЫ). Часть 2.
                    # 20.1 Пример / Метод str
# class Car:
#
#     # создание методов класса
#     def start(self):
#         print('Двигатель заведён')
#
# car_a = Car()
# print(car_a)                                             # Результат: <__main__.Car object at 0x000002AEC418B910>


                    # 20.2 Пример / Метод str
# class Car:
#
#     # создание методов класса
#     def __str__(self):
#         return 'Car class Object'
#
#     def start(self):
#         print('Двигатель заведён')
#
# car_a = Car()
# print(car_a)                                           # Результат: Car class Object
                                                         # М-д start не выводится, т.к. нигде его не вызываем.

                    # 20.3 Пример / Методы экземпляра Класса
# class Phone:
#
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model
#
#     # Обычный м-д
#     # Первый параметр м-да - self
#     def check_sim(self, mobile_operator):
#         if self.model == 'I785' and mobile_operator == 'MTS':
#             print('Your mobile operator is MTS')
#
#
# my_phone = Phone('red', 'I785')
# my_phone.check_sim('MTS')                         # Результат: Your mobile operator is MTS


                    # 20.4 Пример / Cтатические методы Класса
# 20.4.1.
# class Phone:
#     @staticmethod                            # @staticmethod  - 1 из встроенных декораторов
#     def model_hash(model):
#         if model == 'I785':
#             return 34565
#         elif model == 'K498':
#             return 45567
#         else:
#             return None
#                                 # Cтатические м-ды вызываются через имя Класса, а обычные м-ды - через экземпляр Класса
# print(Phone.model_hash('I785'))               # Результат: 34565

# 20.4.2 (п. 20.3 + п. 20.4.1).
# class Phone:
#
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model
#
#     # Обычный м-д
#     # Первый параметр м-да - self
#     def check_sim(self, mobile_operator):
#         if self.model == 'I785' and mobile_operator == 'MTS':
#             print('Your mobile operator is MTS')
#
#                         # Статический м-д справочного хар-ра
#                         # Возвращает hash по номеру модели
#                         # self внутри м-да отсутствует
#     @staticmethod
#     def model_hash(model):
#         if model == 'I785':                     # @staticmethod  - 1 из встроенных декораторов
#             return 34565
#         elif model == 'K498':
#             return 45567
#         else:
#             return None
#                                               # Cтатические м-ды вызываются через имя Класса,
#                                               # Обычные м-ды вызываются через экземпляр Класса
# print(Phone.model_hash('I785'))   # Cтатический м-д / Результат: 34565
#
# my_phone = Phone('red', 'I785')   # Обычный м-д
# my_phone.check_sim('MTS')         # Обычный м-д /  Результат: Your mobile operator is MTS


                    # 20.5 Пример / Уровни доступа атрибутов в Python (Private)
# class H:
#
#     def __init__(self):
#         self.__money = 100       # задали значение ф-ии
#                                  # __money - приватный атрибут
#     def print_money(self):
#         return self.__money      # возвращение ф-ии
#
# h = H()                          # Приватные м-ды используются внутри Класса, снаружи Класса - недоступны
# h.__mo                           # В подсказках отображается __module__, но не __money


                    # ЗАДАНИЕ (20.6)
# Условие:
# Класс Human
# 1. Создайте класс Human.
# 2. Определите для него 2 статических поля: default_name и default_age.
# 3. Cоздайте метод _init_(), который помимо self принимает ещё 2 параметра: name и age.
# Для этих параметров задайте значения по умолчанию, используя cвойства default_name и default_age.
# В м-де _init_() определите 4 свойства: Публичные - name и age. Приватные - money и house.
# 4. Реализуйте справочный м-д info(), который будет выводить поля name, age, house и money.
# 5. Реализуйте справочный статический м-д default_info(), который будет вывоодить статические поля
# default_name и default_age.
# 6. Реализуйте м-д earn_money(), увеличивающий значение свойства money.

# ТЕСТЫ:
# 1. Вызовите справочный м-д default_info() для Класса Human()
# 2. Создайте объект Класса Human
# 3. Выведите справочную информацию о созданном объекте (вызовите м-д info())/
# 4. Поправьте фин. положение объекта - вызовите м-д earn_money()
# 5. Посмотрите, как изменилось состояние объекта классаа Human.

# 1 cпособ:
# class Human:                          # 1.
#
#     default_name = 'Ekaterina'        # 2. Cтатические поля: default_name и default_age
#     default_age = 29
#
#                                       # 3. знач. по умолчанию (name = default_name, age = default_age)
#     def __init__(self, name = default_name, age = default_age):
#         self.name = name               # 4 свойства: Публичные - name и age. Приватные - money и house
#         self.age = age
#
#         self.__money = 1000000000
#         self.__house = 'Penthouse'
#
#     def info(self):
#         print(f'Name: {self.name}')        # или print(self.name)
#         print(f'Age: {self.age}')          # или print(self.age)
#         print(f'House: {self.__house}')    # или print(self.__house)
#         print(f'Money: {self.__money}')    # или print(self.__money)
#                                            # @staticmethod - относится только к одной ф-ии default_info
#     @staticmethod                          # 5.
#     def default_info():                    # д.б. пустые скобочки, self - не передаём
#         print(f'Выведение статического поля default_name: {Human.default_name}')
#         print(f'Выведение статического поля default_age: {Human.default_age}')
#
#     def earn_money(self, plus_money):      # 6.
#         self.__money += plus_money
#         print(f'Новое значение money: {self.__money}')   # f-строка выводит коммент. в виде, приближ. к реальному

# Тесты:                                # Все тесты проводим без табуляции
# Human.default_info()                  # test 1
# Ekaterina = Human('Ekaterina', 29)    # test 2 (создание объекта)
# Ekaterina.info()                      # test 3
# Ekaterina.earn_money(88888888)        # test 4
# Проверка (тест 4*):
# Ekaterina.earn_money(7777777)         # test 4* (проверка) / допустимо прибавление денег неогранич. кол-во раз
# Ekaterina.info()                      # test 5 / по деньгам отобразятся все их прибавления

# Проверка 2.1 (теста 2*):
# Ekaterina = Human()                   # test 2* (проверка) При пустых значениях имя и возраст - по умолчанию.
# Ekaterina.info()                      # Результат: Name: Ekaterina, Age: 29

# Проверка 2.2 (теста 2*):
# Ekaterina = Human('Katy')            # test 2* (проверка)
# Ekaterina.info()                     # Результат: Name: Katy, Age: 29

# Проверка 2.3 (теста 2*):
# Ekaterina = Human('Katy pretty', 29.1)     # test 2* (проверка)
# Ekaterina.info()                           # Результат: Name: Katy pretty, Age: 29.1

                                # Вызов @staticmethod через имя Класса / в статич. м-де не используются аргументы
# Проверка:                             # Приватные атрибуты не покажет:
# Ekaterina.__money                     # Результат: AttributeError: 'Human' object has no attribute '__money'

# 2 cпособ (из презентации):
# class Human:
#
#     # Статические поля:
#     default_name = 'No name'
#     default_age = 0
#
#     def __init__(self, name=default_name, age=default_age):
#         # Динамические поля
#         # Публичные
#         self.name = name
#         self.age = age
#         # Приватные
#         self.__money = 0
#         self.__house = None
#
#     def info(self):
#         print(f'Name: {self.name}')
#         print(f'Age: {self.age}')
#         print(f'Money: {self.__money}')
#         print(f'House: {self.__house}')
#
#     @staticmethod
#     def default_info():
#         print(f'Default Name: {Human.default_name}')
#         print(f'Default Age: {Human.default_age}')
#
#     def earn_money(self, amount):
#         self.__money += amount
#         print(f'Earned {amount} money! Current value: {self.__money}')
#
# Human.default_info()
#
# Ekaterina = Human('Ekaterina', 29)
# Ekaterina.info()
#
# Ekaterina.earn_money(5000)
# Ekaterina.earn_money(20000)
# Ekaterina.info()


                    # 20.7 Пример / Наследование в Python
                    # Родительский класс
# class Phone:
#
#                    # Инициализатор
#     def __init__(self):
#         self.is_on = False
#
#                   # Включаем телефон
#     def turn_on(self):
#         self.is_on = True
#
#                   # Если телефон включен - делаем звонок
#     def call(self):
#         if self.is_on:
#             print('Making call...')
# #
#                  # Унаследованный класс
# class MobilePhone(Phone):                            # Создание нового Класса с помощью механизма наследования:
#                                                      # class<имя_нового_класса>(<имя_родителя>)
#                  # Добавляем новое свойство battery
#     def __init__(self):
#         super().__init__()
#         self.battery = 0
# #
#                 # Заряжаем телефон на величину переданного значения
# def charge(self, num):
#     self.battery = num
#     print(f'Charging battery up to ... {self.battery}%')
#
# my_mobile_phone = MobilePhone()
# dir(my_mobile_phone)


                    # 20.8 Пример / Множественное наследование в Python
# 20.8.1.
                    # создаём класс Vehicle:
# class Vehicle:
#     def vehicle_method(self):
#         print('Это родительский метод из класса Vehicle')
#
#                     # создаём класс Car, который наследует Vehicle
# class Car(Vehicle):
#     def car_method(self):
#         print('Это дочерний метод из класса Car')
#
#                     # создаём класс Cycle, который наследует Vehicle
# class Cycle(Vehicle):
#     def cycleMethod(self):
#         print('Это дочерний метод из класса Cycle')
#
# car_a = Car()
# car_a.vehicle_method() # вызов метода родительского класса / Результат: Это родительский метод из класса Vehicle
# car_b = Cycle()
# car_b.vehicle_method() # вызов метода родительского класса / Результат: Это родительский метод из класса Vehicle

# 20.8.2.
# class Camera:
#     def camera_method(self):
#         print('Это родительский метод из класса Camera')
#
# class Radio:
#     def radio_method(self):
#         print('Это родительский метод из класса Radio')
#
# class CellPhone(Camera, Radio):
#     def cell_phone_method(self):
#         print('Это дочерний метод из класса CellPhone')
#
# cell_phone_a = CellPhone()
# cell_phone_a.camera_method()        # Результат: Это родительский метод из класса Camera
# cell_phone_a.radio_method()         # Результат: Это родительский метод из класса Radio


                    # ЗАДАНИЕ (20.9)
# Класс Alphabet
# 1. Создайте класс Alphabet
# 2. Cоздайте метод _init_(), внутри которого будут определены 2 динамических свойства:
# 1) lang - язык и 2) letters - список букв. Начальные значения свойств берутся из входных параметров метода.
# 3. Создайте метод print(), который выведет в консоль буквы алфавита
# 4. Создайте метод letters_num(), который вернёт количество букв в алфавите.

# Класс EngAlphabet
# 1. Создайте класс EngAlphabet путём наследования от класса Alphabet
# 2. Создайте метод __init__(), внутри которого будет вызываться родительский м-д __init__().
# В качестве параметров ему будут передаваться обозначение языка(например, 'En') и строка, состоящая из всех букв
# алфавита (можно воспользоваться свойством ascii_uppercase из модуля string)/
# 3. Добавьте приватное статическое свойство _letters_num, которое будет хранить количество букв в алфавите.
# 4. Создайте метод is_en_letter(), который будет принимать букву в качестве параметра и определять, относится ли эта
# буква к английскому алфавиту.
# 5. Переопределите метод letters_num() - пусть в текущем классе он будет возвращать значение свойства _letters_num.
# 6. Создайте статический метод example(), который будет возвращать пример текста на английском языке.

# ТЕСТЫ:
# 1. Создайте объект класса EngAlphabet
# 2. Напечатайте буквы алфавита для этого объекта
# 3. Выведите количество букв в алфавите
# 4. Проверьте, относится ли буква F к английскому алфавиту
# 5. Проверьте, относится ли буква Щ к английскому алфавиту
# 6. Вывидите пример текста на английском языке

# import string
#
# class Alphabet:                                       # 1.1. / Алфавит
#
#     def __init__(self, language, letters_str):        # 1.2.
#         self.lang = language
#         self.letters = list(letters_str)
#
#     def print(self):                                  # 1.3. Печатаем все буквы алфавита
#         print(f'Буквы алфавита: {self.letters}')
#
#     def letters_num(self):                            # 1.4. Возвращаем кол-во букв в алфавите
#         return len(self.letters)
#
                                                    # 2.1. Английский алфавит
# class EngAlphabet(Alphabet):                  # string.ascii_uppercase - строка, содержащая все ASCII буквы в upper case
#     __letters_num = 26                              # 2.3. в английском алф. 26 букв.
#
#     def __init__(self):                            # 2.2.
#         super().__init__('En', string.ascii_uppercase)
#
#     def is_en_letter(self, letter):                # 2.4. Проверка: относится ли буква к английскому алфавиту
#         if letter.upper() in self.letters:
#             return True
#         return False
#
#     def letters_num(self):                         # 2.5. Возвращаем кол-во букв в алфавите
#         return EngAlphabet.__letters_num
#
#     @staticmethod                                  # 2.6. Пример текста на английском языке
#     def example():
#         return 'English Example:\n Our life is what our thoughts make it!'

# ТЕСТЫ:
# if __name__ == '__main__':
#     eng_alphabet = EngAlphabet()             # test 1
#     eng_alphabet.print()                     # test 2
#     print(eng_alphabet.letters_num())        # test 3
#     print(eng_alphabet.is_en_letter('F'))    # test 4
#     print(eng_alphabet.is_en_letter('Щ'))    # test 5
#     print(EngAlphabet.example())             # test 6

