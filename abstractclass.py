from abc import ABC, abstractmethod

class absclass(ABC):
    def print(self, x):
        print("Passed: ", x)

    @abstractmethod
    def task(self):
        print("Inside Abstract Class.")

class test(absclass):
    def task(self):
        print("Inside Test Class.")

a=test()
a.task()
a.print(50)