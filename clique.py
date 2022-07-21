from itertools import combinations
import numpy as np


class Clique:

    def __init__(self, vertices, metric):
        self.vertices = vertices
        self.metric = metric

    def total_group_weights(self, group):
        edges = combinations(self.vertices, 2)
        accu = np.zeros(group.shape[0])
        for e in edges:
            accu = accu + group[:, e[0], e[1]]
        return accu

    def mat_weights(self, mat):
        edges = combinations(self.vertices, 2)
        weight = 0.0
        for e in edges:
            weight = weight + mat[e[0]][e[1]]
        return weight

    def __lt__(self, other):
        return self.metric < other.metric

    def __str__(self):
        return '{}, {:.3f}'.format(self.vertices, self.metric)

    @classmethod
    def create_cliques(cls, vertices_combo, mat):
        cliques = []
        for vertices in vertices_combo:
            edges = combinations(vertices, 2)
            weight = 0.0
            for e in edges:
                weight = weight + mat[e[0]][e[1]]
            cliques.append(Clique(vertices, weight))
        return cliques
