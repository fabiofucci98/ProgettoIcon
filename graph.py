#Commento per issue di test

class Graph:
    def __init__(self, barrier_list):
        self.mat = []
        barr_pos = [(barr.center_x, barr.center_y) for barr in barrier_list]
        for x in range(8, 800, 16):
            row = []
            for y in range(8, 800, 16):
                node = 1 if (x, y) in barr_pos else 0
                row.append(node)
            self.mat.append(row)

    def get_neighbours(self, pos):
        offsets = (-1, -1), (-1, 0), (-1, 1), (0,
                                               -1),  (0, 1), (1, -1), (1, 0), (1, 1)
        neighbours = []
        for offset in offsets:
            x = int(pos[0]/16)+offset[0]
            y = int(pos[1]/16)+offset[1]
            try:
                if self.mat[x][y] == 0:
                    neighbours.append((x*16, y*16))
            except IndexError:
                pass
        return neighbours
