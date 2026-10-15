COLORS=[0,1,2]
graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW']
}
assignments={}
def satisfies_constraint(node,color,assignments):
    for neighbor in graph[node]:
        if assignments.get(neighbor,"")==color:
            return False
    return True

def backtrack(assignments):
    if len(assignments)==len(graph):
        return assignments
    for node in graph:
        if node not in assignments:
            current=node
            break
    for i in COLORS:
        assignments[current]=i
        if satisfies_constraint(current,i,assignments):
            result=backtrack(assignments)
            if result is not None:
                return result
        del assignments[current]
    return None
result=backtrack(assignments)
print(result)


    
    