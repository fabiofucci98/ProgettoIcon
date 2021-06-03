import arcade
from math import sqrt

GRID_CHUNK_SIZE = 16


class Graph:
    def __init__(self, barrier_list: arcade.sprite_list):
        screen_height, screen_width = 800, 800
        self.mat = []
        barr_pos = []
        for barr in barrier_list:
            barr_pos.extend(get_chunks_positions(barr))
        for x in range(0, screen_width, GRID_CHUNK_SIZE):
            row = []
            for y in range(0, screen_height, GRID_CHUNK_SIZE):
                node = 1 if (x, y) in barr_pos else 0
                row.append(node)
            self.mat.append(row)

    def get_neighbours(self, pos):
        offsets = (-1, -1), (-1, 0), (-1, 1), (0,
                                               -1),  (0, 1), (1, -1), (1, 0), (1, 1)
        neighbours = []
        for offset in offsets:
            x = int(pos[0]/GRID_CHUNK_SIZE)+offset[0]
            y = int(pos[1]/GRID_CHUNK_SIZE)+offset[1]
            try:
                if self.mat[x][y] == 0:
                    neighbours.append((x*GRID_CHUNK_SIZE, y*GRID_CHUNK_SIZE))
            except IndexError:
                pass
        return neighbours

    def save_matrix(self):
        f = open('matrix', 'w')
        for row in self.mat:
            for val in row:
                if val == 0:
                    f.write(' ')
                else:
                    f.write('@')
            f.write('\n')


def get_chunks_positions(barrier: arcade.Sprite):
    HALF_SPRITE_SIZE = 8
    l = []
    top, bottom, left, right = int(barrier.top), int(
        barrier.bottom), int(barrier.left), int(barrier.right)
    for y in range(left, right, HALF_SPRITE_SIZE):
        for x in range(bottom, top, HALF_SPRITE_SIZE):
            l.append((y, x))
    return l


def A_star(G, S, goal):
    def get_dist(el1, el2):
        if el1[0] == el2[0] or el1[1] == el2[1]:
            return 1
        return 1.4

    def get_cost(path):
        el1 = path[0]
        dist = 0
        for el2 in path:
            dist += get_dist(el1, el2)
            el1 = el2
        return dist

    def ordered_insert(frontier, path):
        i = 0
        while i < len(frontier):
            if get_cost(frontier[i])+euclidean_distance(frontier[i][-1], goal) < get_cost(path)+euclidean_distance(path[-1], goal):
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


def euclidean_distance(last, goal):
    x1, y1 = last
    x2, y2 = goal
    return sqrt(pow(x1-x2, 2)+pow(y1-y2, 2))/GRID_CHUNK_SIZE
