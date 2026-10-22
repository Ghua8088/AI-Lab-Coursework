import random
COL=8
MAX_SCORE=24

def create_induvidual():
    return random.sample(range(8), 8)
def reproduce(i1,i2):
    c=random.randint(1,COL-1)
    c1=i1[:c]+i2[c:]
    c2=i2[:c]+i1[c:]
    return [c1,c2]
def check_fitness(induvidual):
    row=len(set(induvidual))
    diag1=len(set([induvidual[c]-c for c in range(COL)]))
    diag2=len(set([induvidual[c]+c for c in range(COL)]))
    return row+diag1+diag2
def select(generation,fitness):
    total=sum(fitness)
    prob=[fitness[i]/total for i in range(len(fitness))]
    return random.choices(generation,prob,k=1)[0]
def mutate(induvidual):
    s1,s2=random.choices(list(range(0,8)),k=2)
    induvidual[s1],induvidual[s2]=induvidual[s2],induvidual[s1]
    return induvidual
def genetic_algorithm(max_population=10,max_generations=1000,mut_probablity=0.4):
    generation=[create_induvidual() for _ in range(max_population)]
    for i in range(max_generations):
        fitness=[check_fitness(i) for i in generation]
        for i,score in enumerate(fitness):
            if score==MAX_SCORE:
                return generation[i],score,i
        new_gen=[]
        for _ in range(len(generation)//2):
            x=select(generation,fitness)
            y=select(generation,fitness)
            c1,c2=reproduce(x,y)
            if random.random()<mut_probablity:
                c1=mutate(c1)
            if random.random()<mut_probablity:
                c2=mutate(c2)
            new_gen.extend([c1,c2])
        generation=new_gen
    fitnesses = [check_fitness(ind) for ind in generation]
    best_idx = fitnesses.index(max(fitnesses))
    return generation[best_idx], fitnesses[best_idx],max_generations
print(f"Best state:{genetic_algorithm(max_population=100,max_generations=10000)}")