
def satsifies_constraint(assignment,words,domain):
    #LEAD
    leading=[word[0] for word in words]
    for l in leading:
        if assignment.get(l,-1)==0:
            return False

    #ALLDIFF
    if len(set(assignment.values()))!=len(assignment):
        return False

    #MATH
    if len(assignment)==len(domain):
        op=[]
        for word in words:
            s=0
            for l in word:
                s=s*10+assignment[l]
            op.append(s)
        if sum(op[:-1])==op[-1]:
            return True
        return False
    return True
def backtrack(words,assignment,domain):
    if len(assignment)==len(domain):
        return assignment
    c=next(l for l in domain if l not in assignment)
    for i in range(10):
        assignment[c]=i
        if satsifies_constraint(assignment,words,domain):
            result=backtrack(words,assignment,domain)
            if result:
                return result
        del assignment[c]
    return None
words=["send","more","money"]
domain=set([l for word in words for l in word])
result=backtrack(words,{},domain)

print(result) 
op=[]
for word in words:
    s=0
    for l in word:
        s=s*10+result[l]
    op.append(s)
print(" + ".join([str(x) for x in op[:-1]]),"=",op[-1])