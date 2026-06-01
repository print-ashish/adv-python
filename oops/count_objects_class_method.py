class Test:

    count = 0

    def __init__(self):
        Test.count = Test.count + 1

    @classmethod
    def getTotalObjects(cls):
        print("total objects == ", cls.count)

    def getTotal():
        print("total object from the static method ", Test.count)


t1 = Test()
t2 = Test()

Test.getTotalObjects()
Test.getTotal()