class Test:
    a = 30
    def __init__(self):
        self.a = 999 #instance variable can't modify the static variable , rather a new instane variable a will be created for the object 




t1 = Test()
print(Test.a)
print(t1.a)