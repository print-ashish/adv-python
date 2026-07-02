class Test:
    def m1(self, *args , **kwargs):
        # print(*args)
        print("type of args is" , type(args))
        for num in args:
            print(num)

        for key , value in kwargs.items():
            print("key == ", key , "value = ", value)


t = Test()

# t.m1(3)
# t.m1(55, 3)
t.m1(34,5,2,name="Ashish", age = 25)