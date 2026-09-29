# Construa uma matriz 2X2 e, como saída desse programa, 
# a média e a soma dos valores digitados deverão ser calculadas.


# -----------------------------------------
# instanciar matrizes com 0 (zero)
linhas = 2
colunas = 2
matriz = [[0] * colunas for _ in range(linhas)]

# for linha in range(linhas):
#     matriz[linha] = colunas * [0] # -> [0, 0]
    # remontando
    # l1 = [0, 0]
    # l2 = [0, 0]
    # reescrevendo
    # matriz = [
    #               [0, 0],
    #               [0, 0]
    #           ]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = int(input('Digite um número: '))
# -----------------------------------------

matriz = []
for i in range(2): # linha
    lista = [] # elementos da linha
    for j in range(2): # para cada elemento
        lista.append(int(input('Digite um número: ')))
    matriz.append(lista) # quando acabar de ler a linha
    # guarda na matriz

# for linha in matriz:
#     for coluna in linha:
#         soma += coluna
contador = 0
for linha in range(len(matriz)): # quantas linhas tem
    for coluna in range(len(matriz[linha])): # quantas colunas tem
        soma += matriz[linha][coluna]
        contador += 1

media = soma/contador

