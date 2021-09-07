from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def amount_of_fabric(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self._v = v

    @property
    def amount_of_fabric(self):
        return self._v / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, h):
        self._h = h

    @property
    def amount_of_fabric(self):
        return 2 * self._h + 0.3


coat = Coat(45)
print(coat.amount_of_fabric)

costume = Costume(143)
print(costume.amount_of_fabric)
