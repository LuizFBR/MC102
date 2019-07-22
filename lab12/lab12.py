#MC102
#Lab 12
#Luiz Fernando Bueno Rosa - RA 221197

def atualiza_posicao(l, a, x, desl, rot):
    #Se o bloco rotaciona, sua largura troca com sua altura
    if rot == 1:

        salva_l = l
        l = a
        a = salva_l

    #os pontos de referência da largura e da posição diferem, havendo 1 de diferença entre esses:
    if (x + desl + l) > 10:#portanto, a soma do deslocamento, da posição inicial e da largura não ultrapassam a largura da matriz
        x = 10 - l #caso contrário, a distância mínima do máximo da matriz ao ponto de referência do bloco é a diferença entre esses.
    elif (x + desl) < 0: # O mínimo de x é 0
        x = 0
    else:
        x = x + desl

    return l, a, x


def encontra_y(mat, l, x):
    #Percorrendo de x a (x+l-1), encontramos apenas elementos nas mesmas colunas que o bloco.
    achou = False
    for i in range(10):
        for j in range(x, x + l):
            #Ao encontrar um elemento preenchido:
            if mat[i][j] == 1:# todos os elementos nas colunas serão verificados
                save_y = i + 1 #assume-se que na linha acima deverá se posicionar o bloco atual
                achou = True

    if achou is False:# Se não houver algum elemento preenchido, a altura é mínima:
        return 0
    return save_y

def posicao_final_valida(a, y):
    if (a + y) > 10:#A posição só é válida se a altura do bloco não ultrapassar a matriz:
        return 0

    return 1

def posiciona_bloco(mat, l, a, x, y):
    #Utilizando a posição do bloco em altura e em largura  como referências;
    for k in range(y, a + y):
        #Atualiza-se a matriz
        mat[k] = [1 if i in range(x, x + l) else mat[k][i] for i in range(10)]


def atualiza_matriz(mat):

    primeira_vez = False
    cont_linhas_preenchidas = 0
    #Verifica-se se todos os elementos de uma linha são 1. Se sim, troca os elementos por 0.
    for i in range(10):
        cont_1s = 0
        for j in range(len(mat[i])):

            if mat[i][j] == 1:#Para isso, usa-se um contador de 1s por linha
                cont_1s += 1

            if cont_1s == 10:

                if primeira_vez is False:
                    #Salva-se a posição da primeira linha de 1s no eixo y para depois atualizar a matriz:
                    save_i = i

                mat[i] = [0 for k in range(10)]
                cont_linhas_preenchidas += 1 #Atualiza-se os pontos
                primeira_vez = True

    #Abaixar blocos
    if cont_linhas_preenchidas > 0:# Se houve alguma linha modificada
        primeira_vez = False#D
        distancia = 0
        for k in range(save_i, 10):
            for j in range(10):

                if mat[k][j] == 1 and primeira_vez is False:

                    primeira_vez = True # o índice da primeira linha "apagada" é usado como referência
                    mat[save_i] = [mat[k][i] for i in range(10)]# Assim, a linha que possui um elemento mais próxima da linha apagada a substitui:
                    mat[k] = [0 for i in range(10)]# A linha se torna nula
                    save_k = k# E salva-se a antiga posição da linha alterada para referenciar as linhas acima desta.
                    j = 9#Não há necessidade de verificar além disso, visto que já sabemos que essa linha possui algum 1.

                if mat[k][j] == 1 and primeira_vez is True:

                    distancia = k - save_k# Usaremos a verificação acima de referência
                    #a distância determina onde cada linha se posicionará após as modificações:
                    mat[save_i + distancia] = [mat[k][i] for i in range(10)]
                    #E atualiza-se a linha modificada para uma linha 0
                    mat[k] = [0 for i in range(10)]
                    j = 9

    return cont_linhas_preenchidas
