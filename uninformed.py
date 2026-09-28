from collections import deque
import heapq

def bfs(graph, start, goal):
    """Breadth-First Search (BFS)"""
    queue = deque([[start]])
    visited = set()
    nodes_expanded = 0

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            cost = sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))
            return {"path": path, "cost": cost, "nodes_expanded": nodes_expanded}

        if node not in visited:
            visited.add(node)
            nodes_expanded += 1
            for neighbor in graph.get(node, {}):
                if neighbor not in visited:
                    queue.append(list(path) + [neighbor])

    return {"path": [], "cost": float("inf"), "nodes_expanded": nodes_expanded}


def dfs(graph, start, goal):
    """Depth-First Search (DFS)"""
    stack = [[start]]
    visited = set()
    nodes_expanded = 0

    while stack:
        path = stack.pop()
        node = path[-1]

        if node == goal:
            cost = sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))
            return {"path": path, "cost": cost, "nodes_expanded": nodes_expanded}

        if node not in visited:
            visited.add(node)
            nodes_expanded += 1
            for neighbor in graph.get(node, {}):
                if neighbor not in visited:
                    stack.append(list(path) + [neighbor])

    return {"path": [], "cost": float("inf"), "nodes_expanded": nodes_expanded}


def ucs(graph, start, goal):
    """Uniform Cost Search (UCS)"""
    pq = [(0, [start])]
    visited = set()
    nodes_expanded = 0

    while pq:
        cost, path = heapq.heappop(pq)
        node = path[-1]

        if node == goal:
            return {"path": path, "cost": cost, "nodes_expanded": nodes_expanded}

        if node not in visited:
            visited.add(node)
            nodes_expanded += 1
            for neighbor, weight in graph.get(node, {}).items():
                if neighbor not in visited:
                    heapq.heappush(pq, (cost + weight, path + [neighbor]))

    return {"path": [], "cost": float("inf"), "nodes_expanded": nodes_expanded}


def ids(graph, start, goal, max_depth=50):
    """Iterative Deepening Search (IDS)"""
    total_nodes_expanded = 0

    def dls(path, depth):
        nonlocal total_nodes_expanded
        node = path[-1]

        if node == goal:
            return path
        if depth <= 0:
            return None

        total_nodes_expanded += 1
        for neighbor in graph.get(node, {}):
            if neighbor not in path:
                res = dls(path + [neighbor], depth - 1)
                if res is not None:
                    return res
        return None

    for depth in range(max_depth):
        result = dls([start], depth)
        if result is not None:
            cost = sum(graph[result[i]][result[i+1]] for i in range(len(result)-1))
            return {"path": result, "cost": cost, "nodes_expanded": total_nodes_expanded}

    return {"path": [], "cost": float("inf"), "nodes_expanded": total_nodes_expanded}