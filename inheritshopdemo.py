class person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def getname(self):
        return self.name

    def getage(self):
        return self.age


class worker:
    def __init__(self, salary, work):
        self.salary = salary
        self.work = work

    def getsalary(self):
        return self.salary

    def getwork(self):
        return self.work


class woner:
    def __init__(self, money, shopname):
        self.money = money
        self.shopname = shopname

    def getmoney(self):
        return self.money

    def getshopname(self):
        return self.shopname


class shop(person, worker, woner):
    def __init__(self, location):
        self.location = location
        person.__init__(self, age, n)
