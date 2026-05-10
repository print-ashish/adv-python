class Human:
    
    @staticmethod
    def greet():
        print("hello human")
    @staticmethod
    def is_valid_password(password):
        if len(password) > 8:
            return True
        else: 
            return False



print(Human.is_valid_password("abcd"))
h = Human()
h.is_valid_password("test")