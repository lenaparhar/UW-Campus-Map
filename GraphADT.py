from abc import ABC, abstractmethod

class GraphADT(ABC):
    @abstractmethod
    def add_vertex(self, vertex):
        pass

    @abstractmethod
    def remove_vertex(self, vertex):
        pass

    @abstractmethod
    def add_edge(self, vertex1, vertex2, weight):
        pass

    @abstractmethod
    def remove_edge(self, vertex1, vertex2):
        pass

    @abstractmethod
    def get_neighbors(self, vertex):
        pass

    @abstractmethod
    def get_edge_weight(self, vertex1, vertex2):
        pass
