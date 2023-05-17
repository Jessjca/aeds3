from Aluno import Aluno
a1 = Aluno("Bia", 19, 9.2, 0.8)
a2 = Aluno("Caio", 22, 4.5, 0.75)
print(a1.nome, a1.idade)
print(a2.nome, a2.idade)
a2.nota = 10.0
print(a2.nota)
print(a2.aprovado()) #False, pois freq ficou 0.0