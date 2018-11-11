import random


def roulette_wheel_selection(population, evaluation, selection_num):
    selected = random.choices(population=population, weights=evaluation, k=selection_num)
    return selected


def rank_selection(population, evaluation, selection_num):
    return


def elite_selection(population, evaluation, selection_num):
    conbined = list(zip(population, evaluation))
    list.sort(conbined, key=lambda x: x[1])
    elite = [item[0] for item in conbined][:selection_num]
    return elite
