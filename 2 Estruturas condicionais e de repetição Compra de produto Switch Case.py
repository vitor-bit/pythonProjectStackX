# Algoritmo 2. Estruturas condicionais e de repetição: Compra de produto (Switch Case)
# Dev: Vitor Bitencourt
# Data 23/06/2022

CodigoProduto = int(input("Digite o código do produto: "))
QuantidadeProduto = int(input("Digite a quantidade de produtos comprados: "))


if (CodigoProduto >= 1) and (CodigoProduto <=10):
# --------------------------Preço unitário R$10,00: Calcular o preço total da nota e mostrar
    print("O preço unitário do produto comprado: R$10,00")
    PrecoTotalNota = QuantidadeProduto * 10.00
    print("Preço total da nota:", PrecoTotalNota)
# --------------------------Desconto 5%: Calcular o desconto e mostrar o preço final:
    if PrecoTotalNota <= 250:
        print("Valor de desconto 5%")
        PrecoTotalNota = PrecoTotalNota * (1 - 0.05)
        print("Preço final com o desconto:", PrecoTotalNota)
    else:
        print("O produto não tem desconto")
        print("Preço final:", PrecoTotalNota)
elif (CodigoProduto >= 11) and (CodigoProduto <=20):
# --------------------------Preço unitário R$15,00: Calcular o preço total da nota e mostrar
    print("O preço unitário do produto comprado: R$15,00")
    PrecoTotalNota = QuantidadeProduto * 15.00
    print("Preço total da nota:", PrecoTotalNota)
# --------------------------Desconto 10%: Calcular o desconto e mostrar o preço final:
    if (PrecoTotalNota >= 250) and (PrecoTotalNota <= 500):
        print("Valor de desconto 10%")
        PrecoTotalNota = PrecoTotalNota * (1 - 0.10)
        print("Preço final com o desconto:", PrecoTotalNota)
    else:
        print("O produto não tem desconto")
        print("Preço final:", PrecoTotalNota)
elif (CodigoProduto >= 21) and (CodigoProduto <=30):
# --------------------------Preço unitário R$20,00: Calcular o preço total da nota e mostrar
    print("O preço unitário do produto comprado: R$20,00")
    PrecoTotalNota = QuantidadeProduto * 20.00
    print("Preço total da nota:", PrecoTotalNota)
# --------------------------Desconto 15%: Calcular o desconto e mostrar o preço final:
    if PrecoTotalNota > 50:
        print("Valor de desconto 15%")
        PrecoTotalNota = PrecoTotalNota * (1 - 0.15)
        print("Preço final com o desconto:", PrecoTotalNota)
    else:
        print("O produto não tem desconto")
        print("Preço final:", PrecoTotalNota)
elif (CodigoProduto >= 31) and (CodigoProduto <=40):
# --------------------------Preço unitário R$30,00: Calcular o preço total da nota e mostrar
    print("O preço unitário do produto comprado: R$30,00")
    PrecoTotalNota = QuantidadeProduto * 30.00
    print("Preço total da nota:", PrecoTotalNota)
# --------------------------Desconto 0%: Mostrar o preço final:
    print("O produto não tem desconto")
    print("Preço final:", PrecoTotalNota)
