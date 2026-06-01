class Test:
    a = 20
    b = 49

    @classmethod
    def m1(cls):
        # del cls.a  even with this or with the class name  
        del Test.a

    @staticmethod
    def m2():
        del Test.b #it is also possible to del with the class name inside the static method  



print(Test.a)
Test.m2()
print(Test.a)
