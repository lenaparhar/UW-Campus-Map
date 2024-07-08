from abc import ABC, abstractmethod

class MapADT(ABC):
    @abstractmethod
    def put(self, key, value):
        pass

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def contains_key(self, key):
        pass

    @abstractmethod
    def remove(self, key):
        pass

    @abstractmethod
    def size(self):
        pass
