from enum import StrEnum
class Test:

    def __init__(self):
        print("hello from the constructor , id == " , id(self))



# t = Test()
# t.__init__()  ##if we call like this it wont create new object 


##in python there is no such concept of contructor overloading and method overloading 


class Student : 
    def __init__(self):
        print("no arg constructor ")

    def __init__(self , x) :
        print("constructor with 1 arg ")

# s1 = Student()  #will throw error since last constructor is valid one 

s2 = Student(4)