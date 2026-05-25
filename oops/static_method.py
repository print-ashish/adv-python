
#here static method are just general purpose methods
class Student:
    schoolname = "ABC"


    @classmethod
    def get_school_info(cls):
        cls.university = "BHU"
        Student.college ="RGSC"
        print("school name is ", cls.schoolname)
        print("id of cls == " , id(cls))
        

    @staticmethod
    def get_sum(a , b):
        Student.professor_name = "John doe"
        print(a + b)


s1 = Student()
s1.schoolname = "my school"
# s1.get_school_info()

Student.get_sum(3,5)
print(Student.schoolname)
Student.schoolname = "XYZ"
Student.get_school_info()
print(Student.schoolname)
# Student.get_sum()
print(Student.university)
print(Student.college)
print(Student.professor_name)