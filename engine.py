import string
from copy import deepcopy


class Clause:
    def __init__(self, head, body=[]):
        self.head = head
        self.body = body

    def __str__(self):
        tmp_str = str(self.head) + ': '
        for i, atom in enumerate(self.body):
            tmp_str += str(atom)
            if i != len(self.body)-1:
                tmp_str += ', '
        return tmp_str

    def __repr__(self):
        tmp_str = str(self.head) + ': '
        for i, atom in enumerate(self.body):
            tmp_str += str(atom)
            if i != len(self.body)-1:
                tmp_str += ', '
        return tmp_str

    def __eq__(self, o: object):
        return isinstance(o, Clause) and self.head == o.head and self.body == o.body


class Predicate:
    def __init__(self, pred, args=[]):
        self.pred = pred
        self.args = args
        self.negated = True if len(
            self.pred) > 4 and self.pred[0:4] == 'not_' else False

    def __str__(self):
        tmp_str = str(self.pred)
        if len(self.args) > 0:
            tmp_str += '('
            for i, arg in enumerate(self.args):
                tmp_str += str(arg)
                if i != len(self.args)-1:
                    tmp_str += ', '
            tmp_str += ')'
        return tmp_str

    def __repr__(self):
        tmp_str = str(self.pred)
        if len(self.args) > 0:
            tmp_str += '('
            for i, arg in enumerate(self.args):
                tmp_str += str(arg)
                if i != len(self.args)-1:
                    tmp_str += ', '
            tmp_str += ')'
        return tmp_str

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
        tmp_str = str(self.const)
        if len(self.args) > 0:
            tmp_str += '('
            for i, arg in enumerate(self.args):
                tmp_str += str(arg)
                if i != len(self.args)-1:
                    tmp_str += ', '
            tmp_str += ')'
        return tmp_str

    def __repr__(self):
        tmp_str = str(self.const)
        if len(self.args) > 0:
            tmp_str += '('
            for i, arg in enumerate(self.args):
                tmp_str += str(arg)
                if i != len(self.args)-1:
                    tmp_str += ', '
            tmp_str += ')'
        return tmp_str

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

    def __init__(self, built_in_funcs={}, built_in_preds={}) -> None:
        self.kb = []
        self.ass = []
        self.empty_body_clauses = []
        self.built_in_funcs = built_in_funcs
        self.built_in_preds = built_in_preds

    """
    Carica la kb da filename
    """

    def load_kb(self, filename):

        f = open(filename, 'r')
        kb = []
        ass = []
        empty_body_clauses = []
        ass_flag = False
        for line in f:
            line = line.strip()
            if line == '':
                continue

            if line == 'ass:':
                ass_flag = True
                continue

            preds = parse(line)
            if preds:
                clause = Clause(preds[0], preds[1:])
                kb.append(clause)
                if len(preds[1:]) == 0:
                    empty_body_clauses.append(clause)
            if ass_flag and len(preds) == 1:
                ass.append(preds[0])
            elif ass_flag and len(preds) > 1:
                raise ParseException

        self.kb = kb
        self.ass = ass
        self.empty_body_clauses = empty_body_clauses

    """
    Genera le derivazioni SLD ottenute a partire da query
    """

    def prove(self, query: list, prove_one=False, abduce=False, occurs_check=True):
        def derive(gac, abduce, occurs_check):
            def solve_f(gac):
                def rec_solve(const):

                    args = []
                    for arg in const.args:
                        args.append(rec_solve(arg))
                    const.args = args
                    if const.const in self.built_in_funcs:
                        return self.built_in_funcs[const.const](*const.args)
                    else:
                        return const

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
                    if atom.pred in self.built_in_preds:
                        try:
                            f = self.built_in_preds[atom.pred]
                            if f(*atom.args):
                                tmp_gac = deepcopy(gac)
                                del tmp_gac.body[idx]
                                neighbours.append(tmp_gac)
                                continue
                            else:
                                return []
                        except Exception:
                            pass
                    for clause in self.kb:
                        renamed_clause = self.__rename_vars(
                            deepcopy(clause))
                        sub = self.__unify(
                            renamed_clause.head, atom, occurs_check)
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
            def rec_reset(term):
                if isinstance(term, Variable):
                    term.reset()
                else:
                    for arg in term.args:
                        rec_reset(arg)
            for clause in self.kb:
                for term in clause.head.args:
                    rec_reset(term)
                for pred in clause.body:
                    for term in pred.args:
                        rec_reset(term)

        def abduce_criterion(G):
            for atom in G.body:
                if atom not in self.ass:
                    return False

            return True

        def simplify(gac, abduce):
            tmp_gac = deepcopy(gac)
            for atom in tmp_gac.body:
                if abduce and atom in self.ass:
                    continue
                if atom.contains_vars():
                    continue
                idx = tmp_gac.body.index(atom)
                if atom.pred in self.built_in_preds:
                    try:
                        f = self.built_in_preds[atom.pred]
                        if f(*atom.args):
                            del tmp_gac.body[idx]
                    except Exception:
                        pass
                else:
                    for clause in self.empty_body_clauses:
                        renamed_clause = self.__rename_vars(
                            deepcopy(clause))
                        sub = self.__unify(
                            renamed_clause.head, atom, occurs_check)
                        if isinstance(sub, list):
                            del tmp_gac.body[idx]
                            tmp_gac.body[idx:idx] = renamed_clause.body
                            tmp_gac = self.__substitute(tmp_gac, sub)
                            break
            return tmp_gac

        SLD_derivations = []
        frontier = [[self.__get_gac(query)]]

        while len(frontier) != 0:
            path = frontier[-1]
            simp = simplify(path[-1], abduce)
            if simp != path[-1]:
                path.append(simp)
            del frontier[-1]
            if (len(path[-1].body) == 0 and not abduce) or (abduce and abduce_criterion(path[-1])):
                if path not in SLD_derivations:
                    if prove_one:
                        reset_vars()
                        return [path]
                    SLD_derivations.append(path)
                    continue
            neighbours = derive(path[-1], abduce, occurs_check)
            for edge in neighbours:
                if edge in path:
                    continue
                new_path = path.copy()
                new_path.append(edge)
                frontier.append(new_path)

        reset_vars()
        return SLD_derivations

    def __rename_vars(self, clause):
        def rec_rename(term):
            if isinstance(term, Variable):
                term.inc()
            else:
                for arg in term.args:
                    rec_rename(arg)
        for term in clause.head.args:
            rec_rename(term)
        for pred in clause.body:
            for term in pred.args:
                rec_rename(term)
        return clause

    def __substitute(self, clause, subs):
        def rec_sub(term, to_sub, subs):
            if term in to_sub:
                return subs[to_sub.index(term)][1]
            elif isinstance(term, Variable):
                return term
            else:
                term.args = [rec_sub(arg, to_sub, subs) for arg in term.args]
                return term

        to_sub = [sub[0] for sub in subs]
        for i in range(len(clause.head.args)):
            clause.head.args[i] = rec_sub(clause.head.args[i], to_sub, subs)

        for pred in clause.body:
            for j in range(len(pred.args)):
                pred.args[j] = rec_sub(pred.args[j], to_sub, subs)
        return clause

    def __unify(self, t1, t2, occurs_check_var):
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
            def rec_replace(a, b, term):
                if term == a:
                    return b
                elif isinstance(term, Variable):
                    return term
                else:
                    term.args = [rec_replace(
                        a, b, arg) for arg in term.args]
                    return term

            for i in range(len(eqs)):
                for j in range(len(eqs[i])):
                    eqs[i][j] = rec_replace(a, b, eqs[i][j])

            for i in range(len(subs)):
                for j in range(len(subs[i])):
                    subs[i][j] = rec_replace(a, b, subs[i][j])

        eqs = [[t1, t2]]
        subs = []
        while len(eqs) != 0:
            a, b = eqs[0]
            del eqs[0]

            if a != b:
                if isinstance(a, Variable):
                    if occurs_check_var and isinstance(b, Constant) and occur_check(a, b):
                        return None
                    replace(a, b, eqs, subs)
                    subs.append([a, b])
                elif isinstance(b, Variable):
                    if occurs_check_var and isinstance(a, Constant) and occur_check(b, a):
                        return None
                    replace(b, a, eqs, subs)
                    subs.append(([b, a]))
                elif isinstance(a, Predicate) and isinstance(b, Predicate) and len(a.args) == len(b.args) and a.pred == b.pred and len(a.args) > 0:
                    for ai, bi in zip(a.args, b.args):
                        if isinstance(ai, Variable) and isinstance(bi, Variable):
                            eqs.insert(0, [ai, bi])

                        else:
                            eqs.append([ai, bi])
                elif isinstance(a, Constant) and isinstance(b, Constant) and len(a.args) == len(b.args) and a.const == b.const and len(a.args) > 0:
                    for ai, bi in zip(a.args, b.args):
                        if isinstance(ai, Variable) and isinstance(bi, Variable):
                            eqs.insert(0, [ai, bi])

                        else:
                            eqs.append([ai, bi])
                else:
                    return None
        return subs

    def __get_gac(self, query):
        flat_list = []

        def get_vars(term):
            if isinstance(term, Variable):
                return term
            vars = []
            for arg in term.args:
                vars.append(get_vars(arg))
            return vars

        def flatten_list(data):
            for element in data:
                if type(element) == list:
                    flatten_list(element)
                else:
                    flat_list.append(element)

        gac = Clause(Predicate('yes', []), query)
        vars = []
        for pred in query:
            for term in pred.args:
                vars.append(get_vars(term))
        flatten_list(vars)
        gac.head.args = flat_list
        return gac

    def how(self, atom: Predicate, occurs_check=True):
        if atom.negated:
            return [['naf']]
        rules = []
        SLD_ders = self.prove([atom], occurs_check=occurs_check)
        for der in SLD_ders:
            for clause in self.kb:
                renamed_clause = self.__rename_vars(deepcopy(clause))
                sub = self.__unify(
                    renamed_clause.head, atom, occurs_check)
                if isinstance(sub, list):
                    tmp_gac = deepcopy(der[0])
                    del tmp_gac.body[0]
                    tmp_gac.body[0:0] = renamed_clause.body
                    if der[1] == self.__substitute(tmp_gac, sub) and clause not in rules:
                        rules.append(clause)

        return rules

    def __str__(self):
        s = 'KB\n'
        for clause in self.kb:
            s += str(clause)+'\n'
        s += 'ASS\n'
        for clause in self.ass:
            s += str(clause)+'\n'
        return s

    def __repr__(self):
        s = 'KB\n'
        for clause in self.kb:
            s += str(clause)+'\n'
        s += 'ASS\n'
        for clause in self.ass:
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
