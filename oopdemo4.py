import math


class circle:
    def __init__(self, radius):
        self.radius = radius

    def cal_area(self):
        return math.pi * math.pow(self.radius, 2)

    def cal_circumferance(self):
        return math.tau * self.radius

    def show(self):
        print("area is :", self.cal_area())
        print("circumferance is :", self.cal_circumferance())


rad = int(input("enter length of radius"))
e1 = circle(rad)
e1.show()
