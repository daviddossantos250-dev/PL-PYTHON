#MATRIZ

matriz = [['X', ' ', ' '], [' ', 'X', 'O'], [' ', ' ', 'X']]

#PERCORRER A MATRIZ
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=' ')
    print()


#PERCORRER ELEMENTOS A ELEMENTOS DA MATRIZ
for linha_1 in matriz:
    for elemento in linha_1:
        print(elemento, end=' ')
    print()