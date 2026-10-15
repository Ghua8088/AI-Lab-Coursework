import heapq
import math
city_map = {
    "Downtown": (0, 0),
    "North_Junction": (2, 5),
    "East_Plaza": (6, 1),
    "Midtown": (4, 4),
    "South_Bridge": (3, -4),
    "Tech_Park": (8, 6),
    "Harbor": (9, 0),
    "University": (1, 8),
    "Airport": (12, 5),  
}
roads = {
    "Downtown": ["North_Junction", "East_Plaza", "South_Bridge"],
    "North_Junction": ["University", "Midtown"],
    "East_Plaza": ["Midtown", "Harbor"],
    "South_Bridge": ["Harbor"],
    "Midtown": ["Tech_Park", "Harbor"],
    "University": ["Tech_Park"],
    "Tech_Park": ["Airport"],
    "Harbor": ["Airport"],
    "Airport": [],
}
def euclidean_distance(node, goal):
    """Heuristic: Straight-line "as-the-crow-flies" distance to target."""
    x1, y1 = city_map[node]
    x2, y2 = city_map[goal]
    return math.hypot(x2 - x1, y2 - y1)
def greedy_best_first_search(graph, start, goal):
    open_list = [(euclidean_distance(start, goal), start)]
    visited = {start}
    parent = {}
    nodes_expanded = 0
    while open_list:
        h_val, current = heapq.heappop(open_list)
        nodes_expanded += 1
        if current == goal:     
            path = []
            curr = goal
            while curr in parent:
                path.append(curr)
                curr = parent[curr]
            path.append(start)
            return path[::-1], nodes_expanded

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                heapq.heappush(
                    open_list, (euclidean_distance(neighbor, goal), neighbor)
                )
    return None, nodes_expanded
start_node = "Downtown"
destination = "Airport"

route, expanded_count = greedy_best_first_search(roads, start_node, destination)
print(f"Final Path: {' -> '.join(route)}")