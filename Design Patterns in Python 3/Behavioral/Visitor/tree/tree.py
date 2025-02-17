from abs_tree import AbstractTree
from null_person import NullPerson
from collections import Iterable
from functools import reduce


class Tree(AbstractTree, Iterable):

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
        visitor.visit_tree(self)
        for node in self:
            node.accept(visitor)