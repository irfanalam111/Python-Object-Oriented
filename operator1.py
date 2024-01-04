class distance:
    def __init__(self, inch, feet):
        self.inch = inch
        self.feet = feet

    def __str__(self):
        return f"inch is {self.inch},feet is {self.feet}"

    def __add__(self, other):
        feet = self.feet + other.feet
        inch = self.inch + other.inch
        if inch >= 12:
            feet = feet + inch // 12
            inch = inch % 12
        temp = distance(feet, inch)
        return temp


d1 = distance(10, 5)
d2 = distance(12, 9)
d3 = d1 + d2
print(d3)
print(d1)
print(d2)
