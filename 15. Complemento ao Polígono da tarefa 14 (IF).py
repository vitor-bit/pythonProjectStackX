# Algoritmo 15. Complemento ao Polígono da tarefa 14 (IF)
# Dev: Vitor Bitencourt
# Data: 21/06/2022

Lados = int(input("Digite o número de lados do polígono: "))
MedidaLado = float(input("Digite a medida do lado do polígono em cm: "))

Area = Lados * MedidaLado

if Lados == 3:
    print("O polígono é um triângulo, pois tem 3 lados. E a área é de", Area, "cm")
elif Lados == 4:
    print("O polígono é um quadrado, pois tem 4 lados. E a área é de", Area, "cm")
elif Lados == 5:
    print("O polígono é um pentágono, pois tem 5 lados. E a área é de", Area, "cm")
elif Lados < 3:
    print("Não é um polígono, pois os lados são inferiores a 3")
elif Lados > 5:
    print("Polígono não identificado, pois os lados são superiores a 5")

