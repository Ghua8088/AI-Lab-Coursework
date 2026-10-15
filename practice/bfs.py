graph={
    "a":["b","c"],
    "b":["d","e"],
    "c":["f","g"],
    "d":[],
    "e":[],
    "f":[],
    "g":[]
}
def bfs(graph,start,end):
    queue=[start]
    visited=set()
    while queue:
        node=queue.pop(0)
        if node==end:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False
print(bfs(graph,"a","g"))
