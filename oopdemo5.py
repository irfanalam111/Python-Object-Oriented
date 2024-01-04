class student:
    stream = 'CSE'

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
    # def show(self):
    #     print("name is:",self.name)
    #     print("roll is :",self.roll)


e1 = student("amit", 102)
e2 = student("ram", 102)
stream = 'electrical'
print(e1.name, e1.roll, e1.stream)
print(e2.name, e2.roll, e2.stream)
