# Algoritmo 1. Estruturas condicionais e de repetição: Preço de produtos (Swich Case)
# Dev: Vitor Bitencourt
# Data 22/06/2022


Preco = float(input("Digite o preço do produto: "))
Categoria = int(input("Digite a categoria do produto: 1 – limpeza; 2 – alimentação; ou 3 – vestuário: "))
Situacao = str(input("Digite a situação do produto: R – produtos que necessitam de refrigeração; "
                     "e N – produtos que não necessitam de refrigeração: "))
Imposto = 0.08


if Preco <= 25:
# ------------------------------------Calcular o valor do preço com aumento e mostrar o valor do aumento:
    if(Categoria == 1):
        PrecoAumento = Preco * 1.05
        print("Valor do aumento: 5%")
    else:
        if (Categoria == 2):
            PrecoAumento = Preco * 1.08
            print("Valor do aumento: 8%")
        else:
            PrecoAumento = Preco * 1.10
            print("Valor do aumento: 10%")
# ---------------------------------------------Calcular preço final e o imposto e mostrar:
    if (Categoria == 2) or (Situacao == "R"):
        PrecoFinal = PrecoAumento * (1 - 0.05)
        print("Valor do imposto: 5%")
    else:
        PrecoFinal = PrecoAumento - (PrecoAumento * Imposto)
        print("Valor do imposto: 8%")
# ------------------------------------------------Mostrar a classificação de acordo com o preço final:
    if PrecoFinal <= 50:
        print("Preço final:", PrecoFinal, "Classificação: Barato")
    else:
        if (PrecoFinal > 50) and (PrecoFinal < 120):
            print("Preço final:", PrecoFinal, "Classificação: Normal")
        else:
            print("Preço final:", PrecoFinal, "Classificação: Caro")
else:
# ---------------------------------------------Calcular o valor do preço com aumento e mostrar o valor do aumento:
    if (Categoria == 1):
        PrecoAumento = Preco * 1.12
        print("Valor do aumento: 12%")
    else:
        if (Categoria == 2):
            PrecoAumento = Preco * 1.15
            print("Valor do aumento: 15%")
        else:
            PrecoAumento = Preco * 1.18
            print("Valor do aumento: 18%")
# ---------------------------------------------Calcular preço final e o imposto e mostrar:
    if (Categoria == 2) or (Situacao == "R"):
        PrecoFinal = PrecoAumento * (1 - 0.05)
        print("Valor do imposto: 5%")
    else:
        PrecoFinal = PrecoAumento - (PrecoAumento * Imposto)
        print("Valor do imposto: 8%")
# ------------------------------------------------Mostrar a classificação de acordo com o preço final:
    if PrecoFinal <= 50:
        print("Preço final:", PrecoFinal, "Classificação: Barato")
    else:
        if (PrecoFinal > 50) and (PrecoFinal < 120):
            print("Preço final:", PrecoFinal, "Classificação: Normal")
        else:
            print("Preço final:", PrecoFinal, "Classificação: Caro")