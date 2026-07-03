class Person:
    def __init__(self,name , age):
        self.name = name
        self.age = age

    def display(self):
        print("name is ", self.name)
        print("age is ", self.age)



class Employee(Person):
    def __init__(self,name , age , salary , desg):  #constructor overriding 
        super().__init__(name , age)
        self.salary = salary
        self.desg = desg

    def display(self): #method overriding 
        super().display()
        print("salary is " , self.salary)
        print("desg is ", self.desg)

    

e = Employee("Ashish" , 26 , "70000", "AI Engineer")
e.display()