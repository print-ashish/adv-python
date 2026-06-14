class Engine:

    def __init__(self):
        self.power = 125
    def m1(self):
        print("Engine functionality power :{}".format(self.power))


class Car:
    def __init__(self):
        self.engine = Engine()  #adding the functionality of engine class here with has a relation 

    def engineInfo(self):
        self.engine.m1()


c = Car()
c.engineInfo()

