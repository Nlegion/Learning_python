from math import pi


class Figure:
    unit = 'm'

    def __init__(self):
        self._area = None
        self._calc_area()

    def get_area(self):
        return self._area

    def _calc_area(self):
        pass

    def __str__(self):
        return f'{self.__class__.__name__}: {self._area:.2f} {self.unit}^2'


class Circle(Figure):
    def __init__(self, r):
        self._r = r
        super().__init__()  # self._area = None

    def _calc_area(self):
        self._area = pi * self._r ** 2


class Box(Figure):
    def __init__(self, w, h):
        self._w = w
        self._h = h
        super().__init__()

    def _calc_area(self):
        self._area = self._w * self._h


circle_1 = Circle(r=15)
# print(circle_1.get_area())
print(circle_1)

box_1 = Box(w=20, h=30)
print(box_1.get_area())
print(box_1)
