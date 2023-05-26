from graph import Graph

grafo = Graph()
grafo.add_node("Bia")
grafo.add_node("Caio")
grafo.add_node("Liz")
grafo.add_node("Alex")
grafo.add_edge("Caio", "Liz")
grafo.add_edge("Caio", "Alex")
grafo.add_edge("Liz", "Caio")
grafo.add_edge("Alex", "Liz")
print(grafo)