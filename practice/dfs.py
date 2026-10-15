import heapq
graph={
    "a":["b","c"],
    "b":["d","e"],
    "c":["f","g"],
    "d":[],
    "e":[],
    "f":[],
    "g":[]
}
def dfs(graph,start,end):
    stack=[start]
    visited=set()
    while stack:
        node=stack.pop(0)
        if node==end:
            return True
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])
    return False
