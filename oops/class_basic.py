class Student:
    """This is docstring for the class student """
    pass


# print(Student.__doc__)
# print(help(Student))


class Student:

    def __init__(self, name , roll):
        self.name = name
        self.roll = roll 

    def greet(self):
        print(f"hello from {self.name}")


s1 = Student("Ashish" , 4)

s1.greet()