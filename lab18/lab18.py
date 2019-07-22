#LAB 18
#Luiz Fernando Bueno Rosa - RA 221197

#A partir de uma imagem(matriz) de entrada e um filtro(matriz de convolução) de entrada, alteramos o aspecto da imagem
#a partir da operação de convolução e imprimimos a imagem(matriz) de saida.

import sys
import re
import copy
#Abrimos o arquivo de entrada 1:
imagem = open(sys.argv[1], 'r')
matriz = list(imagem)
imagem.close

#Obtemos a ordem da matriz:
(n_colunas, n_linhas) = re.findall(r'[0-9]+', matriz[1])
(n_linhas, n_colunas) = (int(n_linhas), int(n_colunas))

#Constroi-se a matriz:
matriz = [ [int(i) for i in re.findall(r'-?[0-9]+', matriz[3+a])] for a in range(n_linhas)]
#Obtemos uma matriz de saida:
matriz_saida = copy.deepcopy(matriz)
#Agora, abrimos o segundo arquivo:
matriz2 = open(sys.argv[2], 'r')
matriz_convolucao = list(matriz2)
matriz2.close
#Obtemos o divisor
Divisor = matriz_convolucao[0]
#Obtemos a matriz_filtro:
matriz_convolucao = [ [int(i) for i in re.findall(r'-?[0-9]+', matriz_convolucao[1+a])] for a in range(3)]

#Retiramos os números exteriores à matriz:
for i in range(1, n_linhas -1):
    for j in range(1, n_colunas -1):

        x = i
        y = j

        soma = 0
        lista_volta = []
        lista_bonita = []

        #Ordenamos a submatriz em volta do elemento a sofrer convolução em uma lista;
        for a in range(i - 1, i + 2):
            for b in range(j - 1, j + 2):
                lista_volta.append(matriz[a][b])

        #Ao passo que a matriz_convolução, ordenada como lista, compartilhe o indice a ser multiplicado com o indice da submatriz:
        for c in range(3):
            for d in matriz_convolucao[c]:
                lista_bonita.append(d)

        #Assim, obtemos a soma das multiplicações dos termos ao redor;
        for c in range(9):
            soma += lista_volta[c]*lista_bonita[c]

        #E obtemos o elemento final:
        matriz_saida[x][y] = (int(soma)//int(Divisor))

        #Truncamos:
        if matriz_saida[x][y] > 255:
            matriz_saida[x][y] = 255
        elif matriz_saida[x][y] < 0:
            matriz_saida[x][y] = 0

#E obtemos a saída:
print("P2")
print(n_colunas,n_linhas)
print(255)
for x in range(len(matriz_saida)):
    for y in range(len(matriz_saida[x])):
        print(matriz_saida[x][y], end = " ")
    print(' ')
