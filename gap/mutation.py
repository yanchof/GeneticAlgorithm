import random


def binary_mutation(population, probability):
    for i, individual in enumerate(population):
        for j, gene in enumerate(individual):
            if random.random() < probability:
                if gene == 0:
                    individual[j] = 1
                else:
                    individual[j] = 0


def exchange_mutation(population, probability):
    for i, individual in enumerate(population):
        for j, gene in enumerate(individual):
            if random.random() < probability:
                target_i = random.choice([n for n in range(len(individual)) if n != j])
                tmp = population[i][j]
                population[i][j] = population[i][target_i]
                population[i][target_i] = tmp
