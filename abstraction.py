from abc import ABC, abstractmethod

class shape(ABC):
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2


    # abstractmethod
    def area(self):
        # print("I am area method of shape class")
        pass
        

class Triangle(shape):
    def area(self):
        area = 0.5* self.dim1*self.dim2
        print("Area of Triangle: ", area)

class Rectangle(shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("Area of Rectangle :", area)
    



t1 = Triangle(10,20)
t1.area()

r2 = Rectangle(20,30)
r2.area()