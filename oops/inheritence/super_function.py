class P:
    def m1(self):
        print("Parent method called ")


class C(P):
    def m1(self):
        super().m1() # this will call the parent class m1 method 
        print("Child class m1 method")


c = C()
c.m1()