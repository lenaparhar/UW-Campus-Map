from abc import ABC, abstractmethod

class ShortestPathInterface(ABC):
    @abstractmethod
    def find_path(self, start, goal):
        pass
