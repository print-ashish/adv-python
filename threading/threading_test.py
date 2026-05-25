from threading import *
import time 



def greet_hello():
    for i in range(10):
        time.sleep(2)
        print("hello Ashish" , i)


def greet_bye():
    for i in range(10):
        # time.sleep(2)
        print("Bye Ashish" , i)



t1 = Thread(target=greet_hello)
t2 = Thread(target = greet_bye)


t1.start()
t2.start()


l = enumerate()

for elem in l:
    print(elem)