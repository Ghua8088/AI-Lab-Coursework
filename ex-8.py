# Map Coloring CSP using backtracking
COLORS=[0,1]
def satisfies_constraint(node,assignments,graph):
    for neighbor in graph[node]:
        if neighbor in assignments and assignments[neighbor] == assignments[node]:
            return False
    return True

def backtracking_search(graph,domains,assignments):
    if len(assignments) == len(graph):
        return assignments
    for node in graph:
        if node not in assignments:
            current=node
            break
    for color in COLORS:
        assignments[current]=color
        if satisfies_constraint(current,assignments,graph):
            result=backtracking_search(graph,domains,assignments)
            if result is not None:
                return result
        del assignments[current]
    return None

graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW']
}

domains = {node: COLORS[:] for node in graph}
assignments = {}
result = backtracking_search(graph, domains, assignments)
if result:
    print("Solution found:", result)
else:
    print("No solution found")
    

