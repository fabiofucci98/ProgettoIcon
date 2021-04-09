import arcade

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
