# Задание 1
# class Date:
#     def __init__(self, dd, mm, yy):
#         self.dd = dd
#         self.mm = mm
#         self.yy = yy
#
#     @classmethod
#     def transf(cls, data):
#         dd, mm, yy = data.split("-")
#         return cls(int(dd), int(mm), int(yy))
#
#     @staticmethod
#     def valid(obj):
#         if obj.dd < 1 or obj.dd > 31 or obj.mm < 1 or obj.mm > 12 or obj.yy < 1900 or obj.yy > 2100:
#             return f'День должен быть от 1 до 31!\nМесяц должен быть от 1 до 12!\nГод должен быть от 1900 до 2100!'
#         else:
#             return obj.dd, obj.mm, obj.yy
#
#
# my_date = '06-06-2022'
# today = Date.transf(my_date)
# print(today.dd, today.mm, today.yy)
# print(Date.valid(today))

# Задание 2
# class MyError(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
# try:
#     num1 = int(input("Введите число"))
#     num2 = int(input("Введите второе число"))
#     if num2 == 0:
#         raise MyError("На ноль делить нельзя!")
# except (ValueError, MyError) as err:
#     print(err)
# else:
#     res = num1 / num2
#     print(res)
# finally:
#     print("Программа завершена")

# Задание 3
# class MyError(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
# li =[]
# while True:
#     try:
#         elem = input("Введите число")
#         if elem == "stop":
#             break
#         elif elem not in '0123456789':
#             raise MyError("Вы ввели не число!")
#         else:
#             li.append(elem)
#     except MyError as err:
#         print(err)
#
# print(li)

# Задание 4, 5, 6
class Warehouse:

    @staticmethod
    def admission(obj, num):
        try:
            return f'{obj.name} модель {obj.model} в количестве {int(num)} шт. поступил на склад'
        except ValueError:
            print("Вы ввели не число!")

    @staticmethod
    def release(obj, num, shop):
        return f'{obj.name} модель {obj.model} в количестве {num} шт. переданы в магазин № {shop}'


class OfficeEquipment:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

class Printer(OfficeEquipment, Warehouse):
    def __init__ (self, name, color, size, model, number_of_pages, black_and_white):
        super().__init__(name, color, size)
        self.model = model
        self.number_of_pages = number_of_pages
        self.black_and_white = black_and_white

class Scaner(OfficeEquipment, Warehouse):
    def __init__ (self, name, color, size, model):
        super().__init__(name, color, size)
        self.model = model


class Xerox(OfficeEquipment, Warehouse):
    def __init__ (self, name, color, size, model, black_and_white):
        super().__init__(name, color, size)
        self.model = model
        self.black_and_white = black_and_white

class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

pr1 = Printer("Принтер", "grey", '150x200', 'HP 15x1.3', 2000, False)
sc1 = Scaner('Сканер', 'white', '120x150', 'Lenovo 2336gd')
xe1 = Xerox('Ксерокс', 'black', '200x200', 'sumsung 4588f', True)
print(Printer.admission(pr1, '15'))
print(Printer.release(pr1, 11, 5))

# Задание 7
# class ComplexNum:
#     def __init__(self, R, mnim):
#         self.R = R
#         self.mnim = mnim
#
#     def __str__(self):
#         if self.R == 0:
#             return f'{self.mnim}i'
#         elif self.mnim == 0:
#             return f'{self.R}'
#         else:
#             return f'{self.R} + {self.mnim}i'
#
#     def __add__(self, other):
#         return f'{self.R + other.R} + {self.mnim + other.mnim}i'
#
#     def __mul__(self, other):
#         return f'{self.R * other.R - self.mnim * other.mnim} + {self.R * other.mnim + self.mnim * other.R}i'
#
# num1 = ComplexNum(5, 4)
# num2 = ComplexNum(8, 5)
# print(num1)
# print(num2)
# print(num1 + num2)
# print(num1 * num2)

