# Задание 1
# import time
#
# class TraficLight:
#     def __init__(self, color):
#         self.__c = color
#
#     def running(self):
#         print(self.__c[0])
#         time.sleep(7)
#         print(self.__c[1])
#         time.sleep(2)
#         print(self.__c[2])
#         time.sleep(10)
#
# TraficLight1 = TraficLight(['красный', 'жёлтый', 'зелёный'])
# print(TraficLight1.running())

# Задание 2
# class Road:
#     massa = 25
#     thickness = 5
#
#     def __init__(self, length, width):
#         self._l = length
#         self._w = width
#
#     def weight(self):
#         formula = self._l * self._w * self.massa/1000 * self.thickness
#         print(f'Масса асфальта, необходимого для покрытия всей дороги равна: {formula} т')
#
# Road1 = Road(5000, 20)
# Road1.weight()

# Задание 3
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self, wage, bonus):
        self._income[wage] = bonus
        return sum(self._income)

Position1 = Position('Иван', 'Иванов', 'директор', 20000)
Position1.get_full_name()
print(Position1.get_total_income(20000, 15000))