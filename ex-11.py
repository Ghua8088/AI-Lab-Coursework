class Atom:
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return str(self.name)
class Var:
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return str(self.name)
class Term:
    def __init__(self,func,args):
        self.func=func
        self.args=args
    def __repr__(self):
        args_str = ", ".join(str(arg) for arg in self.args)
        return f"{self.func}({args_str})"
class Relation:
    def __init__(self,name):
        self.name=name
    def __call__(self,*args):
        return Term(self.name,args)
def And(*args):
    return " ∧ ".join(args)
def Or(*args):
    return " ∨ ".join(args)
def Implies(left,right):
    return f"{left} ⇒ {right}"
def Not(term):
    return f"¬{term}"
def ForAll(variable,term):
    return f"∀{variable} {term}"
def Exist(variable,term):
    return f"∃{variable} {term}"
Jack=Atom("Jack")
Mary=Atom("Mary")
hates=Relation("Hates")
Jerry=Atom("Jerry")
Tom=Atom("Tom")
likes=Relation("likes")
X=Var("X")
print(Not(likes(Jack,Mary)))
print(Implies(Not(hates(Tom,Jerry)),likes(Tom,Jerry)))