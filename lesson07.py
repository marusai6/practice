# Задание 1
# class Matrix:
#     def __init__(self, num1, num2, num3, num4):
#         self.my_list = [[num1, num2], [num3, num4]]
#
#     def __str__(self):
#         return f'{self.my_list[0][0]} {self.my_list[0][1]}\n{self.my_list[1][0]} {self.my_list[1][1]}'
#
#     def __add__(self, other):
#         new_list = []
#         for i in range(len(self.my_list)):
#             for j in range(len(self.my_list)):
#                 new_list.append(self.my_list[i][j] + other.my_list[i][j])
#         return f'{new_list[0]} {new_list[1]}\n{new_list[2]} {new_list[3]}'
#
# mt1 = Matrix(1,2,3,4)
# mt2 = Matrix(13,2,5,0)
# print(mt1)
# print(mt1 + mt2)

# Задание 2
# from abc import ABC, abstractmethod
#
# class Clothes:
#     def need_all(self, V, H):
#         self.V = V
#         self.H = H
#         return (self.V/6.5 + 0.5) + (2 * self.H + 0.3)
#
# class AbstractCoat(ABC):
#     @abstractmethod
#     def need(self):
#         pass
#
# class Coat(AbstractCoat, Clothes):
#     def __init__(self, V):
#         self.V = V
#     def need(self):
#         return self.V/6.5 + 0.5
#
# class AbstractSuit(ABC):
#     @abstractmethod
#     def need1(self):
#         pass
#
# class Suit(AbstractSuit, Clothes):
#     def __init__(self, H):
#         self.H = H
#     def need1(self):
#         return 2 * self.H + 0.3
#     @property
#     def H(self):
#         return self.__H
#     @H.setter
#     def H(self, H):
#         if H < 1.30:
#             self.__H = 1.30
#         elif H > 2.10:
#             self.__H = 2.10
#         else:
#             self.__H = H
#
# coat1 = Coat(46)
# print(coat1.need())
#
# suit1 = Suit(1.70)
# print(suit1.need1())
#
# print(coat1.need_all(46, 1.70))

# Задание 3
class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        if self.num >= other.num:
            return self.num - other.num
        else:
            return f'Первая клетка меньше второй!'

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        return self.num // other.num

    def make_order(self, row):
        while self.num >= row:
            print("*" * row)
            self.num = self.num - row
        if self.num < row:
            print("*" * (self.num % row))

cell1 = Cell(15)
cell2 = Cell(6)

print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
cell1.make_order(6)