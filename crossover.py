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
