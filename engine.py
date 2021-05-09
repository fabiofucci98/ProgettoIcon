import string
from copy import deepcopy
from built_in import built_in_preds, built_in_funcs


class Clause:
    def __init__(self, head, body=[]):
        self.head = head
        self.body = body

    def __str__(self):
        return str(self.head)+' :- '+str(self.body)

    def __repr__(self):
        return str(self.head)+' :- '+str(self.body)

    def __eq__(self, o: object):
        return isinstance(o, Clause) and self.head == o.head and self.body == o.body


class Predicate:
    def __init__(self, pred, args=[]):
        self.pred = pred
        self.args = args
        self.negated = True if len(
            self.pred) > 4 and self.pred[0:4] == 'not_' else False

    def __str__(self):
        return str(self.pred)+str(self.args)

    def __repr__(self):
        return str(self.pred)+str(self.args)

    def __eq__(self, o: object):
        return isinstance(o, Predicate) and self.pred == o.pred and self.args == o.args

    def negate(self):
        return Predicate(self.pred[4:], self.args) if self.negated else Predicate('not_' + self.pred, self.args)

    def contains_vars(self):
        for arg in self.args:
            if isinstance(arg, Variable):
                return True
        return False


class Variable:
    def __init__(self, var):
        self.var = var
        self.count = 0

    def inc(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def __str__(self):
        return str(self.var)

    def __repr__(self):
        return str(self.var)

    def __eq__(self, o: object):
        return isinstance(o, Variable) and self.var == o.var and self.count == o.count


class Constant:
    def __init__(self, const, args=[]):
        self.const = const
        self.args = args

    def __str__(self):
        return str(self.const)+str(self.args)

    def __repr__(self):
        return str(self.const)+str(self.args)

    def __eq__(self, o: object):
        if not isinstance(o, Constant):
            return False

        if len(self.args) != len(o.args):
            return False

        for i in range(len(self.args)):
            if self.args[i] != o.args[i]:
                return False
        return self.const == o.const


class Engine(object):

    def __init__(self) -> None:
        self.kb = []

    """
    Carica la kb, la carica da filename
    """

    def load_kb(self, filename=None):
        f = open(filename, 'r')
        kb = []
        ass = []
        ass_flag = False
        for line in f:
            if line[-1] == '\n':
                line = line[0:-1]
            if line == '':
                continue

            if line == 'ass:':
                ass_flag = True
                continue

            preds = parse(line)
            if preds:
                kb.append(Clause(preds[0], preds[1:]))

            if ass_flag and len(preds) == 1:
                ass.append(preds[0])
            elif ass_flag and len(preds) > 1:
                raise ParseException

        self.kb = kb
        self.ass = ass

    """
    Genera le derivazioni SLD ottenute a partire da query, vedere libro per documentazione dettagliata
    """

    def prove(self, query: list, prove_one=False, abduce=False):
        def derive(gac, abduce):
            def rec_solve(const):
                if const.const in built_in_funcs:
                    args = [rec_solve(arg) for arg in const.args]
                    for i in range(len(args)):
                        if not isinstance(args[i], Constant):
                            args[i] = Constant(str(args[i]))
                    const.args = args
                    return Constant(str(built_in_funcs[const.const](*const.args)))
                else:
                    return const

            def solve_f(gac):
                for i in range(len(gac.head.args)):
                    try:
                        sub = rec_solve(gac.head.args[i])
                        self.__substitute(gac, [[gac.head.args[i], sub]])
                    except:
                        pass
                for pred in gac.body:
                    for j in range(len(pred.args)):
                        try:
                            sub = rec_solve(pred.args[j])
                            self.__substitute(gac, [[pred.args[j], sub]])
                        except:
                            pass
                return gac

            gac = solve_f(gac)
            neighbours = []
            for atom in gac.body:
                if abduce and atom in self.ass:
                    continue
                idx = gac.body.index(atom)
                if not atom.negated:
                    if atom.pred in built_in_preds:
                        try:
                            f = built_in_preds[atom.pred]
                            if f(*atom.args):
                                tmp_gac = deepcopy(gac)
                                del tmp_gac.body[idx]
                                neighbours.append(tmp_gac)
                                continue
                        except Exception:
                            pass
                    for clause in self.kb:
                        renamed_clause = self.__rename_vars(
                            deepcopy(clause))
                        sub = self.__unify(renamed_clause.head, atom)
                        if isinstance(sub, list):
                            tmp_gac = deepcopy(gac)
                            del tmp_gac.body[idx]
                            tmp_gac.body[idx:idx] = renamed_clause.body
                            neighbours.append(
                                self.__substitute(tmp_gac, sub))
                elif not atom.contains_vars():
                    if not self.prove([atom.negate()]):
                        neighbour = deepcopy(gac)
                        del neighbour.body[idx]
                        neighbours.append(neighbour)
                    else:
                        return []
            return neighbours

        def reset_vars():
            for clause in self.kb:
                for term in clause.head.args:
                    if isinstance(term, Variable):
                        term.reset()
                for pred in clause.body:
                    for term in pred.args:
                        if isinstance(term, Variable):
                            term.reset()

        def abduce_criterion(G):
            for atom in G.body:
                if atom not in self.ass:
                    return False

            return True

        SLD_derivations = []
        closed_list = []
        frontier = [[self.get_gac(query)]]

        while len(frontier) != 0:
            path = frontier[-1]
            del frontier[-1]
            if path[-1] in closed_list:
                continue
            else:
                closed_list.append(path[-1])
            if (len(path[-1].body) == 0 and not abduce) or (abduce and abduce_criterion(path[-1])):
                if path not in SLD_derivations:
                    if prove_one:
                        reset_vars()
                        return path
                    SLD_derivations.append(path)
                    continue
            neighbours = derive(path[-1], abduce)
            for edge in neighbours:
                new_path = path.copy()
                new_path.append(edge)
                frontier.append(new_path)

        reset_vars()
        return SLD_derivations

    def __rename_vars(self, clause):
        for term in clause.head.args:
            if isinstance(term, Variable):
                term.inc()
        for pred in clause.body:
            for term in pred.args:
                if isinstance(term, Variable):
                    term.inc()
        return clause

    def __substitute(self, clause, subs):
        to_substitute = [sub[0] for sub in subs]
        # clause = deepcopy(clause)
        for i in range(len(clause.head.args)):
            if clause.head.args[i] in to_substitute:
                clause.head.args[i] = subs[to_substitute.index(
                    clause.head.args[i])][1]

        for pred in clause.body:
            for j in range(len(pred.args)):
                if pred.args[j] in to_substitute:
                    pred.args[j] = subs[to_substitute.index(
                        pred.args[j])][1]
        return clause

    def __unify(self, t1, t2):
        def occur_check(X, const):
            if isinstance(const, Variable):
                return X == const
            elif len(const.args) == 0:
                return False
            else:
                for arg in const.args:
                    if occur_check(X, arg):
                        return True

                return False

        def replace(a, b, eqs, subs):
            for i in range(len(eqs)):
                for j in range(len(eqs[i])):
                    if eqs[i][j] == a:
                        eqs[i][j] = b
            for i in range(len(subs)):
                for j in range(len(subs[i])):
                    if subs[i][j] == a:
                        subs[i][j] = b
        eqs = [[t1, t2]]
        subs = []
        while len(eqs) != 0:
            a, b = eqs[0]
            del eqs[0]

            if a != b:
                if isinstance(a, Variable):
                    if isinstance(b, Constant) and occur_check(a, b):
                        return None
                    replace(a, b, eqs, subs)
                    subs.append([a, b])
                elif isinstance(b, Variable):
                    if isinstance(a, Constant) and occur_check(b, a):
                        return None
                    replace(b, a, eqs, subs)
                    subs.append(([b, a]))
                elif isinstance(a, Predicate) and isinstance(b, Predicate) and len(a.args) == len(b.args) and a.pred == b.pred and len(a.args) > 0:
                    for ai, bi in zip(a.args, b.args):
                        eqs.append([ai, bi])
                else:
                    return None
        return subs

    def get_gac(self, query):
        gac = Clause(Predicate('yes', []), query)
        for pred in query:
            for term in pred.args:
                if isinstance(term, Variable):
                    gac.head.args.append(term)
        return gac

    def how(self, query: list):
        def find_rule(gac, der):
            flag = False
            for atom in gac.body:
                idx = gac.body.index(atom)
                if not atom.negated:
                    for clause in self.kb:
                        renamed_clause = self.__rename_vars(deepcopy(clause))
                        sub = self.__unify(renamed_clause.head, atom)
                        if isinstance(sub, list):
                            tmp_gac = deepcopy(gac)
                            del tmp_gac.body[idx]
                            tmp_gac.body[idx:idx] = renamed_clause.body
                            if der == self.__substitute(tmp_gac, sub):

                                return clause
                else:
                    flag = True
            if flag:
                return 'naf'

        SLD_ders = self.prove(query)
        if not SLD_ders:
            return None
        dir_ders = []
        for der in SLD_ders:
            if der[1] not in dir_ders:
                dir_ders.append(der[1])
        return [find_rule(self.get_gac(query), der) for der in dir_ders]

    def __str__(self):
        s = ''
        for clause in self.kb:
            s += str(clause)+'\n'
        return s

    def __repr__(self):
        s = ''
        for clause in self.kb:
            s += str(clause)+'\n'
        return s


class ParseException(Exception):
    pass


class Tree:
    def __init__(self, node=None, childs=None, parent=None):
        self.node = node
        self.childs = childs if childs != None else []
        self.parent = parent

    def __repr__(self):
        childs = ''
        for child in self.childs:
            childs += str(child)+','
        childs = childs[:-1]
        if len(childs) == 0:
            return str(self.node)
        return str(self.node)+'('+childs+')'

    def __str__(self):
        childs = ''
        for child in self.childs:
            childs += str(child)+','
        childs = childs[:-1]
        if len(childs) == 0:
            return str(self.node)

        return str(self.node)+'('+childs+')'


def parse(s):
    def get_tree(s):
        if s[-1] != '.':
            raise ParseException
        letters = string.ascii_letters
        numbers = '0123456789'
        elem = ''
        parentheses_check = 0
        tree = Tree()
        for i in range(len(s)):
            if s[i] in letters or s[i] == '_' or s[i] == '-' or s[i] == '/' or s[i] == '*' or s[i] in numbers:
                elem += s[i]
                continue
            if elem != '':
                tree.childs.append(Tree(node=elem, parent=tree))
            elem = ''
            if s[i] == '(':
                tree = tree.childs[-1]
                parentheses_check += 1
            elif s[i] == ')':
                tree = tree.parent
                parentheses_check -= 1

        if parentheses_check != 0:
            raise ParseException
        return tree

    def rec_parse(tree):
        def get_depth(tree):
            i = -1
            while tree.parent != None:
                i += 1
                tree = tree.parent

            return i

        if get_depth(tree) == 0:
            if tree.node[0].isupper():
                raise ParseException
            args = [rec_parse(child) for child in tree.childs]
            return Predicate(tree.node, args)

        elif tree.node[0].isupper():
            if len(tree.childs) > 0:
                raise ParseException
            return Variable(tree.node)
        else:
            args = [rec_parse(child) for child in tree.childs]
            return Constant(tree.node, args)
    tree = get_tree(s)
    return [rec_parse(child) for child in tree.childs]
