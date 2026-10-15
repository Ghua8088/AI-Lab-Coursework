class Variable:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name


class Constant:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name


class Term:
    def __init__(self, functor, *args):
        self.functor = functor
        self.args = list(args)
    def __repr__(self):
        return f"{self.functor}({', '.join(str(a) for a in self.args)})"




def unify_variable(var, x, theta):
    """Maps a Variable object to a substitution term."""
    if var.name in theta:
        return unify(theta[var.name], x, theta)
    elif isinstance(x, Variable) and x.name in theta:
        return unify(var, theta[x.name], theta)
    elif isinstance(x, Variable) and var.name == x.name:
        return theta
    else:
        theta[var.name] = x
        return theta


def unify(x, y, theta=None):
    """Core class-based recursive unification logic."""
    if theta is None:
        theta = {}
    if theta is False:
        return False
    if isinstance(x, Constant) and isinstance(y, Constant) and x.name == y.name:
        return theta
    if isinstance(x, Variable):
        return unify_variable(x, y, theta)
    if isinstance(y, Variable):
        return unify_variable(y, x, theta)
    if isinstance(x, Term) and isinstance(y, Term):
        if x.functor != y.functor or len(x.args) != len(y.args):
            return False
        for arg1, arg2 in zip(x.args, y.args):
            theta = unify(arg1, arg2, theta)
        return theta


    return False


print("--- Class-Based FOL Unification ---")


x = Variable("x")
y = Variable("y")
jack = Constant("Jack")
john = Constant("John")
apple = Constant("Apple")


# Test 1: Unifying Knows(Jack, x) with Knows(Jack, John)
t1 = Term("Knows", jack, x)
t2 = Term("Knows", jack, john)
print(f"Unifying: {t1}  WITH  {t2}")
print(f"Subst:    {unify(t1, t2)}\n")


# Test 2: Unifying Likes(x, y) with Likes(John, Apple)
t3 = Term("Likes", x, y)
t4 = Term("Likes", john, apple)
print(f"Unifying: {t3}  WITH  {t4}")
print(f"Subst:    {unify(t3, t4)}\n")


# Test 3: Structural Mismatch (Should return False)
t5 = Term("Human", x)
t6 = Term("Mortal", john)
print(f"Unifying: {t5}  WITH  {t6}")
print(f"Subst:    {unify(t5, t6)}")

