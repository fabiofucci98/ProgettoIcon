from path_finding import Graph, A_star, euclidean_distance
from engine import Engine, parse


class QueryException(Exception):
    pass


class Agent:
    def __init__(self, wall_lists, kb_filename, sprite, floor):
        self.graphs = [Graph(wall_list) for wall_list in wall_lists]
        self.engine = Engine()
        self.engine.load_kb(kb_filename)
        self.floor = floor
        self.sprite = sprite
        self.path = None
        self.floor_to_go = None

    def act(self, text):
        query = parse(text)
        if len(query) == 1:
            if query[0].pred == 'muovi':
                try:
                    self.path = self.move(query[0].args[0].const)
                except QueryException:
                    return 'culo', 'Non ho capito'
                if self.path == None:
                    return 'culo', 'Non posso arrivarci'
        return 'culo', 'OK'

    def move(self, query):
        def get_pos(obj):
            tmp_query = parse(
                'posizione('+obj+',X,Y,Floor).')
            out = clean(self.engine.prove(tmp_query))
            if out == False or query == 'scale' or query == 'ascensore':
                raise QueryException
            x, y, floor = int(out[0][0].const), int(
                out[0][1].const), out[0][2].const
            if floor == 'all':
                floor = self.floor
            else:
                floor = int(out[0][2].const)
            return x, y, floor

        def get_island(stairs_pos, elevator_pos, goal_pos):
            eu_stairs = euclidean_distance(self.sprite.position, stairs_pos)
            eu_elevator = euclidean_distance(
                self.sprite.position, elevator_pos)
            eu_stairs += euclidean_distance(stairs_pos, goal_pos)
            eu_elevator += euclidean_distance(elevator_pos, goal_pos)
            return stairs_pos if eu_stairs < eu_elevator else elevator_pos

        x, y, floor = get_pos(query)
        if floor == self.floor:
            return A_star(
                self.graphs[floor-1], [self.sprite.position], (x, y))
        else:
            self.floor_to_go = floor
            stairs_pos = get_pos('scale')
            elevator_pos = get_pos('ascensore')
            stairs_pos = (stairs_pos[0], stairs_pos[1])
            elevator_pos = (elevator_pos[0], elevator_pos[1])
            island_pos = get_island(stairs_pos, elevator_pos, (x, y))
            island_to_goal = A_star(self.graphs[floor-1], [island_pos], (x, y))
            if island_to_goal == []:
                return None
            robot_to_island = A_star(
                self.graphs[self.floor-1], [self.sprite.position], island_pos)
            if robot_to_island == []:
                return None

            return robot_to_island + island_to_goal[1:]


def clean(SLD_derivations):
    if not isinstance(SLD_derivations, list):
        return True

    tmp_answers = [der[-1].head.args for der in SLD_derivations]
    answers = []
    for answer in tmp_answers:
        if answer not in answers:
            answers.append(answer)

    if len(answers) == 0:
        return False

    elif len(answers) == 1 and len(answers[0]) == 0:
        return True

    return answers
