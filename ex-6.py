import random
import heapq
def get_fitness(cand):
    major_diags = {}
    minor_diags = {}
    for col, row in enumerate(cand):
        major_diags[row - col] = major_diags.get(row - col, 0) + 1
        minor_diags[row + col] = minor_diags.get(row + col, 0) + 1 
    conflicts = 0  
    for count in major_diags.values():
        if count > 1:
            conflicts += (count * (count - 1)) // 2        
    for count in minor_diags.values():
        if count > 1:
            conflicts += (count * (count - 1)) // 2      
    return conflicts
def init_candidates(no_candidates,n):
    cands = []
    while len(cands) < no_candidates:
        cand = list(range(n))
        random.shuffle(cand)
        invalid = False
        for i in range(n - 1):
            if abs(cand[i] - cand[i+1]) == 1:
                invalid = True
                break
                
        if not invalid:
            cands.append(cand)
    return cands
def score_sort(cands):
    heap = []
    for cand in cands:
        heapq.heappush(heap, (get_fitness(cand), cand))
    return heap
def cross(a,b):
    n = len(a)
    child = [None] * n
    start, end = sorted(random.sample(range(n), 2))
    child[start:end+1] = a[start:end+1]
    filled_set = set(child[start:end+1])
    child_ptr = (end + 1) % n
    for i in range(n):
        parent_b_idx = (end + 1 + i) % n
        candidate_val = b[parent_b_idx]
        
        if candidate_val not in filled_set:
            child[child_ptr] = candidate_val
            filled_set.add(candidate_val)
            child_ptr = (child_ptr + 1) % n
    return child
def mutate(child, n, mutation_rate=0.15):
    if random.random() < mutation_rate:

        idx1, idx2 = random.sample(range(n), 2)
        child[idx1], child[idx2] = child[idx2], child[idx1]
    return child
def genetic_(no_candidates, n_gens, gen_cap, n=8):
    perfect_score = 0   
    gen = init_candidates(no_candidates, n)
    for iteration in range(n_gens):
        scored = score_sort(gen)
        best = heapq.nsmallest(gen_cap, scored)
        if best[0][0] == perfect_score:
            return best[0]
        gen = []
        for _ in range(no_candidates):
            first = random.choice(best)[1]
            second = random.choice(best)[1]
            child=cross(first, second)
            child=mutate(child,n)
            gen.append(child)
    return heapq.nsmallest(1, score_sort(gen))[0]
print("Best solution found (Score, Chromosome):", genetic_(no_candidates=100, n_gens=50000, gen_cap=40, n=20))