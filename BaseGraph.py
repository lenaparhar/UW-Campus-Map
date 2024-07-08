class BaseGraph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, from_node, to_node, cost):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, cost))

    def neighbors(self, node):
        return self.edges.get(node, [])
