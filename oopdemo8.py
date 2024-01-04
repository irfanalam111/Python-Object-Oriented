class emp:
    @classmethod
    def raise_amo(cls):
        emp.raise_amount = eval(input("enter raise amount"))

    def __init__(self, name, id, amount):
        self.name = name
        self.id = id
        self.amount = amount

    def increse_raise_amount(self):
        self.amount = self.amount + (self.amount * emp.raise_amo() / 100)

    def display(self):
        print(self.amount, self.id, self.name)


e1 = emp('amit', 102, 50000)
print("before incresing")
e1.display()
print("after incressing....")
e1.increse_raise_amount()
e1.display()
