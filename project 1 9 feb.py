from abc import ABC, abstractmethod
class ABSclass(ABC):
    def print(self,x):
        print("passed value:",x)
    @abstractmethod
    def task(self):
        print(" we are inside absclass task")
class test__(ABSclass):
    def task(self):
        print(" we are inside test__ class task")
test__obj=test__()
test__obj.task()
test__obj.print(100)