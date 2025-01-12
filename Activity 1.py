from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self, x):
        print("The value of x is",x)

    @abstractmethod

    def test_class(ABC):
        print("This is a abs method")

class childclass(Absclass):
    def test_class(self):
        print("This is child class")

t1 = childclass()
t1.test_class()
t1.print(100)