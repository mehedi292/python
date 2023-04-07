class A:
    def display(self):
        print("I am Inside of class A")

class B(A):
    def display1(A):
        print("I am Inside of class B")

class C(B):
    def display2(B):
        print("I am Inside of class C")

class D(C):
    def display3(C):
        print("I am Inside of class D")

object = D()
object.display1()
object.display2()
object.display3()
