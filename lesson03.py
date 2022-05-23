# Задание 1
# def my_func(num1, num2):
#     try:
#         num1 / num2
#         return print(num1 / num2)
#     except ZeroDivisionError:
#         return print('На ноль делить нельзя!')
#
# num1 = int(input('Введите первое число'))
# num2 = int(input('Введите второе число'))
# my_func(num1, num2)

# Задание 2
# def my_func(name, surname, year, city, email, tel):
#     print(f'Имя: {name}, фамилия: {surname}, год рождения: {year}, город проживания: {city}, email: {email}, телефон: {tel}')
#
# my_func(name = input('Имя: '), surname = input('Фамилия:'), year = input('Год рождения'), city = input('город проживания'), email = input('email: '), tel = input('телефон: '))

# Задание 3
# def my_func(a, b, c):
#     list = [a,b,c]
#     res = sum(list) - min(list)
#     print(res)
#
# my_func(3,2,1)

# Задание 4
# Способ 1
# def my_func(x, y):
#     return print(x**y)
#
# my_func(1.15, -6)

# 2 способ
# def my_func(x, y):
#     num = 1
#     res = 1/x
#     while num != abs(y):
#         res = res * (1/x)
#         num += 1
#     return print(res)
#
# my_func(2, -3)

# Заданеие 5
# def my_func():
#     summa = 0
#     while True:
#         my_list = input('Введите строку чисел, разделённых пробелом').split( )
#         for el in my_list:
#             if el == "*":
#                 return
#             else:
#                 summa = summa + int(el)
#             print(summa)
#
# my_func()

# Задание 6, 7
def int_func():
    stroka = input('Text: ').title()
    return print(stroka)

int_func()

