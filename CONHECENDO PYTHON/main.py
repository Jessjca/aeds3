from operacoes import somar_elementos, encontra_min_max
import math
from aluno import Aluno

'''a = [5, -2, 4, 8]
print("Min e max:", encontra_min_max(a))
print("Soma:", somar_elementos(a))'''

'''print(math.sqrt(9))
print (math.factorial(5))'''


a1 = Aluno("Bia", 19, 9.2, 0.8)
print(a1.nome, a1.idade)

a2 = Aluno("Caio", 22, 4.6, 0.75)
print(a2.nome, a2.idade)

a2.nota = 10.0
print(a2.nota)
