import math


class circle:
    def __init__(self, radius):
        self.radius = radius

    def cal_area(self):
        self.area = math.pi * math.pow(self.radius, 2)

    def cal_circ(self):
        self.circ = math.tau * self.radius

    def show(self):
        print("area is:", self.area)
        print("circumferance is:", self.circ)


rad = int(input("enter length of circle"))
e1 = circle(rad)
e1.cal_circ()
e1.cal_area()
e1.show()
