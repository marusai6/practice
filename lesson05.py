# Задание 1
# f = open("Text.txt", 'w', encoding='utf-8')
# while True:
#     content = input('Введите данные: ')
#     f.write(f'{content}\n')
#     if not content:
#         break
#
# f.close()

# Задание 2
# with open("Text2.txt", 'r', encoding='utf-8') as f:
#     i = 0
#     for line in f:
#         i += 1
#         li = line.split(' ')
#         n = 0
#         for el in li:
#             n += 1
#         print(f'Количество слов в {i} строке: {n}')
#     print(f'Всего в файле строк: {i}')

# Задание 3
# with open("Text3.txt", 'r', encoding='utf-8') as f:
#     okladi = []
#     for line in f:
#         li = line.split(' ')
#         li[1] = float(li[1].strip())
#         okladi.append(li[1])
#         if li[1] < 20000.00:
#             print(li[0])
#     from statistics import mean
#     print(f'Средний оклад {mean(okladi)}')

# Задание 4
# with open("Text4.txt", 'r', encoding='utf-8') as f:
#     my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре' }
#     new_li = []
#     for line in f:
#         li = line.split(' ')
#         for key, value in my_dict.items():
#             if li[0] == key:
#                 li[0] = value
#         for el in li:
#             new_li.append(el)
#
# with open("Text5.txt", 'w', encoding='utf-8') as ff:
#     ff.writelines(new_li)

# Задание 5
# stroka = '1 2 5 12 16'
# with open("Text6.txt", 'w', encoding='utf-8') as f:
#     f.write(stroka)
# with open("Text6.txt", 'r', encoding='utf-8') as f:
#     text = f.readline()
#     li = text.split(' ')
#     new_li = map(int, li)
#     print(sum(new_li))



# Задание 7
with open("Text8.txt", 'r', encoding='utf-8') as f:
    from statistics import mean
    my_dict = {}
    li = []
    for line in f:
        my_li = line.split(' ')
        revenue = int(my_li[2])
        costs = int(my_li[3].strip())
        profit = revenue - costs
        my_dict[my_li[0]] = profit
        if profit >= 0:
            li.append(profit)

    average_profit = mean(li)
    my_dict2 = {"average_profit": average_profit}
    all_li = [my_dict, my_dict2]
    # print(all_li)

import json

with open("all_li.json", 'w', encoding='utf-8') as f1:
    json.dump(all_li, f1)