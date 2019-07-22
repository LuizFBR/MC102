# Luiz Fernando Bueno Rosa - RA 221197

# Este algoritmo analisa as mudanças em uma matriz de entrada (i,j) de acordo com a entrada de iterações, e imprime uma saida de acordo com as interações de uma casa da matriz com seus arredores, gerando uma matriz de mesma ordem mas possivelmente com elementos diferentes.

def main():

    line_column_str = input() #Aqui entra a ordem da matriz

    #Aqui separa-se os valores da ordem em variáveis:
    line_column = line_column_str.split()
    n_list = int(line_column[0])
    list_size = int(line_column[1])

    state = int(input())#Aqui a entrada de iterações(dias) é feita

    #Aqui cria-se a matriz a partir da entrada "linha"
    matrix_pos = [[] for i in range(n_list)]

    for i in range(n_list):

        linha = input()
        matrix_pos[i] = [int(a) for a in linha.split()]

    #Aqui adiciona-se duas linhas zero no começo e no final da matriz
    list1_0 = [0 for p in range(list_size+2)]
    matrix_pos.insert(0,list1_0)
    list2_0 = [0 for p in range(list_size+2)]
    matrix_pos.append(list2_0)

    #Aqui adiciona-se elementos zero no começo e no final de cada linha da matriz original
    for r in range(1, n_list + 1):
        matrix_pos[r].insert(0,0)
        matrix_pos[r].append(0)

    #Aqui encontra-se o laço de analise dos arredores de um elemento e modificação deste
    for day in range(state):

        #Imprime-se a primeira iteração
        print("iteracao " + str(day))
        print_map(matrix_pos)

        #Chama a função update_day
        matrix_pos = update_day(matrix_pos)


    #Imprime-se a última iteração
    print("iteracao " + str(state))
    print_map(matrix_pos)

def circumstance_check(map, lin, col):
    n_zombie = 0
    n_human = 0
    #Escolhe o local de análise, os arredores do elementos
    for i in range(lin - 1, lin + 2):
        for j in range(col - 1, col + 2):
            #Aqui se verifica o número de zumbis e humanos ao redor do elemento em análise
            if not (i == lin and j == col):
                if map[i][j] == 1:
                    n_human += 1
                elif map[i][j] == 2:
                    n_zombie += 1

    #Condições de mudança:
    if map[lin][col] == 0 and n_human == 2:
        return 1

    if map[lin][col] == 1 and n_zombie >= 1:
        return 2

    if map[lin][col] == 2 and n_human == 0:
        return 0

    if map[lin][col] == 2 and n_human >= 2:
        return 0

    return map[lin][col]


def update_day(map): # Essa função é utilizada para criar uma matriz a qual será passada as modificações e escolher os elementos à análise

    matrix_pos = [[0 for n in range(len(map[m]))] for m in range(len(map))]


    for i in range(1, len(map) - 1):
        for j in range(1, len(map[i]) - 1):
            #Atualiza-se os elementos a partir da análise feita na função circumstance_check
            matrix_pos[i][j] = circumstance_check(map, i, j)

    return matrix_pos

#Aqui se imprime cada elemento excluindo os zeros
def print_map(map):
    for i in range(1,len(map)-1):
        for j in range(1,len(map[i])-1):
            print(map[i][j], end='')
        print()

main()
