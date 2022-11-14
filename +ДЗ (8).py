                    # ЗАДАНИЕ 8.1. (ДЗ)
# Условие:
# У Вас есть словарь, где ключ - название продукта. Значение - список, который содержит цену и кол-во товара.
# Выведите через '-' название - цену - количество.
# С клавиатуры вводите название товара и его кол-во. n - выход из программы.
# Посчитать цену выбранных товаров и сколько товаров осталось в изначальном списке.

# способ 1*:
# a = dict(Молоко=[1.92, 321], Кофе=[4.59, 258], Шоколад=[2.09, 325], Кетчуп=[3.59, 254])
# print("Словарь: ", a)
#
# Itogo = 0
#
# for name, price_quantity in a.items():                                # items - список, эл-ты перечислены через запятую
#     print(name, '-', price_quantity[0], '-', price_quantity[1])
#
# while True:
#     b = input("Введите наименование товара: ")
#     c = int(input("Введите количество товара: "))
#     e = "Примечание: Введите 'n'  в 'Наименовании товара', если желаете выйти из программы!"
#     print(e)
#
#     if b == 'n' or b not in a:
#         print("Выход из программы!")
#         break
#     else:
#         if c <= a['Молоко'][1] or c <= a['Кофе'][1] or c <= a['Шоколад'][1] or c <= a['Кетчуп'][1]:
#             Itogo = Itogo + (c * a[b][0])
#             a[b][1] = a[b][1] - c
#             print("ИТОГО:", Itogo)
#             print("Остаток товара на складе: ", a[b][1])
#         if c > a['Молоко'][1] or c > a['Кофе'][1] or c > a['Шоколад'][1] or c > a['Кетчуп'][1]:
#             print("К сожалению, введенное кол-во превышает остаток товара по складу!")
#             continue
#
# for name, price_quantity in a.items():                                # items - список, эл-ты перечислены через запятую
#     print(name, '-', price_quantity[0], '-', price_quantity[1])

# способ 2(из презентации):
# goods = {'Apple': [4.5, 10],
#          "Orange": [6.2, 5],
#          "Pineapple" : [10.0, 1],
#          "Mango": [7.5, 2],
#          "Banana": [3.8, 10]}
#
# for key, value in goods.items():
#     print(key, '-', value[0], '-', value[1])
# cost = 0
#
# while True:
#     good = input("What?(n- nothing)")
#     if good == 'n' or good not in goods.keys():
#         break
#     qty = int(input("How many?"))
#     if qty > goods[good][1]:
#         print("We do not have so much.")
#         continue
#     cost += goods[good][0] * qty
#     goods[good][1] -= qty
# print("Price:", cost)
# print('----------------------------------------------------------------')
# for key, value in goods.items():
#     print(key, '-', value[0], '-', value[1])


# способ 3(закрепление задачи):
# products = {'Meat': [10.38, 47],       # словарь с продукиами.
#          "Fish": [6.27, 54],
#          "Potatoes": [2.00, 33],
#          "Carrot": [1.54, 15],
#          "Cheese": [3.80, 10]}
# b = list(products.keys())                        # выводим все ключи словаря, переводим ключи в список
# print('Ключи:', b)
# c = list(products.values())                      # выводим все значения словаря, переводим значения в список
# print('Значения:', c)
# print(b[0], '-', c[0][0], '-', c[0][1])
# print(b[1], '-', c[1][0], '-', c[1][1])
# print(b[2], '-', c[2][0], '-', c[2][1])
# print(b[3], '-', c[3][0], '-', c[3][1])
# print(b[4], '-', c[4][0], '-', c[4][1])
# cost = 0
#
# while True:
#     name = str(input("Введите название товара либо 'n' для выхода: "))
#     if name == 'n':
#         break
#     quantity = int(input("Введите количество товара: "))
#     if quantity > products[name][1]:
#         print("Введённое количество больше, чем фактическое наличие товара: ")
#         continue
#     cost += products[name][0] * quantity                # cost = cost + (products[name][0] * quantity)
#     products[name][1] -= quantity                       # products[name][1] = products[name][1] - quantity
#     print("К оплате: ", cost)
# for key, value in products.items():
#     print(key, '-', value[0], '-', value[1])
