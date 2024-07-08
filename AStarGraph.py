import heapq
from BaseGraph import BaseGraph
from GraphADT import GraphADT

class AStarGraph(GraphADT, BaseGraph):
    def heuristic(self, node, goal):
        # Implement the heuristic function, e.g., Euclidean distance
        return 0

    def a_star(self, start, goal):
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, goal)}

        while open_set:
            current = heapq.heappop(open_set)[1]

            if current == goal:
                return self.reconstruct_path(came_from, current)

            for neighbor, cost in self.neighbors(current):
                tentative_g_score = g_score[current] + cost
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return None

    def reconstruct_path(self, came_from, current):
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.append(current)
        return total_path[::-1]

    def add_vertex(self, vertex):
        if vertex not in self.edges:
            self.edges[vertex] = []

    def remove_vertex(self, vertex):
        if vertex in self.edges:
            del self.edges[vertex]
        for edges in self.edges.values():
            edges[:] = [(v, w) for v, w in edges if v != vertex]

    def add_edge(self, vertex1, vertex2, weight):
        super().add_edge(vertex1, vertex2, weight)
        super().add_edge(vertex2, vertex1, weight)

    def remove_edge(self, vertex1, vertex2):
        self.edges[vertex1] = [(v, w) for v, w in self.edges[vertex1] if v != vertex2]
        self.edges[vertex2] = [(v, w) for v, w in self.edges[vertex2] if v != vertex1]

    def get_neighbors(self, vertex):
        return super().neighbors(vertex)

    def get_edge_weight(self, vertex1, vertex2):
        for v, w in self.edges[vertex1]:
            if v == vertex2:
                return w
        return None
