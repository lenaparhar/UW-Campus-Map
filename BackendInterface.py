from abc import ABC, abstractmethod

class BackendInterface(ABC):
    @abstractmethod
    def add_edge(self, from_node, to_node, cost):
        pass

    @abstractmethod
    def get_path(self, start, goal):
        pass
