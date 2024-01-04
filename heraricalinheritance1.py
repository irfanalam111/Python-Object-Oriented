class person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __str__(self):
        return f"age is:{self.age},name is:{self.name}"


class teacher(person):
    def __init__(self, age, name, salary, id):
        super().__init__(age, name)
        self.salary = salary
        self.id = id

    def __str__(self):
        return f"{super().__str__()},salary is:{self.salary}id is:{self.id}"


class student(person):
    def __init__(self, age, name, roll, mark):
        super().__init__(age, name)
        self.roll = roll
        self.mark = mark

    def __str__(self):
        return f"{super().__str__()},roll is:{self.roll},marks is:{self.mark}"


t = teacher(32, 'amit', 60000.0, 102)
s = student(19, 'ram', 30, 80.2)
print("data of student:", s)
print("data of teacher", t)
data_ = [t, s]
for x in data_:
    print(x)
