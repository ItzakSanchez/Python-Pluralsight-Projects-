from abs_tree import AbstractTree

class Person(AbstractTree):

    def __init__(self, name, birthdate):
        self._name = name
        self._birthdate = birthdate

    @property
    def name(self):
        return self._name
    
    @property
    def birthdate(self):
        return self._birthdate
    
    def accept(self, visitor):
        visitor.visit_person(self)