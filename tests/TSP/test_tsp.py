from gap.core import GeneticAlgorithm
from gap.select import roulette_wheel_selection, elite_selection
from gap.crossover import partially_mapped_crossover_2
from gap.mutation import exchange_mutation

import sys
import random
import math
import numpy as np
import matplotlib.pyplot as plt


def distance(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    d = math.sqrt(dx**2 + dy**2)
    return d


def calc_route_cost(travel_hist):
    d = 0
    for i in range(len(travel_hist) - 1):
        d += distance(travel_hist[i], travel_hist[i+1])
    d += distance(travel_hist[-1], travel_hist[0])
    return d


def score(individual):
    combined = list(zip(city, individual))
    route = [item[0] for item in sorted(combined, key=lambda x: x[1])]
    cost = calc_route_cost(route)

    return 1./cost


if __name__ == "__main__":
    city = []
    for line in sys.stdin:
        city.append(list(map(float, line.split())))
    city_num = len(city)

    ga = GeneticAlgorithm(1, city_num, 60, 0.85, 0.05, 60)
    ga.add_selection_method(roulette_wheel_selection, 40)
    ga.add_selection_method(elite_selection, 20)
    ga.set_crossover_method(partially_mapped_crossover_2)
    ga.set_mutation_method(exchange_mutation)
    ga.set_evaluation_method(score)

    ga.generate_population()
    for i in range(60):
        ga.population[i] = random.sample(list(range(city_num)), city_num)

    generation_count = 0
    while len(ga.evaluation) == 0 or max(ga.evaluation) > 0.001:
        generation_count += 1
        ga.proceed()

    best_route = np.array(ga.population)[np.argmax(ga.evaluation)]

    x_hist = [city[i][0] for i in best_route]
    x_hist.append(city[best_route[0]][0])
    y_hist = [city[i][1] for i in best_route]
    y_hist.append(city[best_route[0]][1])

    for x, y in zip(x_hist, y_hist):
        print(x, y)

