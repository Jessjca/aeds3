def somar_elementos(lista):
    soma = 0
    for elemento in lista:
        soma += elemento
    return soma

def encontra_min_max(elementos):
    min = float("inf")
    max = float("-inf")
    for i  in range (len(elementos)):
        if elementos[i]<min:
            min = elementos[i]
        if elementos[i]>max:
            max = elementos[i]
    return(min,max)