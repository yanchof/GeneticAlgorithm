import random


def roulette_wheel_selection(population, evaluation, selection_num):
    selected = random.choices(population=population, weights=evaluation, k=selection_num)
    return selected

def rank_selection():
    return

def elite_selection():
    return