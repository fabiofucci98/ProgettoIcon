from re import findall
from copy import deepcopy
from typing import List


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
    def __init__(self, const):
        self.const = const

    def __str__(self):
        return str(self.const)

    def __repr__(self):
        return str(self.const)

    def __eq__(self, o: object):
        return isinstance(o, Constant) and self.const == o.const


class Engine(object):

    def __init__(self) -> None:
        self.kb = []

    """
    Carica la kb, la carica da un file di deafult se non riesce con il file filename
    """

    def load_kb(self, filename=None):
        f = None
        for tries in range(3):
            try:
                f = open(filename, 'r')
                break
            except (TypeError, FileNotFoundError):
                pass

            if tries == 1:
                filename = 'kb_rel'
        if tries == 3:
            return

        for line in f:
            preds = self.parse_query(line)
            if preds:
                self.kb.append(Clause(preds[0], preds[1:]))

    """
    Restituisce tutti i predicati contenuti nella stringa query
    """

    def parse_query(self, query):
        def parse_pred(pred):
            l = findall('[a-zA-Z0-9_]+', pred)
            for i in range(1, len(l)):
                l[i] = Variable(
                    l[i]) if l[i][0].isupper() else Constant(l[i])
            pred = Predicate(l[0], l[1:])
            return pred
        return [parse_pred(pred) for pred in findall('[a-zA-Z0-9_]+(?:\([a-zA-Z0-9_,]+\))?', query)]

    """
    Genera le derivazioni SLD ottenute a partire da query, vedere libro per documentazione dettagliata
    """

    def prove(self, query: list, prove_one=False):
        def derive(gac):
            neighbours = []
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
                            neighbours.append(self.__substitute(tmp_gac, sub))
                elif not atom.contains_vars():
                    if not self.prove([atom.negate()]):
                        neighbour = deepcopy(gac)
                        del neighbour.body[idx]
                        neighbours.append(neighbour)
                    else:
                        return []
                else:
                    continue
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

        SLD_derivations = []
        frontier = [[self.get_gac(query)]]
        while len(frontier) != 0:
            path = frontier[-1]
            del frontier[-1]
            if len(path[-1].body) == 0:
                if path not in SLD_derivations:
                    if prove_one:
                        return True
                    SLD_derivations.append(path)
                    continue
            neighbours = derive(path[-1])
            for edge in neighbours:
                if edge in path:
                    continue
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
                    replace(a, b, eqs, subs)
                    subs.append([a, b])
                elif isinstance(b, Variable):
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
