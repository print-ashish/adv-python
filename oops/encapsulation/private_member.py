class Test:
    def __init__(self):
        self.__x =  23

    
    def __m1(self):
        print("private method m1 called")



t = Test()

# print(t.__x) #will not allow since its private 

print(t._Test__x) #this will allow due to same mangling concept of the __x named to _Test__x



t.m1()  #not allowed
t._Test__m1()  #allowed similarly for this this is such a cool thing 