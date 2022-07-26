# Algoritmo 13. Altura e sexo (IF)
# Dev: Vitor Bitencourt
# Data: 18/06/2022

Altura = float(input("Digite sua altura: "))
Sexo = int(input("Sendo 1: feminino e 2: masculino, Digite seu sexo: "))

if Sexo == 1:
    PesoIdeal = (62.1 * Altura) - 44.7
    print("Seu peso ideal é de", PesoIdeal, "kg")
else:
    PesoIdeal = (72.7 * Altura) - 58
    print("Seu peso ideal é de", PesoIdeal, "kg")
