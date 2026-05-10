def my_gen():
    print("starting")
    yield "Snack 1"

    print("resuming")
    yield "snack 2"

    print("finalizing ")
    yield "snack 3"


# machine = my_gen()

# print(next(machine))

# print(next(machine))


# print(next(machine))


def countdown(n):
    while n > 0:
        yield n
        n-=1


for num in countdown(5):
    print(num)