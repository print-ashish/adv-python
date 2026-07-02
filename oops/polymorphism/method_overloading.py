class Test:
    def m1(self):
        print("no arg m1")


    def m1(self, x):
        print("single arg m1")

    def m1(self, x , y):
        print("method with 2 arg")  #this is the last m1 to this is only considered 


t = Test() 

t.m1() #will throw error 
t.m1(3,4) #will work