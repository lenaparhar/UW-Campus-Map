import sys
import os

sys.path.append(os.path.dirname(os.path.abspath('/Users/lenaparhar/Desktop/UW-Path-Finder-main')))

from Backend import Backend
from PlaceholderMap import PlaceholderMap
from parse_dot import parse_dot_file
from Frontend import Frontend

if __name__ == "__main__":
    backend = Backend()

    absolute_path = '/Users/lenaparhar/Desktop/UW-Path-Finder-main/campus.dot'
    edges = parse_dot_file(absolute_path)

    for from_node, to_node, cost in edges:
        backend.add_edge(from_node, to_node, cost)

    placeholder_map = PlaceholderMap()
    backend.graph.heuristic = placeholder_map.heuristic

    frontend = Frontend(backend)
    frontend.run()
