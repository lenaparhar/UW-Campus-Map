import re

def parse_dot_file(file_path):
    edges = []
    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(r'"([^"]+)" -- "([^"]+)" \[seconds=([\d.]+)\];', line)
            if match:
                from_node = match.group(1)
                to_node = match.group(2)
                cost = float(match.group(3))
                edges.append((from_node, to_node, cost))
    return edges

