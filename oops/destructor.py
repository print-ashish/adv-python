import time
class Test:
    def __init__(self):
        print("object creation ")

    def __del__(self):
        print("cleanup process ")   


# t = Test()
# t = None #now the gc will automatically call the __del__ since object has no refernece

# time.sleep(10)



lst = [Test(), Test(), Test()]
#if the lst is deleted then automatically the objects inside will be deleted too

del lst