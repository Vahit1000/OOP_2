# Задание 1.
#
#     Написать класс точка.
#         __init__, внутри которого будут определены координаты точки по осе абсцисс и ординат.
#         Начальные значения свойств берутся из входных параметров метода.
#         __str__ и/или __repr__ – x,y, цвет точки
#         методset_color, который задает цвет точки
#
#     Написать класс круг.
#         класс является потомком класса точка
#         __init__, внутри которого будут определены: координаты центра окружности и радиус
#         __str__ и/или __repr__ – x,y, радиус, цвет круга
#         метод area – возвращает площадь круга
#         метод set_radius -- позволяет изменить радиуса окружности
#
#     Написать класс сфера.
#         класс является потомком класса окружность
#         __init__, внутри которого будут определены: координаты центра, радиус.
#         метод volume – возвращает площадь круга
#         подумайте о том, как быть с методом area

from abc import ABC, abstractmethod
from enum import Enum, unique


@unique
class Color(Enum):
    BLACK = 0
    BROWN = 1
    GREEN = 3
    RED = 4
    YELLOW = 5
    BLUE = 6


class Point(ABC):

    @abstractmethod
    def __init__(self, x: int, y: int, color: Color):
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value < 0:
            self._x = 0
        else:
            self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if value < 0:
            self._y = 0
        else:
            self._y = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    def __str__(self):
        return f'X = {self._x}, Y = {self._y}, color: {self._color}'


class Circle(Point):
    def __init__(self, x, y, r, color):
        super().__init__(x, y, color)
        self._r = r

    def __str__(self):
        return f'X = {self._x}, Y = {self._y}, radius = {self._r}, color: {self._color}'

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, value):
        if value < 0:
            self._r = 0
        else:
            self._r = value

    def area(self):
        return 3.1415 * self._r ** 2



class Sphere(Circle):
    def __init__(self, x, y, r):
        super().__init__(x, y, r)

    def volume(self):
        return 4 * 3.1415 * self._r ** 2


# p = Point(10, 10, Color.RED)
# print(p)

c = Circle(50, 50, 20, Color.BLUE)
print(c)
print(c)
print(c.area())
