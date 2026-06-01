from os import stat
class Outer:

    def __init__(self):
        print("outer class object creation")

    class Inner:
        def __init__(self):
            print("inner class object creation ")


        class InnerInner():
            
            def __init__(self):
                print("inner inner object creation")

            
            @staticmethod
            def m1():
                print("m1 from the inner inner class")


# o = Outer()

# i = o.Inner()

# i.m1()


# ii = Outer().Inner().InnerInner.m1()



class Human:
    def __init__(self , name):
        self.name = name 
        self.head = self.Head()


    def info(self):
        print("hello i am ", self.head.talk())
        print("my brain is" , self.head.brain.think())
    class Head:
        def talk(self):
            self.brain = self.Brain()
            print("talking")

        class Brain:

            def think(self):
                print("thinking")




# human = Human("ashish")
# human.info()



class Person:
    def __init__(self,name,dd,mm,yyyy):
        self.name = name
        self.dob = self.DOB(dd,mm,yyyy)

    def info(self):
        self.dob.show_dob()


    class DOB:
        def __init__(self,dd,mm,yyyy):
            self.dd = dd
            self.mm =  mm
            self.yyyy = yyyy 
        
        def show_dob(self):
            print("{}/{}/{}".format(self.dd,self.mm,self.yyyy))


p = Person("Ashish","02","03","2000")
p.info()