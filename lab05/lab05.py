#Luiz Fernando Bueno Rosa - RA 221197

#Este algoritmo busca, a partir de variáveis de entrada de dano, calcular a vida de dois jogadores num jogo de luta, de acordo com o sinal. Um dano positivo reduz a vida do jogador 2 e um negativo reduz a vida do jogador 1. Assim, imprime-se a operação de redução da vida atual do jogador a partir da soma da sequência de danos de mesmo sinal. O algoritmo também determina os ganhadores de 2 rounds e, ao final do programa, imprime o ganhador, caso não houver empate, o qual também será imprimido.

#Damos valores às variaveis:
vidaRyu = 50
vidaKen = 50

#As variáveis de verificação de números triangulares e perfeitos são denominadas
somaP = 0
somaT = 0

ganharyu = 0
ganhaken = 0

soma = 0

#Estabelecemos as condições de vitoria
while ganhaken != 2 or ganharyu != 2 or not (ganhaken == 1 and ganharyu == 1):
	#Denomina-se a variável de entrada
	dano = int(input())

	#Se dano é 0, não interessa o fato de ele ser triangular ou perfeito, pois 0 multiplicado por qualquer número é igual a zero.
	if dano != 0:
		#Verificação de dano, caso seja triangular e/ou perfeito:
		for i in range(1,abs(dano)+1):
			#Atendemos os requerimentos para dano ser um número perfeito:
	        if abs(dano) % i == 0 and abs(dano) / i != 1:
	            somaP += i
			#Se a soma de 1 até um número qualquer for igual a dano, isso quer dizer que dano se trata de um número triangular:
	        somaT += i
	        if somaT == abs(dano):
				#valores triangulares são multiplicados por dois
	            dano = dano*2
	    if somaP == abs(dano):
	        #Caso dano seja triangular e perfeito ou apenas perfeito, dano deverá ser multiplicado por três:
			if somaT == abs(dano):
				dano = dano/2
				dano = dano*3
			else:
				dano*3
	#Danos positivos diminuem a vida de Ken, negativos diminuem a vida de Ryu
	if dano > 0:
		vidaKen -= dano
	else:
		vidaRyu += dano

	#Verifica-se se a variável dano não trocou de sinal
	if (soma*dano) >= 0: # golpe na mesma sequencia
		soma += dano
	else: # houve troca de sinal
		#printa-se o dano da variavel soma, de acordo com o sinal:
		if dano > 0:
			print("Ryu: {} - {} = {}".format((vidaRyu - soma), abs(soma), vidaRyu))
		elif dano < 0:
			print("Ken: {} - {} = {}".format((vidaKen + soma), soma, vidaKen))
		#atualiza a variável soma
		soma = dano
	#caso o round acabar, printa-se o dano da variavel, dependendo de qual jogador tenha perdido.
	if vidaRyu <= 0:
		print("Ryu: {} - {} = {}".format((vidaRyu - soma), abs(soma), vidaRyu))
	if vidaKen <= 0:
		print("Ken: {} - {} = {}".format((vidaKen + soma), soma, vidaKen))

	#Atualiza-se as variaveis de vitoria e reseta-se o round, caso ainda seja o primeiro round:
	if ganhaken != 1 or ganharyu != 1:

		if vidaKen <= 0:

			ganharyu = ganharyu + 1
			soma = 0
			vidaKen = 50
			vidaRyu = 50

		if vidaRyu <= 0:

			ganhaken = ganhaken + 1
			soma = 0
			vidaKen = 50
			vidaRyu = 50

	#Caso seja o round 2, não há a necessidade de resetar o round, apenas de atualizar o estado dos rounds.
	elif ganhaken == 1 or ganharyu == 1:

		if vidaKen <= 0:
			ganharyu += 1

		if vidaRyu <= 0:
			ganhaken += 1

	#Para que o programa prossiga, após os dois rounds, esse laço necessita de ser terminado.
	if ganhaken == 2 or ganharyu == 2 or (ganhaken == 1 and ganharyu == 1):
		break

#Aqui se imprimem as condições de vitória:
if ganhaken == 2:
	print ("Ken venceu")

if ganharyu == 2:
	print ("Ryu venceu")

if ganharyu == 1 and ganhaken == 1:
	print ("empatou")
