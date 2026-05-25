# from threading import *

# count = 0

# def increase():
#     global count
#     for i in range(10000000):
#         current = count + 1
#         count = current


# t1 = Thread(target = increase)
# t2 = Thread(target= increase)


# print("count = ", count )

# t1.start()
# t2.start()


# t1.join()
# t2.join()


# print("count = ", count )



from threading import *

count = 0

def increase(name):
    global count
    print(f"Thread {name} starting...")
    for i in range(10000000):
        current = count + 1
        count = current
    print(f"Thread {name} finished!")

t1 = Thread(target=increase, args=("A",))
t2 = Thread(target=increase, args=("B",))

t1.start()
t2.start()

t1.join()
t2.join()

print("count = ", count)
