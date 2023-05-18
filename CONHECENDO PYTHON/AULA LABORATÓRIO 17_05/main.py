from Aluno import Aluno
a1 = Aluno("Bia", 19, 9.2, 0.8)
a2 = Aluno("Caio", 22, 4.5, 0.75)
print(a1.nome, a1.idade)
print(a2.nome, a2.idade)
a2.nota = 10.0
print(a2.nota)
print(a2.aprovado()) #False, pois freq ficou 0.0


#Verificar de 1 é vizinho de 3.

grafo_mat = [[0,0,0,0],
             [0,0,1,1],
             [0,1,0,1],
             [0,1,1,0]]

if grafo_mat[1][3] == 1: #O(1)
    print("Sim")
else:
    print("Não")

#Verificar de 1 é vizinho de 3.

grafo_mat = [[0,0,0,0],
             [0,0,1,1],
             [0,1,0,1],
             [0,1,1,0]]

print(grafo_mat[1][3] == 1) #O(1)

#Verificar de 1 é vizinho de 3.

grafo_lista = [[],
               [2,3],
               [1,3],
               [1,2]]

eh_vizinho = False

for vizinho in grafo_lista[1]: #O(N)
    if vizinho == 3:
        eh_vizinho = True
        break

print(eh_vizinho)

#Verificar de 1 é vizinho de 3.

grafo_lista = [[],
               [2,3],
               [1,3],
               [1,2]]

print(3 in grafo_lista[1]) #O(N)


#Faça funções que recebe 2 nós e informa se eles são vizinhos.

grafo_mat = [[0,0,0,0],
             [0,0,1,1],
             [0,1,0,1],
             [0,1,1,0]]

print(grafo_mat[1][3] == 1) #O(1)