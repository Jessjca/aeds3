class Graph:
    def __init__(self):
        self.adj_list = {} # Dicionário ou tabela hash
        self.node_count = 0 # Dicionário ou tabela hash
        self.edge_count = 0 # Dicionário ou tabela hash

    def __str__(self):
        out = "Nodes: " + str(self.node_count) + "\n"
        out += "Edges: " + str(self.edge_count) + "\n"
        out += str(self.adj_list)
        return out

    def add_node(self, node):
        if node in self.adj_list:
            print(f"WARN Node {node} already exists")
            return
        self.adj_list[node] = {}
        self.node_count += 1

    def add_edge (self, node1, node2):
        try:
            self.adj_list[node1].append(node2)
            self.edge_count += 1
            
        except KeyError as e:
            print(f"WARN: Node {e} does exist in the graph")

    def add_nodes(self,nodes):
        for node in nodes:
            self.add_node(node)

    def add_two_way_edge(self, node1, node2):
        self.add_edge(node1,node2)
        self.add_edge(node2,node1)

    def remove_edge(self, node1, node2):
        try:
            self.adj_list[node1].append(node2)
            self.edge_count -= 1
        except KeyError as e:
            print(f"WARN: Node {e} does exist in the graph")