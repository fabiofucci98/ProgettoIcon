from math import sqrt


class Path:
    def __init__(self):
        self.p = []
        self.c = None

    def add_edge(self, edge):
        self.p.append(edge.n2)
        self.c += edge.cost


def A_star(G, S, goal, h):
    def ordered_insert(frontier, path):
        i = 0
        while i < len(frontier):
            if frontier[i].c + h(frontier[i].p, G) < path.c + h(path.p, G):
                i += 1
            else:
                break
        frontier.insert(i, path)
        return frontier

    closed_list = []
    frontier = []
    for start in S:
        path = Path()
        path.p = [start]
        path.c = 0
        frontier.append(path)

    while len(frontier) != 0:
        path = frontier[0]
        del frontier[0]
        if path.p[-1] in closed_list:
            continue
        else:
            closed_list.append(path.p[-1])
        if goal(path.p[-1]):
            return path.p
        for edge in G.edges:
            if edge.n1 == path.p[-1] and not edge.n2 in path.p:
                new_path = Path()
                new_path.p = path.p.copy()
                new_path.c = path.c
                new_path.add_edge(edge)
                frontier = ordered_insert(frontier, new_path)

    return []


def euclidean_distance(p, G):
    x1, y1 = p[-1].value
    x1, y1 = int(x1), int(y1)
    x2, y2 = G.end_node.value
    x2, y2 = int(y1), int(y2)

    return sqrt(pow((x1-x2), 2)+pow(y1-y2, 2))
