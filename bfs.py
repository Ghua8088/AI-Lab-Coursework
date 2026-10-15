from collections import deque
graph = {
    "A": ["B", "C", "H"],
    "B": ["E", "F", "I"],
    "C": ["G", "J"],
    "D": ["F", "H", "K"],
    "E": ["A", "D"],
    "F": ["I", "K"],
    "G": ["D", "B"],
    "H": ["C", "E"],
    "I": ["J"],
    "J": ["A", "F"],
    "K": [], 
}
path={}
def bfs(graph,start,target):
    queue=deque()
    seen=set()
    queue.append(start)
    visited=set()
    visited.add(start)
    while queue:
        node=queue.popleft()
        seen.add(node)
        if node==target:
            return True
        for neighbor in graph.get(node,[]):
            if neighbor not in visited and neighbor not in seen:
                visited.add(neighbor)
                if neighbor not in path:
                    path[neighbor]=node
                queue.append(neighbor)
    return False
def print_path(path,start,target):
    if target==start:
        print(start)
        return
    print_path(path,start,path[target])
    print(target)
print(bfs(graph,"A","D"))
print_path(path,"A","D")