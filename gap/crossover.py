import random


def uniform_crossover(parent1, parent2):
    child1 = []
    child2 = []

    mask = [random.randint(0, 1) for i in range(len(parent1))]
    for i, m in enumerate(mask):
        if m == 0:
            child1.append(parent1)
            child2.append(parent2)
        else:
            child1.append(parent2)
            child2.append(parent1)

    return [child1, child2]


def partially_mapped_crossover_2(parent1, parent2):
    gene_size = len(parent1)

    child1 = [None] * gene_size
    child2 = [None] * gene_size

    p1 = random.randint(0, gene_size - 3)
    p2 = random.randint(p1, gene_size - 2)

    child1[p1:p2] = parent2[p1:p2]
    child2[p1:p2] = parent1[p1:p2]

    change_rule = {}
    for i in range(p1, p2, 1):
        change_rule[child1[i]] = child2[i]
        change_rule[child2[i]] = child1[i]

    for i in range(gene_size):
        if child1[i] is None:
            if not parent1[i] in change_rule.keys():
                child1[i] = parent1[i]
        if child2[i] is None:
            if not parent2[i] in change_rule.keys():
                child2[i] = parent2[i]

    for i in range(gene_size):
        if child1[i] is None:
            child1[i] = change_rule[parent1[i]]
        if child2[i] is None:
            child2[i] = change_rule[parent2[i]]

    return [child1, child2]
