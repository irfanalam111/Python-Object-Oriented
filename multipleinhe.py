class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name is {self.name},age is {self.age}"


class emp(person):
    def __init__(self, name, age, id, sall):
        self.id = id
        self.sall = sall
        super().__init__(name, age)

    def income(self):
        return self.sall

    def __str__(self):
        return f"{super().__str__()} id is{self.id},salary is{self.sall}"


class maneger(emp):
    def __init__(self, name, age, id, sall, bonus):
        self.bonus = bonus
        super().__init__(name, age, id, sall)

    def income(self):
        total = super().income() + self.bonus

    def __str__(self):
        return f"{super().__str__(), self.income()}"


e = maneger('amit', 29, 102, 60000, 5000)
print(e)
