class P:
    def __init__(self):
        print("parent class constructor")

    def m1(self):
        print("parent class m1 method")


class C1(P):
    def __init__(self):
        print("child class constructor called")
    def m2(self):
        print("child class m2 method")


class C2(P):
    def __init__(self):
        print("child class constructor called")
    def m3(self):
        print("child class m2 method")


c1= C1()
c2 = C2()

c1.m2()
c1.m1()
c2.m3()
c2.m1()