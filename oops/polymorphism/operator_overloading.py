class Book :
    def __init__(self,pages):
        self.pages = pages 

    def __add__(self,other):
        return self.pages + other.pages 


b1 = Book(100)
b3 = Book(34)
b2 = Book(200)



# print(b1 + b2)    #supported for 2 objects
# print(b1 + b2 + b3) # no supported to add 3 objects 

# Example 2 


class Student:
    def __init__(self , roll , marks):
        self.roll = roll
        self.marks = marks 
    def __gt__(self, other):
        res = self.marks > other.marks
        return res 

    def __lt__(self, other):
        return self.marks < other.marks
    
    def __le__(self, other):
        return self.marks <= other.marks

    def __ge__(self, other):
        return self.marks >= other.marks
    
    def __str__(self):
        return "ROll no of the student " + str(self.roll)

s1 = Student(2, 500)
s2 = Student(3 , 400)


# print(s1 <= s2)

# print(s1  >= s2)


#__str__() method

# print(s1.__repr__())
# print(s1)


#lets try to add the 3 objects with the operator overloading 


class Book :
    def __init__(self, pages):
        self.pages = pages 

    def __add__(self, other):
        return Book(self.pages + other.pages)

    def __str__(self):
        return str(self.pages)
    
    def __mul__(self, other):
        return Book(self.pages * other.pages)


b1 = Book(100)
b2 = Book(200)
b3 = Book(40)

print(b1 + b2 + b3) #first it will be called for b1 + b2 then again the object with the b3 
print(b1 + b2 * b3)   #multiplication will happen as per the operator precedence then addition 