"""payment.py"""
from abc import ABC, abstractmethod
from enum import Enum

class PayType(Enum):
    CASH = 1
    CARD = 2
    PHONE = 3

class Payment(ABC):
    """Payemnt Class"""
    @property #getter
    @abstractmethod
    def pay_type(self): #property
        pass

    @pay_type.setter #setter
    @abstractmethod
    def pay_type(self, val):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        for classname in C.__mro__:
            if classname.__name__ == cls.__name__:
                return True
        return False
