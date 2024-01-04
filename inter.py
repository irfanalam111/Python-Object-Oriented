import math
class circle:
    def __init__(self,radius):
        self.radius=radius

    def __str__(self):
        area=math.pow(2,self.radius)
        circ=math.tau*self.radius
        return f"area of circle{area}, circumferance of circle {circ}"
class clynder(circle):
    def __init__(self,height):
        super().__init__(self)

    