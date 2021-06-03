from math import perm, sqrt
from copy import deepcopy
from itertools import permutations


class Constraint_ext:
    def __init__(self, constraint: list = [], domain: list = []):
        self.constraint = constraint
        self.domain = domain

    def min(self, var):
        tmp_c = Constraint_ext(deepcopy(self.constraint),
                               deepcopy(self.domain))
        i = tmp_c.domain.index(var)
        del tmp_c.domain[i]
        for row in tmp_c.constraint:
            del row[i]

        tmp_constraint = []
        done = []
        for row1 in tmp_c.constraint:
            if not row1[:-1] in done:
                done.append(row1[:-1])
                min_c = row1
                for row2 in tmp_c.constraint:
                    if row2[-1] < row1[-1] and row1[:-1] == row2[:-1]:
                        min_c = row2
                tmp_constraint.append(min_c)
        tmp_c.constraint = tmp_constraint
        return tmp_c

    def min_ass(self):
        min = self.constraint[0]
        for row in self.constraint:
            if row[-1] < min[-1]:
                min = row
        d = {}
        for i, var in enumerate(self.domain):
            d[var] = min[i]
        return d

    def __add__(self, other):
        tmp_domain = self.domain.copy()
        tmp_constraint = []
        intersection = []
        difference = []
        for var in other.domain:
            if var not in tmp_domain:
                tmp_domain.append(var)
            else:
                intersection.append(var)
        for var in tmp_domain:
            if var not in intersection:
                difference.append(var)
        tmp_domain = sorted(tmp_domain)
        inter_pos_list = []
        for elem in intersection:
            inter_pos_list.append(
                (self.domain.index(elem), other.domain.index(elem)))

        for row1 in self.constraint:
            for row2 in other.constraint:
                flag = True
                for pos in inter_pos_list:
                    if row1[pos[0]] != row2[pos[1]]:
                        flag = False
                        break
                if flag:
                    tmp_row1 = row1[:-1].copy()
                    tmp_row2 = []
                    pos_list_2 = [pos[1] for pos in inter_pos_list]
                    for i, elem in enumerate(row2[:-1]):
                        if i not in pos_list_2:
                            tmp_row2.append(elem)
                    tmp_constraint.append(
                        tmp_row1+tmp_row2+[row1[-1]+row2[-1]])
        return Constraint_ext(tmp_constraint, tmp_domain)

    def __str__(self):
        s = str(self.domain)+' cost\n'
        for row in self.constraint:
            s += str(row)+'\n'
        return s


def dist(p1, p2):
    return sqrt(pow(p1[0]-p2[0], 2)+pow(p1[1]-p2[1], 2))


def get_routes(pos_array):
    perms = list(permutations(pos_array))
    for i in range(len(perms)):
        perms[i] = list(perms[i])
        distance = 0
        for j in range(len(perms[i])-1):
            distance += dist(perms[i][j], perms[i][j+1])
        perms[i].append(distance)
    return perms


def get_table(pos_array):
    done = []
    for p1 in pos_array:
        for p2 in pos_array:
            if p1 != p2:
                done.append([p1, p2, dist(p1, p2)])
    return done


def ve_csp(vars: list, consts: list):
    def sum_const(arr):
        c = deepcopy(arr[0])
        for tmp_c in arr[1:]:
            c += tmp_c
        return c

    def opt_val(s, var, t):
        diff = []
        for v in t.domain:
            if v != var:
                diff.append(v)
        min = t.constraint[0]
        for row in t.constraint:
            for v in diff:
                if s[v] != row[t.domain.index(v)]:
                    break
            if row[-1] < min[-1]:
                min = row
        return {var: min[t.domain.index(var)]}
    if len(vars) == 1 or len(consts) == 1:
        c = sum_const(consts)
        return c.min_ass()

    else:
        var = vars[0]
        r = []
        for c in consts:
            if var in c.domain:
                r.append(c)

        t = sum_const(r)
        n = t.min(var)
        vars.remove(var)
        for c in r:
            if c in consts:
                consts.remove(c)
        consts.append(n)
        s = ve_csp(vars, consts)
        x_opt = opt_val(s, var, t)

        return {**s, **x_opt}


pos_array = [(0, 0), (1, 1), (4, -2), (-3, 2)]
vars = ['A', 'B', 'C', 'D']
const = [Constraint_ext(get_table(pos_array), ['A', 'B']),
         Constraint_ext(get_table(pos_array), ['B', 'C']),
         Constraint_ext(get_table(pos_array), ['C', 'D'])]


routes = sorted(get_routes(pos_array), key=lambda route: route[-1])

for r in routes:
    print(r)
