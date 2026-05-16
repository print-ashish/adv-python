
# here cls is the reference variable for the class level object  

class Student:
    schoolname = "ABC"


    @classmethod
    def get_school_info(cls):
        print("school name is ", cls.schoolname)
        print("id of cls == " , id(cls))


# s1 = Student()
# s1.get_school_info()

Student.get_school_info()

print(id(Student))