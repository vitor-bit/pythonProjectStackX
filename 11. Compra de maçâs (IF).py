# Algoritmo 11. Compra de maçâs (IF)
# Dev: Vitor Bitencourt
# Data: 18/06/2022

Macas = int(input("Quantas maças deseja comprar? "))

if Macas < 12:
    Macas1 = Macas * 0.30
    print("Quantidade de maças:", Macas, "Valor total:", Macas1)
else:
    Macas1 = Macas * 0.25
    print("Quantidade de maças:", Macas, "Valor total:", Macas1)
