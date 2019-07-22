#MC 102 - Lab15
#Luiz Fernando Bueno Rosa - RA 221197

# Funcao: pertence
#
# Parametros:
#   conj: vetor contendo o conjunto de entrada
#    num: elemento a ser verificado pertinencia
#
# Retorno:
#   True se num pertence a conj e False caso contrario
#
def pertence(conj, num):
    #Ler todos os elementos na lista conj:
    for i in range(len(conj)):
        if conj[i] == num:#Se o um elemento for igual a num a pertinÊncia é verdadeira:
            return True
    #Caso contrário:
    return False

# Funcao: contido
#
# Parametros:
#   conj1: vetor contendo um conjunto de entrada
#   conj2: vetor contendo um conjunto de entrada
#
# Retorno:
#   True se conj1 esta contido em conj2 e False caso contrario
#
def contido(conj1, conj2):
    soma = 0
    if conj1 == []:
        return True

    for i in conj1:
        if i in conj2:
            #Contamos o número de elementos na lista conj1 e verificamos se o número de elementos em conj1 é igual ao número de elementos que pertencem Às duas listas:
            soma += 1
        #Se sim:
        if soma == len(conj1):
            return True
    #Se não:
    return False

# Funcoes: adicao e subtracao
#
# Parametros:
#   conj: vetor contendo o conjunto que tera incluso ou removido o elemento
#    num: elemento a ser adicionado ou removido
#
def adicao(conj, num):
    #Se num não está na lista, adicionar:
    if not num in conj:
        conj.append(num)
    #Caso contrario, encerrar e não executar nada:


def subtracao(conj, num):
    #Se num está na lista, encerrar e não executar nada:
    if num in conj:
        conj.remove(num)
    #Caso contrário, retirar número da lista



# Funcoes: uniao, intersecao e diferenca
#
# Parametros:
#     conj1: vetor contendo o conjunto de entrada do primeiro operando
#     conj2: vetor contendo o conjunto de entrada do segundo operando
#
# Retorno:
#   Vetor contendo o conjunto de saida/resultado da operacao
#
def uniao(conj1, conj2):
    conjfinal = []
    #Copiamos um dos conjuntos para o conjunto uniao:
    conjfinal = conjfinal + conj1

    for i in conj2:#Adicionamos cada elemento que não há no conj1 e há no conj 2 para o conj final
        if not i in conj1:
            conjfinal.append(i)
    #Retornamos o conjunto união:
    return conjfinal

def intersecao(conj1, conj2):
    conjfinal = []
    for i in conj2:#Adicionamos cada elemento que há nos dois conjs para o conj final
        if i in conj1:
            conjfinal.append(i)
    #Retornamos o conjunto união:
    return conjfinal

def diferenca(conj1, conj2):
    conjfinal = []
    #Copiamos um dos conjuntos para o conjunto uniao:
    conjfinal = conjfinal + conj1

    for i in conj1:#subtraimos cada elemento que pertence aos dois conjs simultaneamente do conjfinal:
        if (i in conj1) and (i in conj2):
            conjfinal.remove(i)

    #Retornamos o conjunto diferenca:
    return conjfinal

def uniao_disjunta(conj1, conj2):
    conj_u_disj = []
    conjX = []
    #Copiamos um dos conjuntos para o conjunto x:
    conjX = conjX + conj1

    for i in conj1:#subtraimos cada elemento que pertence simultaneante aos dois conjs do conjX:
        if i in conj1 and i in conj2:
            conjX.remove(i)

    conjY = []
    #Copiamos um dos conjuntos para o conjunto uniao:
    conjY = conjY + conj2

    for i in conj2:#subtraimos cada elemento que pertence simultaneamente aos dois conjs do conjY:
        if i in conj1 and i in conj2:
            conjY.remove(i)

    for i in conjX:#Adicionamos cada elemento que pertence no conjx e não pertence no conj y para o conj_u_disj
        if not i in conjY:
            conj_u_disj.append(i)

    for i in conjY:#Adicionamos cada elemento que pertence no conjy e não pertence no conjx para o conj_u_disj
        if not i in conjX:
            conj_u_disj.append(i)

    #Por fim retornamos o conjunto união disjunta
    return conj_u_disj
