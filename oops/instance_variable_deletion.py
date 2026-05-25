class Test:
    def __init__(self):
        self.a = 2
        self.b = 4
        self.c = 5



t = Test()
print(t.__dict__)

del t.a 
print(t.__dict__)