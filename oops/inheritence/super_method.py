class Human:
    def __init__(self , name , age):
        self.name = name 
        self.age = age


    def action(self):
        print("walking and talking")



class Employee(Human):
    def __init__(self, name , age , work):
        super().__init__(name, age)
        self.work = work

    def details(self):
        print(f"name id {self.name} , age is {self.age} , work is {self.work}")


e = Employee("ash", 22 , "SDE")

e.details()