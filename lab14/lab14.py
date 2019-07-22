#MC 102
#LAB 14
#Luiz Fernando Bueno Rosa - RA 221197

#Este algoritmo tem a função de, dada uma entrada composta por RAs(números inteiros), realizar as operações de inserção, remoção, busca binária de RAs
#contidos na lista além da ordenação crescente e decrescente e impressão dos RAs a partir de comandos específicos de entrada. A saída é composta da
#impressão dos RAs na ordem inserido e/ou organizada, dos índices da busca binária e de mensagens de erro ou êxito.

def main():
    listaRA = input()#RAs de entrada
    listaRA = listaRA.split()#adiciona-os a uma lista

    for i in range(len(listaRA)):
        listaRA[i] = int(listaRA[i])


    s_press = False

    if listaRA == []:#Se a lista for vazia, ela não é nem decrescente ou crescente:
        crescente = False
        decrescente = False

    else:#Parâmetros verificadores de ordenação:
        crescente = True
        decrescente = True

        #Caso um número a frente de i seja maior que i, este não pode ser decrescente e vice versa para vetores crescentes.
        for i in range(len(listaRA)-1):
            if(listaRA[i] > listaRA[i+1]):
                crescente = False
            if(listaRA[i] < listaRA[i+1]):
                decrescente = False

    while s_press is False:

        comando = input()#O primeiro elemento de comando é a ordem, o segundo é o possível RA para manipulação da listaRA
        comando = comando.split()

        if comando[0] == 'p':#Comando de impressão, se listaRA é vazia ele passa:
            if listaRA == []:
                pass
            else:
                print(' '.join(str(v) for v in listaRA) + ' ')

        elif comando[0] == 'c':#Comando de ordenação crescente, se a lista é vazia ele passa:
            if listaRA == []:
                pass
            else:
                ordenaCrescente(listaRA)
                crescente = True
                decrescente = False

        elif comando[0] == 'd':#Comando de ordenação crescente, se a lista é vazia ele passa:
            if listaRA == []:
                pass
            else:
                ordenaDecrescente(listaRA)
                crescente = False
                decrescente = True

        elif comando[0] == 'i':#Comando de inserção de RAs, se a lista é vazia ele apenas insere sem verificaçõs.
            comando[1] = int(comando[1])#Caso contrário, há veificações da ordem do vetor e da posição onde o RA será inserido
            if listaRA == []:
                listaRA.append(comando[1])
            else:
                insereRA(listaRA, comando[1], crescente, decrescente)

        elif comando[0] == 'r':#Comando de remoção de RAs, caso não há o que remover, ele imprime um erro
            comando[1] = int(comando[1])
            removeRA(listaRA, comando[1])

        elif comando[0] == 'b':#Comando de busca binária:
            comando[1] = int(comando[1])
            boolean = True
            buscaBinaria(listaRA, comando[1], crescente, decrescente, boolean)

        elif comando[0] == 's':#Comando de finalização do processo:
            s_press = True


def insereRA(listaRA, RA, crescente, decrescente):
    crescente = True
    decrescente = True

    #Tem-se uma verificação da ordenação do vetor:
    for i in range(len(listaRA)-1):
        if(listaRA[i] > listaRA[i+1]):
            crescente = False
        if(listaRA[i] < listaRA[i+1]):
            decrescente = False

    if len(listaRA) >= 150:#Deve'se ter em mente que o máximo de alunos é 150
        print('Limite de vagas excedido!')
        return

    if crescente:#Se listaRA estiver ordenada de forma crescente:
        for j in range(len(listaRA)):#Verificar todos os elementos em listaRA
        #Se o RA a ser inserido é < que um elemento na posição j, então adicionamos o RA antes de j

            if RA == listaRA[j]:# Caso o eleento listaRA[j] seja o próprio RA, emitir a mensagem de erro:
                print("Aluno ja matriculado na turma!")
                return

            if RA < listaRA[j]:

                listaRA.insert(j, RA)
                return

        #Inserimos o RA no final da lista caso este seja maior que todos os outros elementos do vetor:
        listaRA.insert(len(listaRA), RA)
        return

    elif decrescente:#Se listaRA estiver ordenada de forma decrescente:
        for j in range(len(listaRA)):#Verificar todos os elementos em listaRA da esquerda para direita:
            #Caso algum elemento seja menor que o RA a ser inserido e não igual, inserimos o RA na lista:

            if RA == listaRA[j]:#Se RA está na lista, emitir mensagem de erro:
                print("Aluno ja matriculado na turma!")
                return

            if RA > listaRA[j]:

                listaRA.insert(j, RA)
                return
        #Inserimos o RA no final da lista caso este seja menor que todos os outros elementos do vetor:
        listaRA.insert(len(listaRA), RA)
        return

    else:#Se listaRA estiver desorganizada, verificar se o RA está na lista:
    #Se não o estiver, inserir o RA no final da lista:
        if not RA in listaRA:
            listaRA.append(RA)
        else:
            print("Aluno ja matriculado na turma!")

