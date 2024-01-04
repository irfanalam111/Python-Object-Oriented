import math
class circle:
    def __init__(self, radius):
        self.radius = radius

    def cla_area(self):
        return math.pi * math.pow(self.radius, 2)

    def cla_circum(self):
        return math.tau * self.radius

    def __str__(self):
        return f"area of circle: {self.cla_area()},circumferance of circle: {self.cla_circum()}"


class clynder(circle):
    def __init__(self, radius, hight):
        self.hight = hight
        super().__init__(radius)

    def cal_area(self):
        return 2 * super().cla_area() * self.hight

    def cal_circum(self):
        return super().cla_circum() * self.hight

    def __str__(self):
        return f"area of cylinder: {self.cal_area()},circumferance of cylinder:{self.cal_area()}"


class cone(clynder):
    def __init__(self, radius, hight):
        super().__init__(radius, hight)

    def call_area(self):
        return super().cla_area()

    def __str__(self):
        return f"{self.call_area()}"


c1 = clynder(12, 78)
c2 = cone(23, 89)
a = [c1, c2]
for x in a:
    print(x)
