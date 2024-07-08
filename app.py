from flask import Flask, request, jsonify
from flask_cors import CORS
from Backend import Backend
from PlaceholderMap import PlaceholderMap
from parse_dot import parse_dot_file

app = Flask(__name__)
CORS(app)

backend = Backend()
absolute_path = '/Users/lenaparhar/Desktop/UW-Path-Finder-main/campus.dot'
edges = parse_dot_file(absolute_path)

for from_node, to_node, cost in edges:
    backend.add_edge(from_node, to_node, cost)

placeholder_map = PlaceholderMap()
backend.graph.heuristic = placeholder_map.heuristic  # Set the heuristic function

@app.route('/find_path', methods=['POST'])
def find_path():
    data = request.get_json()
    start = data.get('start')
    goal = data.get('goal')
    path = backend.get_path(start, goal)
    if path:
        return jsonify({"path": path}), 200
    else:
        return jsonify({"error": "Path not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
