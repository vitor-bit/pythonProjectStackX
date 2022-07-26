# Algoritmo 003: Idade de um nadador (if)
# Dev: Vitor Bitencourt
# Data 06/06/2022

Idade = int(input("Digite sua idade: "))

if Idade < 5:
    print("Sua idade é muito inferior e não se encaixa em nenhuma categoria.")

elif Idade >= 80:
    print("Sua idade é muito superior e não se encaixa em nenhuma categoria.")

elif (Idade >= 5) and (Idade <= 7):
    print("Sua categoria é infantil, pois você tem ", Idade, "anos.")

elif (Idade >= 8) and (Idade <= 10):
    print("Sua categoria é juvenil, pois você tem ", Idade, "anos.")

elif (Idade >= 11) and (Idade <= 15):
    print("Sua categoria é adolescente, pois você tem ", Idade, "anos.")

elif (Idade >= 16) and (Idade <= 30):
    print("Sua categoria é adulto, pois você tem ", Idade, "anos.")

elif Idade > 30:
    print("Sua categoria é sênior, pois você tem ", Idade, "anos.")
