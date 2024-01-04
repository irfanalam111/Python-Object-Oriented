class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name is:{self.name},age is:{self.age}"


class teacher:
    def __init__(self, salary, id):
        self.salary = salary
        self.id = id

    def __str__(self):
        return f"salary is {self.salary},id is{self.id}"


class student:
    def __init__(self, roll, marks):
        self.roll = roll
        self.marks = marks

    def __str__(self):
        return f"roll is:{self.roll},marks is:{self.marks}"


class information(person, teacher, student):
    super.__init__(self,name,age,salary,id,roll,marks)
    def __init__(self):
        self.name=name
        self.age=age
        self.id=id
        self.salary=salary
        self.roll=roll
        self.marks=marks
    def __str__(self):
        return(f"namr is {self.name},age is {self.age},id is {self.id},salary is {self.roll},mark is {self.marks}")



