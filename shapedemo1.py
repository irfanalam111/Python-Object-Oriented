import math
class shape:
    def __init__(self,height,radius,side):
        self.height=height
        self.radius=radius
        self.side=side
    def __str__(self):
        return f"height is : {self.height},radius is : {self.radius},side is : {self.side}"
class circle(shape):
    def __init__(self,radius,height,side):
        self.radius=radius
        super().__init__(radius,height,side)
        area=math.pow(2,radius)
        circumferance=math.tau*radius
        print("area of circle : ",area,"area of circumferance : ",circumferance)
class tringle(shape):
    def __init__(self,side,height,radius):
        self.side=side
        super().__init__(height,side,radius)
        area=1/2*math.pow(2,side)
        circumferance=3*side
        print("area of tringle : ",area,"circumferance of tringle : ",circumferance)
class cylinder(shape):
    def __init__(self,side,height,radius):
        self.height=height
        self.radius=radius
        super().__init__(height,side,radius)
        volume=math.pow(2,radius*height)
        circumferance=math.tau*radius*height
        area=2*math.tau*radius+2*math.pi*height
        print("area of cylinder : ",area,"circumferanc eof cylinder : ",circumferance,"volume of cylinder : ",volume)

