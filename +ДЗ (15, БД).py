                    # ЗАДАНИЕ 15.1 (ДЗ)
# import sqlite3
#
# BD = sqlite3.connect('Dom_Zad_15.db')
#
# Vzaimodeistvie_s_BD = BD.cursor()
#
# Vzaimodeistvie_s_BD.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER, col_2 INTEGER, col_3 INTEGER)''')
# Vzaimodeistvie_s_BD.execute('''INSERT INTO tab_1(col_1, col_2, col_3) VALUES (2020, 2021, 2022)''')
#
#                                                                                        # 1. ВЫБОРКА ДАННЫХ:
# Vzaimodeistvie_s_BD.execute('''SELECT * FROM tab_1''')                                 # 1.1. Выводим всё из таблицы tab_1.
# BD.commit()
# Result = Vzaimodeistvie_s_BD.fetchall()
# print(Result)                                                                          # Результат: [(1, 2020, 2021, 2022)]
#
# Vzaimodeistvie_s_BD.execute('''SELECT 2022 FROM tab_1''')                              # 1.2. Выводим колонку '2022' из таблицы tab_1.
# BD.commit()
# Result = Vzaimodeistvie_s_BD.fetchall()
# print(Result)                                                                          # Результат: [(2022,)]

# Vzaimodeistvie_s_BD.execute('''SELECT 2020, 2022 FROM tab_1''')                        # 1.3. Выводим колонки '2020 и 2022' из таблицы tab_1.
# BD.commit()
# Result = Vzaimodeistvie_s_BD.fetchall()
# print(Result)                                                                          # Результат: [(2020, 2022)]

#                                                                                        # 2. ВЫБОРКА ДАННЫХ С УСЛОВИЕМ:
# c = 1000        # новое значение для колонки 1.
# d = 2000        # новое значение для колонки 2.
# e = 3000        # новое значение для колонки 3.
# Vzaimodeistvie_s_BD.execute('''INSERT INTO tab_1(col_1, col_2, col_3) VALUES (?,?,?)''', (c, d, e))
#
# Vzaimodeistvie_s_BD.execute('''SELECT * FROM tab_1 WHERE col_2 = 2000 ''')             # 2.1. Выводим всё из tab_1, если 2-ая колонка = 2000
# BD.commit()
# Result = Vzaimodeistvie_s_BD.fetchall()
# print(Result)                                                                         # Результат: [(2, 1000, 2000, 3000)]
#
# Vzaimodeistvie_s_BD.execute('''SELECT * FROM tab_1 WHERE col_2 = 2000 and col_3 = 3000''')  # 2.2. Выводим всё из tab_1, если 2-ая колонка = 2000
# BD.commit()                                                                                 # а 3-я = 3000
# Result = Vzaimodeistvie_s_BD.fetchall()
# print(Result)                                                                    # Результат: [(2, 1000, 2000, 3000)]
#
# Vzaimodeistvie_s_BD.execute('''SELECT 1000 FROM tab_1 WHERE col_1 = 1000 ''')    # 2.3. Выводим 1000 из tab_1, если 1-ая колонка = 1000
# BD.commit()
# Result = Vzaimodeistvie_s_BD.fetchall()
# print(Result)                                                                 # Результат: [(1000,)]

                                                                                # 3. СОРТИРОВКА ДАННЫХ:
# Vzaimodeistvie_s_BD.execute('''SELECT * FROM tab_1 ORDER BY col_1 ''')        # 3.1. Список всех записей, отсортированных относительно 1-ой колонки
# BD.commit()                                                                   # cортировка по возрастанию
# Result = Vzaimodeistvie_s_BD.fetchall()
# print(Result)                                                                 # Результат: [(2, 1000, 2000, 3000), (1, 2020, 2021, 2022)]

# Vzaimodeistvie_s_BD.execute('''SELECT * FROM tab_1 ORDER BY col_3 DESC ''')   # 3.2. Список всех записей, отсортированных относительно 3-ей колонки
# BD.commit()                                                                   # сортировка по убыванию
# Result = Vzaimodeistvie_s_BD.fetchall()
# print(Result)                                                                 # Результат: [(2, 1000, 2000, 3000), (1, 2020, 2021, 2022)]

                                                                                # 4. ЧАСТИЧНОЕ СОВПАДЕНИЕ:
# Vzaimodeistvie_s_BD.execute('''SELECT * FROM tab_1 WHERE col_1 LIKE '2%' ''')
# BD.commit()                                                                   # 4.1. Поиск по всей таблице записи 1-ой колонки, которые начинаются с 2
# Result = Vzaimodeistvie_s_BD.fetchall()
# print(Result)                                                                 # Результат: [(1, 2020, 2021, 2022)]

# Vzaimodeistvie_s_BD.execute('''SELECT * FROM tab_1 WHERE col_2 LIKE '%00%' ''')
# BD.commit()                                                               # 4.2. Поиск по всей таблице записи 2-ой колонки, которые имеют '00'.
# Result = Vzaimodeistvie_s_BD.fetchall()
# print(Result)                                                             # Результат: [(2, 1000, 2000, 3000)]

                                                                     # 5. РЕДАКТИРОВАНИЕ И УДАЛЕНИЕ ЗАПИСЕЙ:
# Vzaimodeistvie_s_BD.execute('''SELECT * FROM tab_1''')             # 5.1. Выводим всё из таблицы tab_1.
# BD.commit()
# Result = Vzaimodeistvie_s_BD.fetchall()
# print(Result)                                                      # Результат: [(1, 2020, 2021, 2022), (2, 1000, 2000, 3000)]
#
# Vzaimodeistvie_s_BD.execute('''DELETE FROM tab_1 WHERE id = 2''')
# BD.commit()                                                        # Результат: [(1, 2020, 2021, 2022)]
#
# Vzaimodeistvie_s_BD.execute('''SELECT * FROM tab_1''')
# Result = Vzaimodeistvie_s_BD.fetchall()
# print(Result)
                                                                     # 5.2. Обновление записей в БД
# t = 1
# Vzaimodeistvie_s_BD.execute('''UPDATE tab_1 SET col_1 = 2022 WHERE id=?''', (t,))
# BD.commit()
# Vzaimodeistvie_s_BD.execute('''SELECT * FROM tab_1''')
# Result = Vzaimodeistvie_s_BD.fetchall()
# print(Result)                                                      # Результат: [(1, 2022, 2021, 2022)]