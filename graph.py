class Graph:
    def __init__(self, barrier_list):
        def collides():
            pass
        self.nodes = []
        self.edges = []
        for x in range(0, 800, 50):
            for y in range(0, 800, 50):
                self.nodes.append(Node((x, y)))
        for node1 in self.nodes:
            for node2 in self.nodes:
                if node1 != node2:
                    self.edges.append(Edge(node1, node2))

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        self.edges.append(edge)


class Node:
    def __init__(self, value=None):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value if type(other) == Node else False

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)


class Edge:
    def __init__(self, n1, n2, cost=0):
        self.n1 = n1
        self.n2 = n2
        self.cost = cost

    def __eq__(self, other):
        return self.n1 == other.n1 and self.n2 == other.n2 and self.cost == other.cost

    def __repr__(self):
        return str(self.n1)+' '+str(self.n2)+str(self.cost)

    def __str__(self):
        return str(self.n1)+' '+str(self.n2)+str(self.cost)
