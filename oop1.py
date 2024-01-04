class book:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"name is {self.name},price is{self.price}"

    def __add__(self, other):
        name = (self.name, other.name)
        price = self.price + other.price
        temp = book(name, price)
        return temp


b1 = book("python", 500)
b2 = book("java", 700)
b3 = b1 + b2
print(b1)
print(b2)
print(b3)
