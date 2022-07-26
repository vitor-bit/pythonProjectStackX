# Algoritmo 002: Idade e Peso (if)
# Dev: Vitor Bitencourt
# Data 06/06/2022

Idade = int(input("Digite sua idade: "))
Peso = float(input("Digite seu peso: "))

if (Idade < 20) and (Peso < 61):
    print("Seu grupo de risco é 9.")

elif (Idade < 20) and (Peso > 60) and (Peso <= 90):
    print("Seu grupo de risco é 8.")

elif (Idade < 20) and (Peso > 90):
 print("Seu grupo de risco é 7.")

if (Idade >= 20) and (Idade <= 50) and (Peso < 61):
    print("Seu grupo de risco é 6.")

elif (Idade >= 20) and (Idade <= 50) and (Peso > 60) and (Peso <= 90):
    print("Seu grupo de risco é 5.")

elif (Idade >= 20) and (Idade <= 50) and (Peso > 90):
    print("Seu grupo de risco é 4.")

if (Idade > 50) and (Peso < 61):
    print("Seu grupo de risco é 3.")

elif (Idade > 50) and (Peso > 60) and (Peso <= 90):
    print("Seu grupo de risco é 2.")

elif (Idade > 50) and (Peso > 90):
    print("Seu grupo de risco é 1.")
