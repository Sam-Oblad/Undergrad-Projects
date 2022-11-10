"""
Interface
"""
from abc import ABC, abstractmethod
from typing import TypeVar

T = TypeVar("T") #Anything

class SameItem(ABC):
    """SameItem Class"""
    @abstractmethod
    def is_same_as(self:T, other:T)->bool:
        "abstract method passed to Cookie and Candy Subclasses"

    @classmethod
    def __subclasshook__(cls, C):
        method_name = "is_same_as"
        if cls is SameItem:
            #Checks if C implements method_name
            if method_name in C.__dict__:
                if C.__dict__[method_name] is None:
                    return NotImplemented
            else:
                return NotImplemented
            return True
        return NotImplemented
