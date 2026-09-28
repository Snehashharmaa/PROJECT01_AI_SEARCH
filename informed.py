import math
import heapq

def haversine(coord1, coord2):
    """Straight-line distance (heuristic) in miles between two lat/lon pairs."""
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    R = 3958.8  # Earth radius in miles

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


def greedy_best_first(graph, nodes, start, goal):
    """Greedy Best-First Search using h(n)"""
    goal_coord = (nodes[goal]["lat"], nodes[goal]["lon"])
    
    def h(city):
        city_coord = (nodes[city]["lat"], nodes[city]["lon"])
        return haversine(city_coord, goal_coord)

    pq = [(h(start), [start])]
    visited = set()
    nodes_expanded = 0

    while pq:
        _, path = heapq.heappop(pq)
        node = path[-1]

        if node == goal:
            cost = sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))
            return {"path": path, "cost": cost, "nodes_expanded": nodes_expanded}

        if node not in visited:
            visited.add(node)
            nodes_expanded += 1
            for neighbor in graph.get(node, {}):
                if neighbor not in visited:
                    heapq.heappush(pq, (h(neighbor), path + [neighbor]))

    return {"path": [], "cost": float("inf"), "nodes_expanded": nodes_expanded}


def a_star(graph, nodes, start, goal):
    """A* Search using f(n) = g(n) + h(n)"""
    goal_coord = (nodes[goal]["lat"], nodes[goal]["lon"])

    def h(city):
        city_coord = (nodes[city]["lat"], nodes[city]["lon"])
        return haversine(city_coord, goal_coord)

    pq = [(h(start), 0, [start])]
    visited = set()
    nodes_expanded = 0

    while pq:
        f_score, g_score, path = heapq.heappop(pq)
        node = path[-1]

        if node == goal:
            return {"path": path, "cost": g_score, "nodes_expanded": nodes_expanded}

        if node not in visited:
            visited.add(node)
            nodes_expanded += 1
            for neighbor, distance in graph.get(node, {}).items():
                if neighbor not in visited:
                    new_g = g_score + distance
                    new_f = new_g + h(neighbor)
                    heapq.heappush(pq, (new_f, new_g, path + [neighbor]))

    return {"path": [], "cost": float("inf"), "nodes_expanded": nodes_expanded}
