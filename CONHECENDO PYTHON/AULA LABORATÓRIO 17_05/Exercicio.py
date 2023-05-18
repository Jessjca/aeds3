class Exercicio:
    def ehvizinho(grafo_mat,i,j):
        return grafo_mat[i][j] == 1

    def ehvizinholista(grafo_lista,i,j):
        return i in grafo_lista[j]