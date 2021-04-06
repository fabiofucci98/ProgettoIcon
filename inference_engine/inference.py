from collections import namedtuple
import re

Clause = namedtuple('Clause', 'head body')


def parse():
    kb = []
    f = open('kb', 'r')
    for line in f:
        prop = re.findall('[a-zA-Z_]+', line)
        kb.append(Clause(prop[0], prop[1:]))
    return kb


class Engine(object):
    def __init__(self) -> None:
        self.kb = parse()

    def ask(self, query: list):
        frontier = [[query]]
        while len(frontier) != 0:
            path = frontier[-1]
            del frontier[-1]
            if len(path[-1]) == 0:
                return True, path
            for edge in self.find_neighbours(path[-1]):
                if edge in path:
                    continue
                new_path = path.copy()
                new_path.append(edge)
                frontier.append(new_path)

        return False, None

    def how(self, query):
        answer = self.ask(query)[1]
        if not answer:
            return
        query = answer[0]
        for atom in query:
            for rule in self.kb:
                if atom == rule.head:
                    neighbour = query.copy()
                    del neighbour[neighbour.index(atom)]
                    neighbour.extend(rule.body)
                if neighbour == answer[1]:
                    return rule

    def find_neighbours(self, query: list):
        neighbours = []
        for atom in query:
            for rule in self.kb:
                if atom == rule.head:
                    neighbour = query.copy()
                    del neighbour[neighbour.index(atom)]
                    neighbour.extend(rule.body)
                    neighbours.append(neighbour)
        return neighbours


e = Engine()
print(e.ask(['g'])[0])
print(e.how(['g']))
