# Создать класс Circle на базе класса Point
# Класс должен поддерживать все методы родительского класса, а так же:
# минимальное расстояние от окружности до центра координат;
# площадь окружности и длину окружности.


import math
from task_01 import Point


class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __str__(self):
        return super().__str__()[:-1] + f', radius={self.radius})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        radius = self.radius + other.radius
        return Circle(radius, x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        radius = abs(self.radius - other.radius)
        if radius == 0:
            answer = Point(x, y)
        else:
            answer = Circle(radius, x, y)
        return answer


    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)

    def circumference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius**2)


if __name__ == '__main__':
    circle_1 = Circle(3, 1, 2)
    print(circle_1)
    circle_2 = Circle(7, 1, 3)
    print(circle_2)

    circle_3 = circle_1 - circle_2
    if type(circle_3) == Point:
        print('Circle_3 is Point: ', circle_3)
        print('Type circle_3: ', type(circle_3))
        print('Distance_from_origin: ', circle_3.distance_from_origin())
    else:
        print('Circle_3 is Circle: ', circle_3)
        print('Type circle_3: ', type(circle_3))
        print('Edge_distance_from_origin: ', circle_3.edge_distance_from_origin())
        print('Distance_from_origin: ', circle_3.distance_from_origin())
        print('Circumference: ', circle_3.circumference())
        print('Area: ', circle_3.area())

    print('-'*50)
    circle_11 = Circle(7, 0, 2)
    print(circle_11)
    circle_22 = Circle(7, 15, 3)
    print(circle_22)
    circle_7 = circle_11 - circle_22
    if type(circle_7) == Point:
        print('Circle_7 is Point: ', circle_7)
        print('Type circle_7: ', type(circle_7))
        print('Distance_from_origin: ', circle_7.distance_from_origin())
    else:
        print('Circle_7 is Circle: ', circle_7)
        print('Type circle_7: ', type(circle_7))
        print('Edge_distance_from_origin: ', circle_7.edge_distance_from_origin())
        print('Distance_from_origin: ', circle_7.distance_from_origin())
        print('Circumference: ', circle_7.circumference())
        print('Area: ', circle_7.area())
