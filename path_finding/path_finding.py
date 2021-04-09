from math import sqrt


def A_star(G, S, goal):
    def ordered_insert(frontier, path):
        i = 0
        while i < len(frontier):
            if len(frontier[i])+euclidean_distance(frontier[i], goal) < len(path)+euclidean_distance(path, goal):
                i += 1
            else:
                break
        frontier.insert(i, path)
        return frontier

    closed_list = []
    frontier = []
    for start in S:
        path = [start]
        frontier.append(path)

    while len(frontier) != 0:
        path = frontier[0]
        del frontier[0]
        if path[-1] in closed_list:
            continue
        else:
            closed_list.append(path[-1])
        if goal == path[-1]:
            return path
        for neighbour in G.get_neighbours(path[-1]):
            if neighbour not in path:
                new_path = path.copy()
                new_path.append(neighbour)
                frontier = ordered_insert(frontier, new_path)

    return []


def euclidean_distance(p, goal):
    x1, y1 = p[-1]
    x2, y2 = goal
    return sqrt(pow((x1-x2), 2)+pow(y1-y2, 2))
