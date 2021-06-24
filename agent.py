from copy import deepcopy
from path_finding import Graph, A_star, euclidean_distance
from engine import Clause, Constant, Engine, ParseException, parse
from math import inf

ELEVATOR_POS = 320, 48
STAIRS_POS = 720, 496


class Agent:
    def __init__(self, wall_lists, kb_filename, sprite, floor):
        self.graphs = [Graph(wall_list) for wall_list in wall_lists]
        self.engine = Engine()
        self.engine.load_kb(kb_filename)
        self.floor = floor
        self.sprite = sprite
        self.path = None
        self.floor_to_go = None
        self.options = {'abduce': False, 'one': False,
                        'occurs': False, 'solve': False, 'solving': None}
        self.route = None
        self.timer = 0
        self.solve_timer = 0
        self.message = []
        self.pos_ind_dict = None

    def act(self, text: str):
        if text == 'abduce':
            self.options['abduce'] = not self.options['abduce']
            self.message.extend(['abduce = '+str(self.options['abduce'])])

        elif text == 'prove one':
            self.options['one'] = not self.options['one']
            self.message.extend(['prove one = '+str(self.options['abduce'])])
        elif text == 'occurs check':
            self.options['occurs'] = not self.options['occurs']
            self.message.extend(
                ['occurs check = '+str(self.options['abduce'])])
        elif text == 'solve_conflicts':
            self.solve_conflicts()
        elif text.split()[0] == 'how' and len(text.split()) == 2:
            rules = self.engine.how(
                parse(text.split()[1]+'.')[0], self.options['occurs'])
            messages = [str(clause)
                        for clause in rules] if len(rules) > 0 else ['None']
            self.message.extend(
                messages)
        else:
            try:
                query = parse(text)
            except ParseException:
                self.message.extend(['Sintassi errata'])
                return
            if len(query) == 1 and query[0].pred == 'muovi' and len(query[0].args) == 1:
                pos = self.get_pos(query[0].args[0])
                if not pos:
                    self.message.extend(['Non ho capito'])
                    return
                path = self.get_path(pos)
                if path:
                    self.message.extend(['Ok'])
                    self.path = path
                else:
                    self.message.extend(['Non posso arrivarci'])

            else:
                ans = clean(self.engine.prove(query, self.options['one'],
                                              self.options['abduce'], self.options['occurs']), self.options['abduce'])
                self.message.extend([str(elem) for elem in ans])

    def solve_conflicts(self):
        def get_ind(conflict):
            inds = []
            for atom in conflict:
                inds.extend(atom.args)
            return inds

        def min_conflict(conflicts):
            min = conflicts[0]
            for conflict in conflicts[1:]:
                if len(conflict) < len(min):
                    min = conflict
            return min

        def branch_and_bound(positions):
            def dist(p1, p2):
                p1, f1 = p1[:2], p1[2]
                p2, f2 = p2[:2], p2[2]
                if f1 == f2:
                    return euclidean_distance(p1, p2)
                else:
                    island_pos = get_island(p1, p2)
                    return euclidean_distance(p1, island_pos)+euclidean_distance(island_pos, p2)

            def get_cost(path):
                cost = 0
                for i in range(len(path)-1):
                    cost += dist(path[i], path[i+1])
                return cost

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

        ans = clean(self.engine.prove(
            parse('false.'), abduce=True), abduce=True)
        if len(ans) == 1 and ans[0] == 'False':
            self.message.extend(['Non ci sono conflitti da risolvere'])
            return
        conflict = min_conflict(ans)

        self.message.extend(
            ['Ho trovato i seguenti conflitti']+[str(elem) for elem in ans]+[''])
        self.message.extend(['Risolverò']+[str(conflict)]+[''])
        inds = get_ind(conflict)
        inds_pos = [self.get_pos(ind) for ind in inds]
        self.pos_ind_dict = dict(zip(inds_pos, inds))
        self.route = branch_and_bound(inds_pos)
        self.conflict = []
        for pos in self.route:
            for c in conflict:
                if self.pos_ind_dict[pos] in c.args:
                    self.conflict.append(c)
                    break

        self.message.extend(['In questo ordine'] +
                            [str(self.pos_ind_dict[pos]) for pos in self.route]+[''])
        self.options['solve'] = True

    def get_pos(self, ind):
        ind = str(ind)
        tmp_query = parse(
            'posizione('+ind+',X,Y,Floor).')
        out = clean(self.engine.prove(tmp_query))
        if out == ['False']:
            return
        x, y, floor = int(out[0][0].const), int(
            out[0][1].const), int(out[0][2].const)
        return x, y, floor

    def update_path(self, delta_time, ass_lbls, ass_colors):
        if not self.path and self.options['solving']:
            if self.solve_timer >= 1:
                self.message.extend(
                    ['Ho risolto '+self.options['solving']])
                del self.engine.kb[self.engine.kb.index(
                    Clause(self.conflict[0]))]
                del self.engine.ass[self.engine.ass.index(self.conflict[0])]
                del self.engine.empty_body_clauses[self.engine.empty_body_clauses.index(
                    Clause(self.conflict[0]))]

                str_ass = [str(ass) for ass in self.engine.ass]
                for i, ass in enumerate(ass_lbls):
                    if ass_colors[i] and ass not in str_ass:
                        ass_colors[i] = not ass_colors[i]

                del self.conflict[0]

                self.options['solving'] = None
                self.solve_timer = 0
            else:
                self.solve_timer += delta_time
        if self.route and not self.path:
            if self.timer >= 1:
                goal = self.route[0]
                del self.route[0]
                if not self.route:
                    self.options['solve'] = False
                self.timer = 0
                self.path = self.get_path(goal)
                ind = str(self.pos_ind_dict[goal])
                self.message.extend(
                    ['Sto risolvendo '+ind])
                self.options['solving'] = ind
                self.pos_ind_dict.pop(goal)
            else:
                self.timer += delta_time

    def get_path(self, pos):
        x, y, floor = pos[0], pos[1], pos[2]
        if floor == self.floor:
            return A_star(
                self.graphs[floor-1], [self.sprite.position], (x, y))
        else:
            self.floor_to_go = floor
            island_pos = get_island(self.sprite.position, (x, y))
            island_to_goal = A_star(self.graphs[floor-1], [island_pos], (x, y))
            if island_to_goal == []:
                return None
            robot_to_island = A_star(
                self.graphs[self.floor-1], [self.sprite.position], island_pos)
            if robot_to_island == []:
                return None

            return robot_to_island + island_to_goal[1:]


def clean(SLD_derivations, abduce=False):
    if abduce:
        tmp_answers = [ans[-1].body for ans in SLD_derivations]
        if len(tmp_answers) == 0:
            return ['False']
        answers = []
        for ans in tmp_answers:
            if ans not in answers:
                answers.append(ans)
        return answers
    tmp_answers = [der[-1].head.args for der in SLD_derivations]
    answers = []
    for answer in tmp_answers:
        if answer not in answers:
            answers.append(answer)

    if len(answers) == 0:
        return ['False']

    elif len(answers) == 1 and len(answers[0]) == 0:
        return ['True']

    return answers


def get_island(p1, p2):
    eu_stairs = euclidean_distance(p1, STAIRS_POS)
    eu_elevator = euclidean_distance(
        p1, ELEVATOR_POS)
    eu_stairs += euclidean_distance(STAIRS_POS, p2)
    eu_elevator += euclidean_distance(ELEVATOR_POS, p2)
    return STAIRS_POS if eu_stairs < eu_elevator else ELEVATOR_POS
