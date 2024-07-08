from BackendInterface import BackendInterface
from AStarGraph import AStarGraph

class Backend(BackendInterface):
    def __init__(self):
        self.graph = AStarGraph()

    def add_edge(self, from_node, to_node, cost):
        self.graph.add_edge(from_node, to_node, cost)

    def get_path(self, start, goal):
        return self.graph.a_star(start, goal)
