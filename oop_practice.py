class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self,amount):
        self.salary+= amount


    def show_details(self):
        print(f"Employee : {self.name} , Salary {self.salary}")


# emp1 = Employee("Alice",500000)
# emp1.give_raise(5000)
# emp1.show_details()


class Developer(Employee):
    def __init__(self,name,salary,tech_stack):
        super().__init__(name,salary) 
        self.tech_stack = tech_stack

    def show_details(self):
        print(f"Employee : {self.name} , Salary {self.salary} , tech stack {self.tech_stack}")


dev1 = Developer("Alex",80000,["python","system design"])
dev1.show_details()