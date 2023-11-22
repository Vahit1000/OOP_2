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

class Point:
    __color__ = ''

    def __init__(self, X, Y):
        self.__X__ = X
        self.__Y__ = Y

    def set_color(self, color):
        if isinstance(color, str):
            self.__color__ = color

    def __str__(self):
        return f'X = {self.__X__}, Y = {self.__Y__}, color: {self.__color__}'


class Circle(Point):
    def __init__(self, X, Y, R):
        super().__init__(X, Y)
        self.__R__ = R

    def __str__(self):
        return f'X = {self.__X__}, Y = {self.__Y__}, radius = {self.__R__}, color: {self.__color__}'

    def area(self):
        return 3.1415 * self.__R__ ** 2

    def set_radius(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self.__R__ = value


class Sphere(Circle):
    def __init__(self, X, Y, R):
        super().__init__(X, Y, R)

    def volume(self):
        return 4 * 3.1415 * self.__R__ ** 2


p = Point(10, 10)
p.set_color("green")
print(p)

c = Circle(50, 50, 20)
c.set_color("red")
print(c)
c.set_radius(50.8)
print(c)
print(c.area())
