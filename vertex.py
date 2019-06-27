class Vertex:

    id = None
    edges = []
    color = None
    sat_degree = 0

    def __init__(self, id):
        self.id = id

    def __str__(self):
        return str(self.id)

    def get_degree(self):
        return len(self.edges)

    def get_sat_degree(self):
        # count = 0
        # for edge in edges:
        #     if edge.color is None:
        #         count += 1
        # return count
        return self.sat_degree
