from re import findall
from copy import deepcopy


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
    def __init__(self, predicate, arguments=[]):
        self.predicate = predicate
        self.arguments = arguments

    def __str__(self):
        return str(self.predicate)+str(self.arguments)

    def __repr__(self):
        return str(self.predicate)+str(self.arguments)

    def __eq__(self, o: object):
        return isinstance(o, Predicate) and self.predicate == o.predicate and self.arguments == o.arguments


class Variable:
    def __init__(self, variable):
        self.variable = variable
        self.n_renamed = 0

    def inc(self):
        self.n_renamed += 1

    def reset(self):
        self.n_renamed = 0

    def __str__(self):
        return str(self.variable)+str(self.n_renamed)

    def __repr__(self):
        return str(self.variable)+str(self.n_renamed)

    def __eq__(self, o: object):
        return isinstance(o, Variable) and self.variable == o.variable


class Constant:
    def __init__(self, constant):
        self.constant = constant

    def __str__(self):
        return str(self.constant)

    def __repr__(self):
        return str(self.constant)

    def __eq__(self, o: object):
        return isinstance(o, Constant) and self.constant == o.constant


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
            preds = findall('[a-zA-Z0-9_]+(?:\([a-zA-Z0-9_,]+\))?', line)
            preds = [self.parse_pred(pred) for pred in preds]
            self.kb.append(Clause(preds[0], preds[1:]))
    """
    Restituisce tutti i predicati contenuti nella stringa query
    """

    def parse_query(self, query):
        return [self.parse_pred(pred) for pred in findall('[a-zA-Z0-9_]+(?:\([a-zA-Z0-9_,]+\))?', query)]

    """
    Restituisce il predicato contenuto nella stringa query
    """

    def parse_pred(self, pred):
        l = findall('[a-zA-Z0-9_]+', pred)
        for i in range(1, len(l)):
            l[i] = Variable(
                l[i]) if l[i][0].isupper() else Constant(l[i])
        pred = Predicate(l[0], l[1:])
        return pred

    """
    Effettua una query, prende in input una lista di predicati, 
    restituisce una versione "pulita" delle derivazioni SLD generate con Engine.get_SLD_derivations
    """

    def ask(self, query: list):
        """
        Pulisce le derivazioni SLD in input, restituisce una stringa rappresentante la lista di tuple di individui per i quali la  
        risoluzione ha avuto successo se ce ne sono, "True" se non ce ne sono ma la risoluzione ha avuto successo, "False" altrimenti
        """
        def clean(SLD_derivations):
            if not SLD_derivations:
                return 'False'

            tmp_answers = [der[-1].head.arguments for der in SLD_derivations]
            answers = []
            for answer in tmp_answers:
                if answer not in answers:
                    answers.append(answer)

            out = ''
            for answer in answers:
                for i, individual in enumerate(answer):
                    out += str(individual)
                    if i < len(answer)-1:
                        out += ', '
                out += '\n'
            if out == '\n':
                return 'True'
            return out

        return clean(self.get_SLD_derivations(query))

    """
    Genera le derivazioni SLD ottenute a partire da query, vedere libro per documentazione dettagliata
    """

    def get_SLD_derivations(self, query: list):

        def substitute(clause, substitution):
            to_substitute = [sub[0] for sub in substitution]
            clause = deepcopy(clause)
            for i in range(len(clause.head.arguments)):
                if clause.head.arguments[i] in to_substitute:
                    clause.head.arguments[i] = substitution[to_substitute.index(
                        clause.head.arguments[i])][1]

            for pred in clause.body:
                for j in range(len(pred.arguments)):
                    if pred.arguments[j] in to_substitute:
                        pred.arguments[j] = substitution[to_substitute.index(
                            pred.arguments[j])][1]
            return clause

        def unify(t1, t2):
            def replace(a, b, equalities, substitutions):
                for i in range(len(equalities)):
                    for j in range(len(equalities[i])):
                        if equalities[i][j] == a:
                            equalities[i][j] = b
                for i in range(len(substitutions)):
                    for j in range(len(substitutions[i])):
                        if substitutions[i][j] == a:
                            substitutions[i][j] = b
            equalities = [[t1, t2]]
            substitutions = []
            while len(equalities) != 0:
                a, b = equalities[0]
                del equalities[0]
                if a != b:
                    if isinstance(a, Variable):
                        replace(a, b, equalities, substitutions)
                        substitutions.append([a, b])
                    elif isinstance(b, Variable):
                        replace(b, a, equalities, substitutions)
                        substitutions.append(([b, a]))
                    elif isinstance(a, Predicate) and isinstance(b, Predicate) and len(a.arguments) == len(b.arguments) and a.predicate == b.predicate and len(a.arguments) > 0:
                        for ai, bi in zip(a.arguments, b.arguments):
                            equalities.append([ai, bi])
                    else:
                        return None
            return substitutions

        def rename_variables(clause):
            tmp_clause = deepcopy(clause)
            for term in tmp_clause.head.arguments:
                if isinstance(term, Variable):
                    term.inc()
            for pred in tmp_clause.body:
                for term in pred.arguments:
                    if isinstance(term, Variable):
                        term.inc()
            return tmp_clause

        def find_neighbours(gac):
            neighbours = []
            for atom in gac.body:
                for clause in self.kb:
                    if clause.head == atom:
                        idx = gac.body.index(atom)
                        tmp_gac = deepcopy(gac)
                        del tmp_gac.body[idx]
                        tmp_gac.body[idx:idx] = clause.body
                        neighbours.append(tmp_gac)
                    renamed_clause = rename_variables(clause)
                    sub = unify(renamed_clause.head, atom)
                    if sub:
                        idx = gac.body.index(atom)
                        tmp_gac = deepcopy(gac)
                        del tmp_gac.body[idx]
                        tmp_gac.body[idx:idx] = renamed_clause.body
                        neighbours.append(substitute(tmp_gac, sub))
            return neighbours

        def reset_variables():

            for clause in self.kb:
                for term in clause.head.arguments:
                    if isinstance(term, Variable):
                        term.reset()
                for pred in clause.body:
                    for term in pred.arguments:
                        if isinstance(term, Variable):
                            term.reset()

        gac = Clause(Predicate('yes', []), query)
        for pred in query:
            for term in pred.arguments:
                if isinstance(term, Variable):
                    gac.head.arguments.append(term)
        gacs = []
        frontier = [[gac]]
        while len(frontier) != 0:
            path = frontier[-1]
            del frontier[-1]
            if len(path[-1].body) == 0:
                if path not in gacs:
                    gacs.append(path)
            for edge in find_neighbours(path[-1]):
                new_path = path.copy()
                new_path.append(edge)
                frontier.append(new_path)

        reset_variables()
        return gacs

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
