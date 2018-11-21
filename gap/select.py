import random
import numpy as np


def roulette_wheel_selection(population, evaluation, selection_num):
    selected = random.choices(population=population, weights=evaluation, k=selection_num)
    return selected


def rank_selection(population, evaluation, selection_num):
    population_num = len(population)
    rank = np.argsort(evaluation)
    rank_probability = 2 * (population_num - rank + 1) / (population_num * (population_num + 1))
    selected = random.choices(population=population, weights=rank_probability, k=selection_num)
    return selected


def elite_selection(population, evaluation, selection_num):
    conbined = list(zip(population, evaluation))
    list.sort(conbined, key=lambda x: x[1])
    elite = [item[0] for item in conbined][:selection_num]
    return elite
