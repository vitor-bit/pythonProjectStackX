# Algoritmo 2. Estruturas condicionais e de repetição: Tabuada com entrada do usuário (FOR)
# Dev: Vitor Bitencourt
# Data: 27/06/2022

Numero = int(input("Digite um número: "))
Tabuada = 0
for i in range(Tabuada, 11):
	Multiplicacao = Numero * i
	print(Numero, "*", i, "=", Multiplicacao)
	i += 1
