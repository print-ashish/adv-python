
#here static method are just general purpose methods
class Student:
    schoolname = "ABC"


    @classmethod
    def get_school_info(cls):
        print("school name is ", cls.schoolname)
        print("id of cls == " , id(cls))

    @staticmethod
    def get_sum(a , b):
        print(a + b)


# s1 = Student()
# s1.get_school_info()

Student.get_sum(3,5)