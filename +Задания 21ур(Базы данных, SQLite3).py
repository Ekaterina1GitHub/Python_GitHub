                    # 21. БАЗЫ ДАННЫХ (БД). SQLite 3
                    # 21.1 Пример / Создание БД
import sqlite3    # 3 - последняя версия библиотеки sqlite
                    # Cоздаём базу данных:
# a = sqlite3.connect('name.db') # connect() - команда, помогающая создать БД
                               # cursor()- команда, позволяющая взаимодействовать с БД (доб, удал, заполнять колонки)
                               # db - разрешение для БД
# b = a.cursor()               # пер. a, b - можно задавать любые наименования
                               # Cоздадим таблицу с 2-мя текстовыми колонками:
# b.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT)''')
                               # ''' - обязательный синтаксис !!!
                               # execute - команда, помогающая создать таблицу
                               # CREATE TABLE IF NOT EXISTS - СОЗДАТЬ ТАБЛ, ЕСЛИ НЕ СУЩЕСТВУЕТ (БОЛЬШИМИ БУКВАМИ ПИШЕМ)
                               # tab_1 - название таблички
                               # id INTEGER PRIMARY KEY AUTOINCREMENT - автоматич. привязка ID к каждой записи в БД
                               # col_1, col_2 - необходимые колонки
                               # TEXT - один из типов данных для текста.


                    # 21.2 Пример / Заполнение БД
                    # Заполняем таблицу данными:
# 21.2.1 (1-ый способ заполнения)
# b.execute('''INSERT INTO tab_1(col_1, col_2) VALUES ('hello', 'world')''')

# 21.2.2 (2-ой способ заполнения / через переменные)
# c = 'red'                       # перем. можно записать через input
# d = 'black'
# b.execute('''INSERT INTO tab_1(col_1, col_2) VALUES (?,?)''', (c, d))
                                # Можно было сделать запись без переменных c и d:
                                # b.execute('''INSERT INTO tab_1(col_1, col_2) VALUES (red, black)''')

                    # Сохраняем изменения (вносить после каждого изм-я БД):
# a.commit()                      # Сохранение изм-ий в БД - обязательно !!!
                                # INSERT INTO - ВСТАВИТЬ В (БОЛЬШИМИ БУКВАМИ ПИШЕМ)
                                # VALUES - ЗНАЧЕНИЯ (БОЛЬШИМИ БУКВАМИ ПИШЕМ)
                                # ('hello', 'world') - знач-я, которые хотим доб-ть


                    # 21.3 Пример / Выведение записи из таблиц
# 21.3.1 (1-ый способ)
# b.execute('''SELECT * FROM tab_1''')      # SELECT * FROM tab_1 - SQL - запрос (SELECT, FROM - кл. слова)
# v = b.fetchall()
# print(v)                 # Результат: [(1, 'hello', 'world'), ... , (10, 'red', 'black'), (11, 'hello', 'world')]
                           # Если закомментир-ть 23 либо 28 строку - добавится 1 запись в БД (23 либо 28 строка)
                           # Если закомментир-ть 23 и 28 строку - при запуске программы не добавится ни 1 запись в БД


                    # 21.4 Пример / Примеры SELECT
# Пример, рассмотренный на занятии:
# import sqlite3
# A = sqlite3.connect('primeri_s_21_zaniatia.db')
# B = A.cursor()
# B.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT, col_3 INTEGER)''')
# B.execute('''INSERT INTO tab_1(col_1, col_2, col_3) VALUES ('hello', 'world', 7654321)''')
# A.commit()

# B.execute('''SELECT * FROM tab_1''')                     # SELECT * FROM tab_1 - SQL - запрос (SELECT, FROM - кл. слова)
# V = B.fetchall()
# print(V)
                    # ПРИМЕРЫ:
                    # 21.4.1. Ф-ия fetchone() для получ-я результа:
# a = 'hello'
# B.execute('''SELECT * FROM tab_1 WHERE col_1 = 'hello' ''')
# A.commit()
# V = B.fetchall()
# print(V)
#
#                     # 21.4.2. Список всех записей, отсортир. относит. 3 колонки
# B.execute('''SELECT * FROM tab_1 ORDER BY col_3''')
# A.commit()
# V = B.fetchall()
# print(V)

                    # 21.4.3. Поиск по всей таблице записи 3-ей колонки, которые начинаются с 7
# B.execute('''SELECT * FROM tab_1 WHERE col_3 LIKE '7%' ''')
# A.commit()
# V = B.fetchall()
# print(V)


                    # 21.5 Пример / Редактирование и удаление записей
                    # Удаление записей из таблицы по id, по значению
# b.execute('''DELETE FROM tab_1 WHERE id = 1''')
# a.commit()
# b.execute('''DELETE FROM tab_1 WHERE col_1 = 'red' ''')
# a.commit()
# b.execute('''SELECT * FROM tab_1''')
# v = b.fetchall()
# print(v)
                                                   # После каждого удаления требуется закомментировать уд-ные строки

                    # 21.6 Пример / Обновление записей в БД
# t = 3
# b.execute('''UPDATE tab_1 SET col_1 = 'world' WHERE id=?''', (t,))
# a.commit()
# b.execute('''SELECT * FROM tab_1''')
# v = b.fetchall()
# print(v)                                          # Результат: [ ... , (3, 'world', 'world'), ... ]
