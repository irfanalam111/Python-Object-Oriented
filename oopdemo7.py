class EMP:
    @classmethod
    def set_raise_amount(cls):
        EMP.set_raise_amount = eval(input("enter raise amount"))

    def __init__(self, name, sall, id):
        self.name = name
        self.sall = sall
        self.id = id

    def raise_amount(self):
        self.sall = self.sall + (self.sall * EMP.set_raise_amount / 100)

    def display(self):
        print('name:', self.name, 'salray:', self.sall, 'id:', self.id)


e1 = EMP('amit', 60000.0, 102)
e2 = EMP('ram', 8000.0, 103)
print("before incressing.....")
e1.display()
e2.display()
e1.raise_amount()
e2.raise_amount()
print("after incesing.....")
e1.display()
e2.display()
