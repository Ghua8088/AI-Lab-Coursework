# CryptArithemetic
def word_map(words,assignment):
    op=[]
    for word in words:
        s=0
        for l in word:
            s=s*10+assignment[l]
            
        op.append(s)
    return op
def satisfies_constraint(var,assignment,variables,leading_letters,words):
    val=assignment[var]
    if var in leading_letters and val==0:
        return False
    for other_var,other_val in assignment.items():
        if other_var !=var and other_val == val:
            return False
    if len(assignment)==len(variables):
        op=word_map(words,assignment)
        if sum(op[:-1])!=op[-1]:
            return False
    return True
def backtrack(assignment,variables,leading_letters,words):
    if len(assignment)==len(variables):
        return assignment
    for v in variables:
        if v not in assignment:
            current=v
            break
    for n in range(0,10):
        assignment[current]=n
        if satisfies_constraint(current,assignment,variables,leading_letters,words):
            result=backtrack(assignment,variables,leading_letters,words)
            if result is not None:
                return result
        del assignment[current]
    return None
words = ['SEND', 'MORE', 'MONEY']
variables = list(dict.fromkeys(''.join(words)))
leading_letters=[word[0] for word in words]
print(variables)
assignment = {}
result=backtrack(assignment,variables,leading_letters,words)
print("Assignments:", result)
if result:
    out=[]
    for word in words:
        s=0
        for l in word:
            s=s*10+assignment[l]  
        out.append(s)
    print(f"{out[0]} + {out[1]} = {out[2]}")
        
            
            
            
            
    
    
        
    