#Luiz Fernando Bueno Rosa - RA 221197

#Este algoritimo lê a entrada de duas matrizes, os números de linhas e colunas de cada, referentes a 2 jogadores
#após isso, a partir de entradas de coordenadas das matrizes dos jogadores 1 e 2, alternadamente, se uma coorde-
#nada coincidir com a posição da parte de um navio(@) de uma coordenada, esse navio é destruido, sendo substituido por
# "-"s. O primeiro jogador que ter seus navios destruidos acarretará  no fim do programa.

import re

turno = 0

mapa_vazio = False

(linhas, colunas) = re.findall(r'[0-9]+', input())
(linhas, colunas) = int(linhas), int(colunas)

quadro_navios = {}

matrizJ1 = [[i for i in input()] for a in range(linhas)]
# for i in range(linhas):
#     for a in range(colunas):
#         if a != (colunas - 1):
#             print(matrizJ1[i][a], end = " ")
#         else:
#             print(matrizJ1[i][a])
matrizJ2 = [[i for i in input()] for a in range(linhas)]
# for i in range(linhas):
#     for a in range(colunas):
#         if a != (colunas - 1):
#             print(matrizJ2[i][a], end = " ")
#         else:
#             print(matrizJ2[i][a])
# def cadencia(matriz, linhas, colunas, quadro_navios):
#     for a in range(linhas):
#         for b in range(colunas):
#
#             if matriz[a][b] == "@":
#
#                 if (quadro_navios != []):
#                     for i in range(len(quadro_navios)):
#                         for j in quadro_navios[i]:
#                             print(j)
#                             (k,x) = j
#
#                             if (a,b) == (k, x + 1):
#                                 quadro_navios[i].append((a,b))
#                                 i = len(quadro_navios) - 1
#                                 j = quadro_navios[i]
#
#                             elif (a,b) == (k + 1, x):
#                                 quadro_navios[i].append((a,b))
#
#                 else:
#                     quadro_navios["navio_1"] = (a,b)
#                     print(quadro_navios)
#     return quadro_navios
#
# print(cadencia(matrizJ1, linhas, colunas, quadro_navios))

def bombardeia(mapa, lin, col):
    if (lin < 0 or lin >= len(mapa)
        or col < 0 or col >= len(mapa[lin])
        or mapa[lin][col] != '@'):
            return

    mapa[lin][col] = '-'
    bombardeia(mapa, lin-1, col)
    bombardeia(mapa, lin+1, col)
    bombardeia(mapa, lin, col-1)
    bombardeia(mapa, lin, col+1)

def mapa_vazio(mapa):
    for lin in mapa:
        for x in lin:
            if x == "@":
                return False
    return True

while not mapa_vazio(matrizJ1) and not mapa_vazio(matrizJ2):

    (linha, coluna) = re.findall(r'[0-9]+', input())
    (linha, coluna) = int(linha), int(coluna)

    jogadorX = 0
    matrizJX = [[]]

    if turno % 2 == 0:
        matrizJX = matrizJ2
        jogadorX = 1

    else:
        matrizJX = matrizJ1
        jogadorX = 2

    print("Ataque em ({},{}) do jogador {}".format(linha, coluna, jogadorX))

    bombardeia(matrizJX, linha - 1, coluna - 1)
    for i in range(len(matrizJX)):
        for j in range(len(matrizJX[i])):
            print(matrizJX[i][j], end='')
        print()

    turno += 1
