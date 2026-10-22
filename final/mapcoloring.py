colors=[0,1,2]
graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW']
}
def satisfies_constraint(node,graph,assignment):
    c=assignment[node]
    for neigh in graph[node]:
        if assignment.get(neigh,"")==c:
            return False
    return True

def backtrack(graph,assignment):
    if len(assignment)==len(graph):
        return assignment
    curr=next(i for i in graph if i not in assignment)
    for c in colors:
        assignment[curr]=c
        if satisfies_constraint(curr,graph,assignment):
            result=backtrack(graph,assignment)
            if result:
                return result
        del assignment[curr]
    return None
result=backtrack(graph,{})
print(result)

        
