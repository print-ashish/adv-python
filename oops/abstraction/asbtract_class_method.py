from abc import abstractmethod , ABC


class Vehicle(ABC):

    @abstractmethod
    def noOfWheels(self):
        pass



class Auto(Vehicle):

    def noOfWheels(self):
        print("auto wheel implementation")
        return 3



a = Auto()
print(a.noOfWheels())