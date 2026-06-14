class P:

    def __init__(self):
        print("parent class constructor called")

    def m1(self):
        print("parent class m1 method")




class C(P):
    def __init__(self):   #it looks like constructor over ridding 
        print("child class constructor called")

    def m2(self):
        print("child class m2 method")


c = C()
c.m1()
c.m2()