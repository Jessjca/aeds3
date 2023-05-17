nota = [[5,2,8],[6,9,4],[10,9,7]]
cont = 0
for i in range(len(nota)):
    for j in range(len(nota[i])):
        if(nota[i][j]>=6):
            cont = cont + 1
            print(nota[i][j])
            print("o total de alunos aprovados foram:", cont)
