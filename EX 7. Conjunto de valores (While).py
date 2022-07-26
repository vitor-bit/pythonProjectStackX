# Algoritmo 7. Conjunto de valores (While)
# Dev: Vitor Bitencourt
# Data 17/06/2022

# Faça um programa que leia um conjunto não determinado de valores e mostre o valor
# lido, seu quadrado, seu cubo e sua raiz quadrada. Finalize a entrada de dados com
# um valor negativo ou zero.

import math
ConjuntoValor = 1
Resposta = "Sim"
while Resposta == "Sim":
    print("Conjunto de valores:", ConjuntoValor)
    Valor = int(input("Digite um valor: "))
    Quadrado = pow(Valor, 2)
    Cubo = pow(Valor, 3)
    Raiz = math.sqrt(Valor)
    ConjuntoValor += 1
    print("Valor lido:", Valor, "Quadrado:", Quadrado, "Cubo:", Cubo, "Raiz quadrada:", Raiz)
    Resposta = input("Deseja continuar ? ")
    continue
print("Conjunto de valor final")
Valor0 = 0
Quadrado = pow(Valor0, 2)
Cubo = pow(Valor0, 3)
Raiz = math.sqrt(Valor0)
print("Valor lido:", Valor0, "Quadrado:", Quadrado, "Cubo:", Cubo, "Raiz quadrada:", Raiz)