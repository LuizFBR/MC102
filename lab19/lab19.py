#LAB 19
#Luiz Fernando Bueno Rosa - RA 221197

#Este algoritmo busca analisar a hierarquia de um funcionario de uma empresa, de modo que cada funcionario seja representado por um número(linha da matriz
# de entrada). Assim, analisamos até o subordinado que não possui subordinados e imprimimos uma string dessa hierarquia.
import random
import re
saida = []
#Obtemos a ordem da matriz e o número do funcionario
(ordem_m, funcionario) = map(int, input().split())
#Criamos uma matriz a partir da string dada
matriz = [ [int(i) for i in re.findall(r'[0-9]+', input())] for a in range(ordem_m)]

contador = 0
#aqui usamos um MergeSort para organizar a lista de saida:
# def mergeSort(v, ini, fim, aux):
#     meio = (fim+ini) // 2
#     if(ini < fim):
#
#         mergeSort(v, ini, meio, aux)
#         mergeSort(v, meio + 1, fim, aux)
#         merge(v, ini, meio ,fim , aux)
#
# def merge(v, ini, meio, fim, aux):
#     g = ini; h = meio +1; k = 0;
#
#     while(g <= meio and h <= fim):
#
#         if(v[g] <= v[h]):
#             aux[k] = v[g]
#             k += 1
#             g += 1
#         else:
#             aux[k] = v[h]
#             k += 1
#             h += 1
#
#         while(g <= meio):
#             aux[k] = v[g]
#             k += 1
#             g += 1
#
#         while (h <= fim):
#             aux[k] = v[h]
#             k += 1
#             h += 1
#
#         g = ini; k = 0;
#         while( g <= fim):
#             v[g] = aux[k]
#             g += 1
#             k += 1

def randomQuickSort(v, ini, fim):
    if(ini < fim):
        j = random.randint(ini, fim)
        v[j], v[fim] = v[fim], v[j]
        pos = particiona(v, ini, fim)
        randomQuickSort(v, ini, pos - 1)
        randomQuickSort(v, pos, fim)

def particiona(v, ini, fim):
    pivo = v[fim]
    while(ini < fim):

        while (ini < fim) and (v[ini] <= pivo):
            ini += 1

        while (ini < fim) and (v[fim] > pivo):
            fim -= 1

        v[ini], v[fim] = v[fim], v[ini]
    return ini


def Hierarquia(funcionario, saida, contador):#Função que determina a hierarquia de um funcionario

    if not 1 in matriz[funcionario]:#Caso básico; se o funcionario não possui subordinados, a função se encerra;
        return funcionario

    else:#Caso contrário, adicionamos cada subordinado à lista de subordinados;
        for i in range(len(matriz[funcionario])):
            if (matriz[funcionario][i] == 1): #and (i not in saida) - A pat falou para eu deixar esses corretores fora dos laços.
                saida.append(i)


        for i in range(0 + contador, len(saida)):#percorremos a lista de subordinados e verificamos e identificamos a hierarquia desses, se houver algum;
            contador += 1
            funcionario = saida[i]
            Hierarquia(funcionario, saida, contador)

    return saida

# aux = copy.deepcopy(saida)
#imprimimos a saida
saida = Hierarquia(funcionario, saida, contador)

if type(saida) != int:
    saida = list(set(saida))# deixei aq, tá feliz agora pat?
    randomQuickSort(saida, 0, len(saida)-1) #mergeSort(saida, 0+ contador, len(saida) - 1, aux)
    print(funcionario, end =' ')
    for i in saida:
        if i != saida[len(saida) - 1]:
            print(i, end = ' ')
        else:
            print(i)
else:
    print(saida)

#
# def Hierarquia(funcionario):
#     if not 1 in matriz[funcionario]:
#         return funcionario
#
#     else:
#         saida.append(int(i) for i in re.findall(r'[1]', matriz[funcionario]))
#
#     for i in matriz[funcionario]:
#         if i == 1:
#             saida.append(matriz[funcionario].index(i))
#     saida.append(Hierarquia(funcionario))

#     return saida
#     if not 1 in matriz[funcionario]:
#         return funcionario
#     else:
#         for i in matriz[funcionario]:
#             if i == 1:
#
#
#
# print(Hierarquia(funcionario))
