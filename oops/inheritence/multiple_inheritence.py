class P1():
    def m1(self):
        print("p1 m1 method called")

class P2():
    def m1(self):
        print("p2 m1 method called")

class C(P1,P2):
    def m3(self):
        print("child m3 called ")


c = C()
c.m1()