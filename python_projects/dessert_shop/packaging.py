"""packaging.py"""
from abc import ABC, abstractmethod
class Packaging(ABC):
    """Packaging class"""
    @property
    @abstractmethod
    def packaging(self):
        pass

    @packaging.setter
    @abstractmethod
    def packaging(self, val):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        for classname in C.__mro__:
            if classname.__name__ == cls.__name__:
                return True
        return False