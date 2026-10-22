
def is_var(x):
    return isinstance(x,str) and x.islower()
def unify_var(var,x,theta):
    if var in theta:
        return unify(theta[var],x,theta)
    if is_var(x) and x in theta:
        return unify(var,theta[x],theta)
    theta[var]=x
    return theta
def unify(x,y,theta=None):
    if theta is None: theta={}
    if theta is False: return theta
    if x==y:return theta
    elif is_var(x): return unify_var(x, y, theta)
    elif is_var(y): return unify_var(y, x, theta)
    elif isinstance(x,tuple) and isinstance(y,tuple):
        if len(x)!=len(y):
            return False
        for a,b in zip(x,y):
            theta=unify(a,b,theta)
        return theta
    return False
print(unify(('Prime', 13), ('Prime', 'y')))
print(unify(('Knows', 'John', 'x'), ('Knows', 'y', ('Mother', 'John'))))
print(unify(('Human', 'x'), ('Mortal', 'John')))