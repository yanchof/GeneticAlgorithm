from gap.core import GeneticAlgorithm
from gap.select import roulette_wheel_selection, elite_selection
from gap.crossover import uniform_crossover
from gap.mutation import binary_mutation


def score(individual):
    correct_binary = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    correct_count = 0
    for individual_bit, correct_bit in zip(individual, correct_binary):
        if individual_bit == correct_bit:
            correct_count += 1

    return correct_count


if __name__ == "__main__":
    ga = GeneticAlgorithm(1, 5, 40, 0.85, 0.1, 40)

    ga.add_selection_method(roulette_wheel_selection, 100)
    ga.add_selection_method(elite_selection, 20)
    ga.set_crossover_method(uniform_crossover)
    ga.set_mutation_method(binary_mutation)
    ga.set_evaluation_method(score)
    ga.generate_population()

    generation_count = 0
    while len(ga.evaluation) == 0 or max(ga.evaluation) < 10:
        generation_count += 1
        ga.proceed()

    print("Generation:", generation_count)
