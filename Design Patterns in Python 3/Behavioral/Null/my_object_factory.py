from my_class import MyClass
from null_class import NullClass

class MyObjectFactory():
    
    @staticmethod
    def generate(objectName):
        if objectName == "MyClass":
            return MyClass()
        else:
            return NullClass()