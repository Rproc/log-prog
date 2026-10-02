matriz = [
    [6, 7, 2],
    [1, 5, 9],
    [8, 3, 4]
]

soma_linhas = []
soma_colunas = []
soma_diag = 0
soma_diag2 = 0
somas = []
for i in range(3):
    soma_linha = 0
    soma_coluna = 0
    for j in range(3):
        soma_linha += matriz[i][j] # soma elementos de cada linha
        soma_coluna += matriz[j][i]
    soma_diag1 += matriz[i][i]
    soma_diag2 += matriz[i][2-i]
    somas.append(soma_linha)
    somas.append(soma_coluna)


