def encontra_menor(elementos):
    menor = 1000000
    for i in range(len(elementos)):
        if elementos[i]<menor:
            menor = elementos[i]
    return menor
a = [5,8,-2,4,0]
print("Menor elemento de a:", encontra_menor(a))