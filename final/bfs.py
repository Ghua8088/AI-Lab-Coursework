from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}
def bfs(graph,start,goal):
    path={}
    seen=set([start])
    if start not in graph:
        return path
    q=deque([start])
    while q:
        curr=q.popleft()
        if curr==goal:
            return path
        for neighbor in graph.get(curr,[]):
            if neighbor not in seen:
                path[neighbor]=curr
                seen.add(neighbor)
                q.append(neighbor)
def decode_path(path,start,goal):
    op=[]
    while start!=goal:
        op.append(goal)
        goal=path[goal]
    op.append(goal)
    return op[::-1]
START='A'
GOAL='G'
path=bfs(graph,START,GOAL)
print(f"path from source to goal {' -> '.join(decode_path(path,START,GOAL))}")

        
        