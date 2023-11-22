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

class Car:
    def __init__(self, name='', distance=0, fuel_cons=0, average_speed=0):
        self.__name__ = name
        self.__distance__ = float(distance)  # расстояние
        self.__fuel_cons__ = float(fuel_cons)  # удельный расход топлива
        self.__average_speed__ = float(average_speed)  # средняя скорость

    def get_name(self):
        return self.__name__

    def set_name(self, value):
        if isinstance(value, str):
            self.__name__ = value

    def get_distance(self):
        return self.__distance__

    def set_distance(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self.__distance__ = float(value)

    def det_fuel_cons(self):
        return self.__fuel_cons__

    def set_fuel_cons(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self.__fuel_cons__ = float(value)

    def driving(self):
        return self.__distance__ / self.__average_speed__


class LigthCar(Car):

    def __init__(self, name, mans, distance, fuel_cons):
        super().__init__(name, distance, fuel_cons)
        self.__mans__ = mans

    def fuel(self):
        return self.__distance__ * self.__fuel_cons__ * self.__mans__


class Bus(LigthCar):
    pass

class Truck(Car):
    def __init__(self, name, weight, distance, fuel_cons):
        super().__init__(name, distance, fuel_cons)
        self.__weight__ = weight

    def fuel(self):
        return self.__distance__ * self.__fuel_cons__ * self.__weight__

