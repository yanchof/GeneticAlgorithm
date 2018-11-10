import random


def binary_mutation(population, probability):
    for i, individual in enumerate(population):
        for j, gene in enumerate(individual):
            if random.random() < probability:
                if gene == 0:
                    individual[j] = 1
                else:
                    individual[j] = 0
