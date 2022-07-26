# Algoritmo 16. Três valores e o maior deles (IF)
# Dev: Vitor Bitencourt
# Data: 21/06/2022

Valor1 = int(input("Digite o primeiro valor: "))
Valor2 = int(input("Digite o segundo valor: "))
Valor3 = int(input("Digite o terceiro valor: "))


if (Valor1 > Valor2) and (Valor1 > Valor3):
    print(Valor1, "Esse é o maior valor")
elif (Valor2 > Valor1) and (Valor2 > Valor3):
    print(Valor2,"Esse é o maior valor")
elif (Valor3 > Valor1) and (Valor3 > Valor2):
    print(Valor3, "Esse é o maior valor")