def removeRA(listaRA,RA):

    if listaRA == []:#Se a lista estiver vazia, imprimimos a mensagem de erro:
        print("Nao ha alunos cadastrados na turma!")

    elif RA in listaRA:#Se o RA existir dentro da lista:
        listaRA.remove(RA)

    else:#Se não atender a nenhuma condição, imprimir a mensagem de erro:
        print("Aluno nao matriculado na turma!")

def ordenaCrescente(listaRA): #Função que organiza listas em forma crescente

    for j in range(len(listaRA) - 1, 0,-1): #Comparamos listaRA[i] e listaRA[j]
        for i in range(0,j): #Comparamos os números da esquerda a direita até antes do nº listaRA[j]
            if listaRA[i] > listaRA[j]: #Se listaRA[j] é menor que listaRA[i] há uma troca de elementos
                listaRA[i], listaRA[j] = listaRA[j], listaRA[i]

def ordenaDecrescente(listaRA):#Função que organiza listas em forma decrescente

    for j in range(len(listaRA) - 1, 0, -1): #Comparamos listaRA[i] e listaRA[j]
        for i in range(0, j): #Comparamos os números da esquerda a direita até antes do nº listaRA[j]
            if listaRA[i] < listaRA[j]: #Se listaRA[j] é maior que listaRA[i] há uma troca de elementos
                listaRA[i], listaRA[j] = listaRA[j], listaRA[i]

def buscaBinaria(listaRA, ra_busca, crescente, decrescente, boolean):

    if crescente or decrescente:#Caso a função esteja ordenada:
        import math

        RA = ra_busca


        comeco = 0
        fim = len(listaRA) - 1
        meio = int(math.floor((comeco + fim)/2))#Eis o índice do meio da lista:

        lista_indices = []#Esta lista será usada para imprimir, em ordem, os índices do vetor listaRA percorridos durante a busca binária:
        lista_indices.append(meio)

        if listaRA[meio] == RA:#Caso o primeiro índice seja do RA procurado:
            print(meio + ' ')#Imprimir o índice de busca e a mensagem:
            print("%d esta na posicao: %d"%(RA, meio))
            return

        #Caso não obtemos o RA com a primeira busca, precisamos continuar a busca:
        while crescente is True and boolean is True:#Para vetores crescentes:

            if comeco > fim:#Se a busca chegou a um vetor com apenas um elemento sem encontrar o RA, assume-se que o RA não está na lista:
                print(' '.join(str(v) for v in lista_indices) + ' ')#Imprime-se os índices de busca e a mensagem de erro:
                print('%d nao esta na lista!'%RA)
                return

            if RA == listaRA[meio]:#Caso o índice seja do RA procurado:
                #Imprimir o índice de busca e a mensagem de êxito:
                print(' '.join(str(v) for v in lista_indices) + ' ')
                print("%d esta na posicao: %d"%(RA, meio))
                return

            #Caso o RA não fora encontrado, verificados se o RA está antes ou depois do índice de busca atual(meio):
            #Se o RA está antes do índice, obtemos uma lista definida pelo começo até o meio da passada:
            if RA < listaRA[meio]:#Excluimos o meio de ambas novas listas para otimizar a busca:
                fim = meio - 1
            else:#Se o RA está depois do índice, obtemos uma lista com o começo de meio da lista anterior +1:
                comeco = meio + 1

            meio = int(math.floor((comeco + fim)/2))#Obtemos um novo índice

            if comeco <= fim: #Enquanto a busca não termina, acrescentar um índice a lsita de índices
                lista_indices.append(meio)

        #Para listas ordenadas dercrescentemente, aplicamos o mesmo processo das listas crescentes, mas com uma diferença:
        #Devemos lembrar que se o RA é menor que o elemento do índice de busca, o primeiro se encontra a frente do segundo, oposto ao que ocorre em listas crescentes:
        #Assim, se o RA é menor que o elemento do índice de busca, o primeira está antes do segundo:
        while crescente is False and boolean is True:
            if comeco > fim:
                print(' '.join(str(v) for v in lista_indices) + ' ')
                print('%d nao esta na lista!'%RA)
                return

            if RA == listaRA[meio]:
                print(' '.join(str(v) for v in lista_indices) + ' ')
                print("%d esta na posicao: %d"%(RA, meio))
                return

            if RA > listaRA[meio]:
                fim = meio - 1
            else:
                comeco = meio + 1

            meio = int(math.floor((comeco + fim)/2))

            if comeco <= fim:
                lista_indices.append(meio)

    else:#Caso o vetor não esteja ordenado, imprimir a seguinte mensagem de erro:
        print("Vetor nao ordenado!")

main()
