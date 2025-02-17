from my_class import MyClass
from null_class import NullClass
from my_object_factory import MyObjectFactory

myclass = MyObjectFactory.generate("MyClass")
myclass.do_something("Play videogames")

mynullclass = MyObjectFactory.generate("hello")
mynullclass.do_something("Sleep")