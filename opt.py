import time
from math import sqrt, inf
from random import randint


def dist(p1, p2):
    return sqrt(pow(p1[0]-p2[0], 2)+pow(p1[1]-p2[1], 2))


def get_cost(path):
    cost = 0
    for i in range(len(path)-1):
        cost += dist(path[i], path[i+1])
    return cost


def branch_and_bound(positions):
    def expand(path, positions):
        neighbours = []
        for pos in positions:
            if pos not in path:
                tmp_path = path.copy()
                tmp_path.append(pos)
                neighbours.append(tmp_path)
        return neighbours

    stack = [[p] for p in positions]
    best = None
    best_cost = inf
    while len(stack) != 0:
        path = stack[-1]
        del stack[-1]
        path_cost = get_cost(path)

        if path_cost < best_cost:
            if len(path) == len(positions):
                best = path
                best_cost = path_cost
            else:
                neighbours = expand(path, positions)
                for neighbour in neighbours:
                    stack.append(neighbour)

    return best


for n in range(5, 21):
    positions = []
    print(n)
    for i in range(n):
        positions.append((randint(-100, 100), randint(-100, 100)))

    start = time.time()
    branch_and_bound(positions)
    end = time.time()
    print(end - start)
