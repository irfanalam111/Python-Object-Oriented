class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f" name is: {self.name},age is: {self.age}"


class student(person):
    def __init__(self, name, age, roll, grade):
        self.roll = roll
        self.grade = grade
        super().__init__(name, age)

    def __str__(self):
        return f"{super().__str__()},roll is: {self.roll},grade is: {self.grade}"


class teacher(person):
    def __init__(self, name, age, salary):
        self.salary = salary
        super().__init__(name, age)

    def __str__(self):
        return f"{super().__str__()},salary is: {self.salary}"


s1 = student('amit', 29, 39, 90)
t1 = teacher('ram', 53, 60000)
l1 = [s1, t1]
for x in l1:
    print(x)
