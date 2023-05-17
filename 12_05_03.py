def encontra_min_max(elementos):
    min = float("inf")
    max = float("-inf")
    for i  in range (len(elementos)):
        if elementos[i]<min:
            min = elementos[i]
        if elementos[i]>max:
            max = elementos[i]
    return(min,max)

a = [5, -2, 6, 4, 8]
print(encontra_min_max(a))
(min, max) = encontra_min_max(a)
print(min, max)