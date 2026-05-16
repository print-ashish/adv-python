##the self denotes the method is instance method bcz the method is using the intstance variable inside it

class Student:

    def __init__(self, name):
        self.name = name 

    def get_info(self):
        print("hello i am , ", self.name)
        


s1 = Student("Ashish")
s1.get_info()
