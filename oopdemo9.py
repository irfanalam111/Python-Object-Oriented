import math


class box:
    def __init__(self, l, b, h):
        self.l = l
        self.b = b
        self.h = h

    def __str__(self):
        return f"lenghth is: {self.l},bregth is: {self.b},hight is: {self.h}"


class squre(box):
    def __init__(self, l, b, h):
        super().__init__(l, b, h)

    def cal_area(self):
        math.pow(self.l, 2)

    def cla_circum(self):
        c = self.l * 4

    def __str__(self):
        return f"area is :{self.cal_area()},{self.cla_circum()} "


class ractangle(box):
    def __init__(self, l, b, h):
        super().__init__(l, b, h)

    def cal_area(self):
        a = self.l * self.b


a = squre(2, 1, 1)
print(a)
