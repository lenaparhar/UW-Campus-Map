from MapADT import MapADT

class PlaceholderMap(MapADT):
    def __init__(self):
        self.map = {}

    def put(self, key, value):
        self.map[key] = value

    def get(self, key):
        return self.map.get(key, None)

    def contains_key(self, key):
        return key in self.map

    def remove(self, key):
        if key in self.map:
            del self.map[key]

    def size(self):
        return len(self.map)

    @staticmethod
    def heuristic(node, goal):
        return abs(len(node) - len(goal))
