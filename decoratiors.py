from typing import Callable
from codecs import getincrementaldecoder
def greet():
    print("hello ashish")




#function aliasing 
# print(type(greet))
# print(id(greet))

# new_greet = greet

# print(type(new_greet))
# print(id(new_greet))


##fuction as argument 

def func1(func1 : Callable):
    func1()



def f1():
    print("hello from f1")

# func1(f1)

##function returning another function 


def outer():
    def inner():
        print("hello from the inner function ")

    return inner



# res = outer()

# res()


############lets implement the deorator function 


def decor(func):
    def inner(name:str):
        print(f"hello from the decorator {name}")

    return inner 



@decor 
def display(name : str):
    print(f"hello displaying {name}")


# display("ashish")


 
##lets create decorator with arguments and performing operation

def decor_add_nums(func):
    def inner(a  , b):
        print("*"*50)
        print(func(a, b))
        print("*"*50)

    return inner 

@decor_add_nums
def add_num(a , b) :
    return (a + b)


add_num(3,5 )



