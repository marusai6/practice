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
    wage = 0
    bonus = 0
    income = {"wage": wage, "bonus": bonus}
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self, wage, bonus):
        self.wage = wage
        self.bonus = bonus
        print(self.wage + self.bonus)

Position1 = Position('Иван', 'Иванов', 'директор', 20000)
Position1.get_full_name()
Position1.get_total_income(20000, 15000)

# Задание 4
# class Car:
#     def __init__(self, speed, color, name, is_police):
#         self.s = speed
#         self.c = color
#         self.n = name
#         self.is_police = is_police
#
#     def info(self):
#         print(self.c, self.s, self.n, self.is_police)
#
#     def go(self):
#         print('Машина поехала')
#
#     def stop(self):
#         print("Машина остановилась")
#
#     def turn(self, direction):
#         self.direction = direction
#         print(f'Машина повернула {self.direction}')
#
#     def show_speed(self):
#         print(f'{self.s} км/ч')
#
# class TownCar(Car):
#     def show_speed(self):
#         if self.s > 60:
#             print("Скорость выше 60 км/ч! Превышение скорости!")
#
# class SportCar(Car):
#     pass
#
# class WorkCar(Car):
#     def show_speed(self):
#         if self.s > 40:
#             print("Скорость выше 40 км/ч! Превышение скорости!")
#
# class PoliceCar(Car):
#     pass
#
# Car1 = TownCar(75, 'жёлтый', 'BMW', False)
# Car2 = SportCar(120, "green", 'Tesla', False)
# Car3 = WorkCar(35, 'black', 'Cat', False)
# Car4 = PoliceCar(90, 'blue', 'Ford', True)
#
# Car1.info()
# Car1.go()
# Car1.turn('налево')
# Car1.show_speed()
#
# Car2.info()
# Car2.stop()
# Car2.show_speed()
#
# Car3.info()
# Car3.show_speed()
#
# Car4.info()
# Car4.turn('направо')

# Задание 5
# class Stationery:
#     title = 'Канцелярия'
#     def draw(self):
#         print("Запуск отрисовки")
#
# class Pen(Stationery):
#     def draw(self):
#         print("Запуск отрисовки ручки")
#
# class Pencil(Stationery):
#     def draw(self):
#         print("Запуск отрисовки карандаша")
#
# class Handle(Stationery):
#     def draw(self):
#         print("Запуск отрисовки маркера")
#
# Pen1 = Pen()
# Pencile1 = Pencil()
# Handle1 = Handle()
# Stationery1 = Stationery()
#
# Pen1.draw()
# Pencile1.draw()
# Handle1.draw()
# Stationery1.draw()

