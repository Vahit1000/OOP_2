# Написать класс - Student
#
# Напишите программу с классом Student, в котором есть три атрибута: name, group_number и age.
# По умолчанию name = Ivan, age = 18, group_number = 10A. Необходимо создать методы:
#
#     get_name
#     get_age
#     get_group_number
#     set_name
#     set_age
#     set_group_number В программе необходимо создать пять экземпляров класса Student,
#     установить им разные имена, возраст и номер группы.


class Student:

    def __init__(self, name='Ivan', age=18, group_number='10A'):
        self.__name__ = name
        self.__age__ = age
        self.__group_number__ = group_number

    def get_name(self):
        return self.__name__

    def set_name(self, value):
        self.__name__ = value

    def get_age(self):
        return self.__age__

    def set_age(self, value) -> int | None:
        if isinstance(value, int):
            self.__age__ = value
        else:
            return None

    def get_number(self):
        return self.__group_number__

    def set_number(self, value):
        self.__group_number__ = value


p1 = Student()
print(f'name: {p1.get_name()}, age: {p1.get_age()}, number group: {p1.get_number()}')
p2 = Student('Lisa', 20, '11B')
print(f'name: {p2.get_name()}, age: {p2.get_age()}, number group: {p2.get_number()}')
p3 = Student('Kate', 19, '09C')
print(f'name: {p3.get_name()}, age: {p3.get_age()}, number group: {p3.get_number()}')
p4 = Student('Dina', 17, '08A')
print(f'name: {p4.get_name()}, age: {p4.get_age()}, number group: {p4.get_number()}')
p5 = Student('Alsu', 21, '07E')
print(f'name: {p5.get_name()}, age: {p5.get_age()}, number group: {p5.get_number()}')

