import random
import numpy as np


def roulette_wheel_selection(population, evaluation, option):
    selected = random.choices(population=population, weights=evaluation, k=option['selection_num'])
    return selected


def rank_selection(population, evaluation, option):
    population_num = len(population)
    rank = np.argsort(evaluation)
    rank_probability = 2 * (population_num - rank + 1) / (population_num * (population_num + 1))
    selected = random.choices(population=population, weights=rank_probability, k=option['selection_num'])
    return selected


def tournament_selection(population, evaluation, option):
    selected = []
    for selection in range(option['selection_num']):
        population_and_evaluation = list(zip(population, evaluation))
        tournament_population_and_evaluation = \
            random.choices(population=population_and_evaluation, k=option['tournament_size'])
        top_individual = max(tournament_population_and_evaluation, key=lambda x: x[0])[0]
        selected.append(top_individual)
    return selected


def elite_selection(population, evaluation, option):
    population_and_evaluation = list(zip(population, evaluation))
    list.sort(population_and_evaluation, key=lambda x: x[1])
    elite = [item[0] for item in population_and_evaluation][:option['selection_num']]
    return elite
