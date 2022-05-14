# Задание 1
# Name = 'Maria'
# print(Name)
# Age = 35
# print(Age)
# City = input('Введите свой город')
# Pop = input('Введите население')
# print(f'Вы проживаете в городе {City} с населением {Pop} человек')

# Задание 2
# time = int(input('Введте время в секундах'))
# hour = time//60//60
# min = (time - hour * 3600)//60
# sec = time % 60
# print(f'{hour}:{min}:{sec}')

# Задание 3
# number = input('Введите число')
# result = int(number) + int(number+number) + int(number+number+number)
# print(result)

# Задание 4
# num = int(input('Введите целое положительное число'))
# res = 0
# while True:
#     last = num % 10
#     if last > res:
#         res = last
#         num = num // 10
#     else:
#         break
# print(res)

# Задание 5
# profit = int(input('Введите выручку'))
# costs = int(input('Введите издержки'))
# result = profit - costs
# if profit >= costs:
#     print(f'У вас прибыль {result}')
# else:
#     print(f'У вас убыток {result}')

# Задание 6
# profit = int(input('Введите выручку'))
# costs = int(input('Введите издержки'))
# result = profit - costs
# if profit > costs:
#     rent = result / profit
#     print(f'Рентабельность выручки {rent}')
#     number = int(input('Укажите численность сотрудников'))
#     res = result / number
#     print (f'Прибыль фирмы на одного сотрудника {res}')
# else:
#     print('Убыток')

# Задание 7
a = int(input('Сколько пробежал в  первый день'))
b = int(input('Сколько нужно пробежать'))
day = 1
while a < b:
    a = a + 0.1 * a
    day = day + 1
print(f'На {day} день спортсмен достиг результата - не менее {b} км')