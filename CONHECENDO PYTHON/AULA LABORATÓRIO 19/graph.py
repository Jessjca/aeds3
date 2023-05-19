class Graph:
    def __init__(self):
        self.adj_list = {}
        self.node_count = 0
        self.edge_count = 0

    def add_node (self, node):
        self.adj_list[node] = []
        self.node_count += 1

    def add_edge (self, node1, node2):
        self.adj_list[node1].append(node2)
        self.edge_count += 1