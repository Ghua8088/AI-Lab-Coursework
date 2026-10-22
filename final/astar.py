import heapq

graph = {
    'S': [('A', 3), ('B', 2)],
    'A': [('C', 4), ('D', 1)],
    'B': [('E', 3), ('F', 1)],
    'C': [],
    'D': [],
    'E': [('H', 5)],
    'F': [('I', 2), ('G', 3)],
    'G': [],
    'H': [],
    'I': []
}
heuristics = {
    'S': 13,
    'A': 12,
    'B': 4,
    'C': 7,
    'D': 3,
    'E': 8,
    'F': 2,
    'G': 0,
    'H': 4,
    'I': 9
}

def astar(graph,heuristics,start,target):
    heap=[(heuristics[start],0,start)]
    seen=set()
    path={}
    while heap:
        h_c,g_c,curr=heapq.heappop(heap)
        if curr==target:
            return path
        for neighbor,edge_cost in graph[curr]:
            if neighbor not in seen:
                g_n=g_c+edge_cost
                heapq.heappush(heap,(g_n+heuristics[neighbor],heuristics[neighbor],neighbor))
                seen.add(neighbor)
                path[neighbor]=curr
    return None
def decode_path(path,start,goal):
    op=[]
    while start!=goal:
        op.append(goal)
        goal=path[goal]
    op.append(goal)
    return op[::-1]
path=astar(graph,heuristics,'S','G')
if path:
    print(f"path from source to goal {' -> '.join(decode_path(path,'S','G'))}")

            