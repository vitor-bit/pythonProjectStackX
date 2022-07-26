# Algoritmo 09. Idade para voto (IF)
# Dev: Vitor Bitencourt
# Data 15/06/2022

#Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma
#mensagem que diga se ela poderá ou não votar este ano
#(não é necessário considerar o mês em que ela nasceu).

Nome = input("Qual seu nome? ")
AnoDeNascimento = int(input("Qual o ano de nascimento? "))
AnoAtual = int(input("Qual o ano atual? "))

Idade = int(AnoAtual - AnoDeNascimento)

# ----------- Quadro IF, Mostrar mensagem que diga se ela poderá ou não votar este ano:

if Idade >= 18:
    print(Nome, "você tem idade necessária para votar, pois nasceu em",
          AnoDeNascimento, "e tem", Idade, "anos")
else:
    print(Nome, "você não tem idade necessária para votar, pois nasceu em",
          AnoDeNascimento, "e tem", Idade, "anos e para votar é preciso ter no minimo 18")
