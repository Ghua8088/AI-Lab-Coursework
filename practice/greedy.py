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
hueristic={
    "a":3,
    "b":2,
    "c":1,
    "d":0,
    "e":0,
    "f":0,
    "g":0
}

def dfs(graph,start,end):
    heap=[(hueristic[start], start)]
    visited=set()
    while heap:
        h,node=heapq.heappop(heap)
        if node==end:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                heapq.heappush(heap, (hueristic[neighbor]+h, neighbor))
    return False
