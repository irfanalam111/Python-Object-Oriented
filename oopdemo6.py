class emp:
    increse_sal = 8.6

    def __init__(self, name, sall, id):
        self.name = name
        self.sall = sall
        self.id = id

    def incre_sal(self):
        self.sall = self.sall + (self.sall + emp.increse_sal / 100)

    def display(self):
        print('name:', self.name, 'salray:', self.sall, 'id:', self.id)


e1 = emp('amit', 60000.0, 102)
e2 = emp('ram', 8000.0, 103)
print("before incressing.....")
e1.display()
e2.display()
e1.incre_sal()
e2.incre_sal()
print("after incesing.....")
e1.display()
e2.display()
