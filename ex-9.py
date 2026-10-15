def satisfies_constraint(var, assignments, variables, words):
    val = assignments[var]
    if var in leading_letters and val == 0:
        return False
    for other_var, other_val in assignments.items():
        if other_var != var and other_val == val:
            return False
    if len(assignments) == len(variables):
        base = 10
        out = []
        for word in words:
            v = 0
            for i, char in enumerate(reversed(word)):
                v += assignments[char] * pow(base, i)
            out.append(v)

        if sum(out[:-1]) != out[-1]:
            return False

    return True


def backtrack(variables, words, assignments):
    if len(assignments) == len(variables):
        return assignments

    var = variables[len(assignments)]
    for value in range(10):
        assignments[var] = value
        if satisfies_constraint(var, assignments, variables, words):
            result = backtrack(variables, words, assignments)
            if result is not None:
                return result
        del assignments[var]

    return None


words = ['SEND', 'MORE', 'MONEY']
variables = list(dict.fromkeys(''.join(words)))
leading_letters = {letters[0] for letters in words}
assignments = {}
result = backtrack(variables, words, assignments)
print("Assignments:", result)
if result:
    out = []
    for word in words:
        v = 0
        for i, char in enumerate(reversed(word)):
            v += result[char] * pow(10, i)
        out.append(v)
    print(f"{out[0]} + {out[1]} = {out[2]}")