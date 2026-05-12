def decor1(func):
    def inner1():
        print("hello from decor 1")
        func()

    return inner1 

def decor2(func):
    def inner2():
        print("hello from decor 2 ")
        func()

    return inner2  



@decor2  #############last decorator output will be printer bcz last inner function is executed 

@decor1
def f1():
    print("hello from f1 ")


f1()