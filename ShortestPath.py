from ShortestPathInterface import ShortestPathInterface

class ShortestPath(ShortestPathInterface):
    def __init__(self, backend):
        self.backend = backend

    def find_path(self, start, goal):
        return self.backend.get_path(start, goal)
