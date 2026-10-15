class Variable:
    def __init__(self, name):
        self.name = name
        self.value = None 

    def bind(self, value):
        self.value = value if isinstance(value, Atom) else Atom(value)
    def __repr__(self):
        if self.value is not None:
            return str(self.value)
        return f"Unknown {self.name}"
class Atom:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return str(self.name)
class Term:
    def __init__(self, functor,*args):
        self.functor = functor
        self.args = args
    def __repr__(self):
        functor_words = " ".join(self.functor.split('_'))
        return f"{self.args[0]} {functor_words} {', '.join(str(a) for a in self.args[1:])}"
class Relation:
    def __init__(self, name):
        self.name = name
    def __call__(self,*args):
        return Term(self.name,*args)
likes = Relation("likes")
is_a  = Relation("is_a")


X = Variable("X")
Jack = Atom("Jack")
Mary = Atom("Mary")
Human = Atom("Human")
Banana = Atom("Banana")
Apple = Atom("Apple")
fact1 = likes(Jack, Banana, Apple)
fact2 = is_a(Mary, Human)
query = likes(Jack, X)
print("Fact 1: ", fact1)
print("Fact 2: ", fact2)
print("Query:  ", query)
X.bind("Banana")
print("Query:  ", query)


