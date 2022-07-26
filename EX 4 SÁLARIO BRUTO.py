# Algoritmo 004: Sálario Bruto (if)
# Dev: Vitor Bitencourt
# Data 06/06/2022

SalarioBruto = float(input("Digite seu sálario bruto: "))

if SalarioBruto <= 350:
    SalarioGratificao = SalarioBruto + 100
    SalarioFinal = SalarioGratificao - ((SalarioGratificao * 7) / 100)


elif (SalarioBruto >= 351) and (SalarioBruto <= 600):
    SalarioGratificao = SalarioBruto + 75
    SalarioFinal = SalarioGratificao - ((SalarioGratificao * 7) / 100)

elif (SalarioBruto >= 601) and (SalarioBruto <= 900):
    SalarioGratificao = SalarioBruto + 50
    SalarioFinal = SalarioGratificao - ((SalarioGratificao * 7) / 100)

elif SalarioBruto >= 901:
    SalarioGratificao = SalarioBruto + 35
    SalarioFinal = SalarioGratificao - ((SalarioGratificao * 7) / 100)

print("Este é seu sálario final : R$", SalarioFinal,", somando a gratificação e descontando 7% de imposto.")
