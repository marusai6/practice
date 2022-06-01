# Задание 2
# n = [2, 5, 3, 10, 10, 12, 7, 6, 5, 44, 122]
#
# new = [n[i+1] for i in range(len(n)-1) if n[i+1] > n[i]]
# print(new)

# Задание 3
# gen = [num for num in range(20, 241) if num % 20 == 0 or num % 21 == 0]
# print(gen)

# Задание 4
# my_list = [1, 2, 2, 35, 36, 8, 2, 6, 7, 12, 6, 15, 16, 16]
# new_list = [el for el in my_list if my_list.count(el) == 1]
# print(new_list)

# Задание 5
# from functools import reduce
#
# def func(a, b):
#     return a * b
#
# li = [num for num in range(100, 1001) if num % 2 == 0]
# print(reduce(func, li))

# Задание 6
# from itertools import count, cycle

# for el in count(3):
#     print(el)
#     if el >= 10:
#         break

# i = 0
# for el in cycle([1, 2, 3, 4, 5]):
#     print(el)
#     i += 1
#     if i >= 20:
#         break

# Задание 7
def fact(n):
    a = 1
    for el in range(1, n + 1):
        a = a * el
        yield a

for el in fact(6):
    print(el)



