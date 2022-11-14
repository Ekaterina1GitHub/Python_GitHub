                    # ЗАДАНИЕ 10.1 (ДЗ)
# Условие:
# Есть массив, состоящий из слов и чисел, нужно записать в файл сначала слова в порядке их длины,
# а после слов цифры в порядке возрастания.

# arr = [1, 2, 'three', 'four', 5, 6, 'seven', 'eight', 9, 10, 'eleven']    # Массив из слов и чисел
#
# f = open('DZ_10.txt', 'w')
# s = []       # числа
# c = []       # слова
# for i in arr:
#     if type(i) is int:
#         s.append(i)
#         s.sort()
#     else:
#         c.append(i)
#         d = sorted(c, key=len)
# s = str(s)
# s1 = ''.join(s.replace("[", ', '))
# s2 = ''.join(s1.replace("]", ' '))
# s3 = ', '.join(d)
#
# f.write(s3 + s2)
# f.close()