# Задание 1
# list = [5, 'home', 12, True, [1, 2, 3]]
# for element in list:
#     print(type(element))

# Задание 2
# list = list(input('Введите список'))
# for i in range(0, len(list)-1, 2):
#     list[i], list[i+1] = list[i+1], list[i]
# print(list)

# Задание 3
# Решение через list
# month = int(input('Введите месяц в виде числа от 1 до 12'))
# list = ['зима', 'весна', 'лето', 'осень']
# if month >= 1 and month <=2 or month == 12:
#     print(list[0])
# elif month >=3 and month <=5:
#     print(list[1])
# elif month >=6 and month<=8:
#     print(list[2])
# else:
#     print(list[3])

# Решение через dict
# month = int(input('Введите месяц в виде числа от 1 до 12'))
# dict = {'зима': [1, 2, 12], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
# for el in dict:
#     if month in dict[el]:
#         print(el)

# Задание 4
# stroka = input('Введите строку')
# list = stroka.split((' '))
# for ind, el in enumerate(list, 1):
#     print(ind, el[:10])

# Задание 5
my_list = [7, 5, 3, 3, 2]
new_el = int(input('Введите новый элемент списка'))
for el in my_list:
    if new_el >= el:
        i = my_list.index(el)
        my_list.insert(i, new_el)
        break

for el in my_list:
    if new_el < my_list[-1]:
        my_list.append(new_el)

print(my_list)

# Задание 6
# number1 = int(input('Введите номер первого товара'))
# name1 = input('Введите название первого товара')
# price1 = int(input('Введите цену первого товара'))
# kol1 = int(input('Введите количество первого товара'))
# ed1 = input('Введите единицу измерения первого товара')
# number2 = int(input('Введите номер второго товара'))
# name2 = input('Введите название второго товара')
# price2 = int(input('Введите цену второго товара'))
# kol2 = int(input('Введите количество второго товара'))
# ed2 = input('Введите единицу измерения второго товара')
# number3 = int(input('Введите номер третьего товара'))
# name3 = input('Введите название третьего товара')
# price3 = int(input('Введите цену третьего товара'))
# kol3 = int(input('Введите количество третьего товара'))
# ed3 = input('Введите единицу измерения третьего товара')
#
# kor1 = (number1, {"название": name1, "цена": price1, "количество": kol1, "ед": ed1})
# kor2 = (number2, {"название": name2, "цена": price2, "количество": kol2, "ед": ed2})
# kor3 = (number3, {"название": name3, "цена": price3, "количество": kol3, "ед": ed3})
# tovari = [kor1, kor2, kor3]
#
# list1 = [name1, name2, name3]
# list2 = [price1, price2, price3]
# list3 = [kol1, kol2, kol3]
# list4 = [ed1, ed2, ed3]
# dict = {'название': list1, "цена": list2, "количество": list3, "ед": list4}
#
# print(dict)



