#Luiz Fernado Bueno Rosa - RA 221197
#MC 102
#Lab 13


# Funcao: atualizaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato
#   jogo: string contendo as informações de um jogo no formato especificado no lab.
#
# Descrição:
#   Deve inserir as informações do parametro 'jogo' na tabela.
#   OBSERVAÇÃO: nesse momento não é necessário ordenar a tabela, apenas inserir as informações.
def atualizaTabela(tabela, jogo):
    #Retira-se os dados das listas:
    split = jogo.split()
    nome1 = split[0]
    nome2 = split[4]
    gol1 = int(split[1])
    gol2 = int(split[3])

    linha1 = 0
    linha2 = 0

    #Aqui se acha o índice dos nomes dos times
    for i in range(len(tabela))  :
        for j in range(1):
            if tabela[i][j] == nome1:
                linha1 = i
            if tabela[i][j] == nome2:
                linha2 = i

    #Faz-se a comparação de vitória e atualizza-se a tabela:
    if gol1 > gol2:#Se time 1 ganhar:
        saldo = gol1 - gol2
        tabela[linha1][1] = 3 + int(tabela[linha1][1])
        tabela[linha1][2] = 1 + int(tabela[linha1][2])
        tabela[linha1][3] = int(tabela[linha1][3]) + saldo
        tabela[linha2][3] = int(tabela[linha2][3]) - saldo

    elif gol1 < gol2:#Se time 2 ganhar
        saldo = gol2 - gol1
        tabela[linha2][1] = 3 + int(tabela[linha2][1])
        tabela[linha2][2] = 1 + int(tabela[linha2][2])
        tabela[linha1][3] = int(tabela[linha1][3]) - saldo
        tabela[linha2][3] = int(tabela[linha2][3]) + saldo

    else:#Empate:
        tabela[linha1][1] = 1 + int(tabela[linha1][1])
        tabela[linha2][1] = 1 + int(tabela[linha2][1])
    #O número de gols independe do resultado
    tabela[linha1][4] = gol1 + tabela[linha1][4]
    tabela[linha2][4] = gol2 + tabela[linha2][4]

#*******************************************************************************
# Funcao: comparaTimes
#
# Parametros:
#   time1: informações de um time
#   time2: informações de um time
#
# Descricão:
#   retorna 1, se o time1>time2, retorna -1, se time1<time2, e retorna 0, se time1=time2
#   Observe que time1>time2=true significa que o time1 deve estar em uma posição melhor do que o time2 na tabela.
def comparaTimes(time1, time2):

    #Estabelece as condições de vitória em ordem de importância de nº de pontos, nº de vitórias, nº do saldo e nº de gols
    #Compara-se os times:
    if int(time1[1]) > int(time2[1]):
        return 1
    elif int(time1[1]) < int(time2[1]):
        return -1
    else:
        if int(time1[2]) > int(time2[2]):
            return 1
        elif int(time1[2]) < int(time2[2]):
            return -1
        else:
            if int(time1[3]) > int(time2[3]):
                return 1
            elif int(time1[3]) < int(time2[3]):
                return -1
            else:
                if int(time1[4]) > int(time2[4]):
                    return 1
                elif int(time1[4]) < int(time2[4]):
                    return -1
                else:
                    return 0
#*******************************************************************************
# Funcao: ordenaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descricão:
#   Deve ordenar a tabela com campeonato de acordo com as especificaçoes do lab.
#
def ordenaTabela(tabela):
    #Aqui há o ranqueamento dos times:
    for i in range(len(tabela) - 1, -1, -1):#Usando um bubble sort, ordena-se o ranqueamento;
        for j in range(i):
            what = comparaTimes(tabela[j+1],tabela[j])#Busca a função de comparação.
            if what == 1:#Se o retorno de comparaTimes é 1, o time1 vence, e trocam-se as posições.
                (tabela[j],tabela[j+1]) = (tabela[j+1], tabela[j])


#*******************************************************************************
# Funcao: imprimeTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descrição:
#   Deve imprimir a tabela do campeonato de acordo com as especificações do lab.
def imprimeTabela(tabela):
    for i in range(len(tabela)):
        for j in range(5):
            tabela[i][j] = str(tabela[i][j])
        tabela[i] = ", ".join(tabela[i])
        print(tabela[i])
