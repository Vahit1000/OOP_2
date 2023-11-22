# Задание 2.
#
# Реализовать иерархию классов автомобилей.
#
#     Легковые
#     Грузовые
#     Пассажирские
#
# Помимо служебных методов реализовать расчёт расхода топлива
# в зависимости от загрузки, расчёт стоимости и/или времени поездки.
from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def __init__(self, name: str = '', distance: float = 0, fuel_cons: float = 0, average_speed: float = 0):
        self._name = name
        self._distance = float(distance)  # расстояние
        self._fuel_cons = float(fuel_cons)  # удельный расход топлива
        self._average_speed = float(average_speed)  # средняя скорость

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def distance(self):
        return self._distance

    @name.setter
    def distance(self, value):
        if value < 0:
            self._distance = 0
        else:
            self._distance = value

    @property
    def fuel_cons(self):
        return self._fuel_cons

    @name.setter
    def fuel_cons(self, value):
        if value < 0:
            self._fuel_cons = 0
        else:
            self._fuel_cons = value

    @property
    def average_speed(self):
        return self._average_speed

    @name.setter
    def average_speed(self, value):
        if value < 0:
            self._average_speed = 0
        else:
            self._average_speed = value if value <= 90 else 90

    def driving(self):
        if self._average_speed <= 0:
            return 0
        else:
            return self._distance / self._average_speed


class LigthCar(Car):

    def __init__(self, name, mans, distance, fuel_cons, average_speed):
        super().__init__(name, distance, fuel_cons, average_speed)
        self._mans = mans

    def fuel(self):
        return self._distance * self._fuel_cons * self._mans / 100


class Bus(LigthCar):
    pass


class Truck(Car):
    def __init__(self, name, weight, distance, fuel_cons, average_speed):
        super().__init__(name, distance, fuel_cons, average_speed)
        self.__weight = weight  # масса груза

    def fuel(self):
        return self._distance * self._fuel_cons * self.__weight / 100 /1000


l = LigthCar('Renault', 2, 350, 10, 50)
print(f'{l.name} - Расход: {l.fuel()} л')
print(f'{l.name} - Плановое время: {l.driving()} ч')

b = Bus('Fiat', 36, 200, 20, 40)
print(f'{b.name} - Расход: {b.fuel()} л')
print(f'{b.name} - Плановое время: {b.driving()} ч')

t = Truck('Man', 25000, 400, 15, 45)
print(f'{t.name} - Расход: {t.fuel()} л')
print(f'{t.name} - Плановое время: {t.driving()} ч')
