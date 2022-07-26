# Algoritmo 008. Número maior (IF)
# Dev: Vitor Bitencourt
# Data 15/06/2022

# Escreva um programa para ler 2 valores
# (considere que não serão informados valores iguais) e escrever o maior deles.

Valor1 = input("Digite o primeiro valor: ")
Valor2 = input("Digite o segundo valor: ")

# ---------Condicional If e else, tratando os valores 1 e 2.

if Valor1 > Valor2:
    print("O primeiro valor digitado é maior que o segundo valor, sendo", Valor1, "maior que", Valor2)
else:
    print("O segundo valor digitado é maior que o primeiro valor, sendo", Valor2, "maior que", Valor1)