# Algorito 14. Polígono (IF)
# Dev: Vitor Bitencourt
# Data: 18/06/2022

Lados = int(input("Digite o número de lados do polígono: "))
MedidaLado = float(input("Digite a medida do lado do polígono em cm: "))

Area = Lados * MedidaLado

if Lados == 3:
    print("O polígono é um triângulo, pois tem 3 lados. E a área é de", Area, "cm.")
elif Lados == 4:
    print("O polígono é um quadrado, pois tem 4 lados. E a área é de", Area, "cm.")
elif Lados == 5:
    print("O polígono é um pentágono, pois tem 5 lados. E a área é de", Area, "cm.")
