import sys
import itertools
import math
import numpy as np


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


if __name__ == '__main__':
    city = []
    for line in sys.stdin:
        city.append(tuple(map(float, line.split())))

    route = list(range(len(city)))

    all_route = list(itertools.permutations(route))
    s = [score(r) for r in all_route]
    best_route = all_route[np.argmax(s)]

    print(max(s))
    for i in best_route:
        x = city[i][0]
        y = city[i][1]
        print(x, y)
    print(city[best_route[0]][0], city[best_route[0]][1])
