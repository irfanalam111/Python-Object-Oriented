import math


class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * math.pow(self.radius, 2)


class cylinder(circle):
    def __init__(self, hight, radius):
        super().__init__(radius)
        self.hight = hight

    def area(self):
        return super().area() * 2 + math.tau * self.hight * self.hight

    def volume(self):
        return super().area() * self.hight


obj = cylinder(10, 5)
print(obj.area())
print(obj.volume())
