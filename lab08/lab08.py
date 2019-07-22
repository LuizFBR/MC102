#Luiz Fernando Bueno Rosa - RA 221197

#Este algoritmo visa o cálculo do poder final de pokemons após a evolução destes a partir do cálculo de multiplicadores de poder, usando uma data base de monstros da mesma especie, a partir de entradas do id da especie, do poder inicial e final do indivíduo da especie. O multiplicador seraá por espécie e será a média de multiplicadores de individuos da mesma especieself.
#Após, a partir de novas entradas de id já existente e de poder inicial, o poder final será calculado a partir dos multiplicadores da especie, enquanto a entrada 0 0 é o comando de parada.

atuais = [-1,-1]
soma_medias = []
lista_especies = []
denominador_medias = []
medias_multiplicador = []
ezero = False
import math

organismos = int(input())

#Mais de 1000000000 entradas de pokemons na database não serão lidas
if organismos <= 1000000000:
    for i in range(1, organismos + 1):
        repetida = False
        #O numero de especies é limitado pela lista_especies
        if len(lista_especies) <= 151:

            #Entrada de individuos da data base
            linha = input()
            ints = [int(j) for j in linha.split()]
            multiplicadora = (ints[2]/ints[1])

            #Ver especies repetidas:
            if ints[0] in lista_especies:

                repetida = True

                #Adicionar multiplicadores e denominadores das médias às listas:
                indice = lista_especies.index(ints[0])
                soma_medias[indice] += multiplicadora
                denominador_medias[indice] += 1

            #Adicionar espécie novas, multiplicadores e denominadores das médias às listas:
            if repetida is False:

                lista_especies.append(ints[0])
                soma_medias.append(multiplicadora)
                denominador_medias.append(1)

            #Resetando
            indice = 0
            multiplicadora = 0

    #Calculando a média de cada especie e adicionando-a a uma lista
    for i in range(len(lista_especies)):
        medias_multiplicador.append(soma_medias[i]/denominador_medias[i])

    #Nova entradas e respectivos cálculos de poderes finais.
    while ezero is False:

        linha = input()
        atuais = [int(j) for j in linha.split()]


        if atuais[0] == 0 and atuais[1] == 0:
            ezero = True

        else:
            resgatar = lista_especies.index(atuais[0])
            poder_final = medias_multiplicador[resgatar]*atuais[1]
            #Aqui se arredonda os números para o teto.
            print(math.ceil(poder_final))
