class person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def getname(self):
        return self.name

    def getage(self):
        return self.age


class student:
    def __init__(self, roll, grade):
        self.grade = grade
        self.roll = roll

    def getroll(self):
        return self.roll

    def getgrade(self):
        return self.grade


class scincestudent(person, student):
    def __init__(self, age, name, roll, grade, stream):
        person.__init__(self, age, name)
        student.__init__(self, roll, grade)
        self.stream = stream

    def getstraem(self):
        return self.stream


sc = scincestudent(16, 'mohit', 102, 76.9, 'math')
print("name is:", sc.getname())
print("age is:", sc.getage())
print("roll is:", sc.getroll())
print("grade is:", sc.getgrade())
print("stream is:", sc.getstraem())
