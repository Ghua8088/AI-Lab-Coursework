import heapq
from collections import deque
import heapq
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
heuristic = {
    "A": 3,  # A -> B -> E -> D (3 hops)
    "B": 2,  # B -> E -> D (2 hops)
    "C": 2,  # C -> G -> D (2 hops)
    "D": 0,  # Target node
    "E": 1,  # E -> D (1 hop)
    "F": 6,  # F -> I -> J -> A -> H -> E -> D (6 hops)
    "G": 1,  # G -> D (1 hop)
    "H": 2,  # H -> E -> D (2 hops)
    "I": 5,  # I -> J -> A -> H -> E -> D (5 hops)
    "J": 4,  # J -> A -> H -> E -> D (4 hops)
    "K": float("inf"),  # Dead end, cannot reach D
}
path={}
def astar(graph,start,target):
    queue=[]
    seen=set()
    heapq.heappush(queue,(heuristic[start],0,start))
    visited=set()
    visited.add(start)
    while queue:
        h_cost,g_cost,node=heapq.heappop(queue)
        seen.add(node)
        g_score={start:0}
        if node==target:
            return True
        for neighbor in graph.get(node,[]):
            tentative_g=g_cost+1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic.get(neighbor, float("inf"))
                path[neighbor] = node
                heapq.heappush(queue, (f_score, tentative_g, neighbor))
    return False
def print_path(path,start,target):
    if target==start:
        print(start)
        return
    print_path(path,start,path[target])
    print(target)
print(astar(graph,"A","D"))
print_path(path,"A","D")