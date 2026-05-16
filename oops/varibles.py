class Student:
    college = "Banaras Hindu University" ## this is class level static variable which is available for all the object is is having only one reference 

    def __init__(self, name):
        self.name = name  ## this is instance variable 

    def count(self):
        n = 4   ### this is local variable for the function 
        for i in range(n):
            print(i) 

s1 = Student("ashish")
print(s1.college)
print(s1.name)
s1.count()