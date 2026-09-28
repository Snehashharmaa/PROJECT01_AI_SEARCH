import os
import json
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

MAP_DATA_FILE = "map_data.json"


def load_map_data():
    """Load graph and location data from map_data.json if available."""
    if os.path.exists(MAP_DATA_FILE):
        try:
            with open(MAP_DATA_FILE, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading {MAP_DATA_FILE}: {e}")
    return {
        "region": "State / Metro Area",
        "total_cities": 0,
        "total_edges": 0,
        "locations": {},
        "graph": {}
    }


@app.route("/search", methods=["POST"])
def search():
    """Executes the selected search algorithm and returns the path, distance, and nodes expanded."""
    data = request.get_json() or {}
    start = data.get("start")
    goal = data.get("goal")
    algorithm = str(data.get("algorithm", "")).strip().lower()

    map_data = load_map_data()
    graph = map_data.get("graph", {})
    nodes = map_data.get("nodes", {})

    if not start or not goal or start not in graph or goal not in graph:
        return jsonify({"error": "Invalid start or destination city"}), 400

    result = None

    # Flexible string matching (handles hyphens, case, and short names)
    if "bfs" in algorithm or "breadth" in algorithm:
        result = bfs(graph, start, goal)
    elif "dfs" in algorithm or "depth" in algorithm:
        result = dfs(graph, start, goal)
    elif "ucs" in algorithm or "uniform" in algorithm:
        result = ucs(graph, start, goal)
    elif "ids" in algorithm or "iterative" in algorithm:
        result = ids(graph, start, goal)
    elif "greedy" in algorithm:
        result = greedy_best_first(graph, nodes, start, goal)
    elif "a*" in algorithm or "a_star" in algorithm or "a star" in algorithm:
        result = a_star(graph, nodes, start, goal)
    else:
        return jsonify({"error": f"Unknown algorithm selection: {algorithm}"}), 400

    if not result:
        return jsonify({"error": "No path found between cities"}), 404

    total_cost = round(result.get("cost", 0), 2)

    return jsonify({
        "path": result.get("path", []),
        "distance": total_cost,
        "cost": total_cost,
        "nodes_expanded": result.get("nodes_expanded", 0)
    })