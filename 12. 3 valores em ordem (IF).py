# Algoritmo 12. 3 valores em ordem (IF)
# Dev: Vitor Bitencourt
# Data: 18/06/2022

print("Digite 3 valores inteiros")
Valor1 = int(input("Primeiro valor: "))
Valor2 = int(input("Segundo valor: "))
Valor3 = int(input("Terceiro valor: "))

# Primeiro Quadro IF (Valor 1 < Valor 2 < Valor 3); ou (Valor 1 < Valor 3 < Valor 2):
if (Valor1 < Valor2) and (Valor1 < Valor3):
    if Valor2 < Valor3:
        print("Valores em ordem crescente:")
        print("Primeiro Valor:", Valor1, "Segundo Valor:", Valor2, "Terceiro Valor:", Valor3)
    else:
        print("Valores em ordem crescente:")
        print("Primeiro Valor:", Valor1, "Terceiro Valor:", Valor3, "Segundo Valor:", Valor2)

# Segundo Quadro IF (Valor 2 < Valor 1 < Valor 3); ou (Valor 2 < Valor 3 < Valor 1):
if (Valor2 < Valor1) and (Valor2 < Valor3):
    if Valor1 < Valor3:
        print("Valores em ordem crescente:")
        print("Segundo Valor:", Valor2, "Primeiro Valor:", Valor1, "Terceiro Valor:", Valor3)
    else:
        print("Valores em ordem crescente:")
        print("Segundo Valor:", Valor2, "Terceiro Valor:", Valor3, "Primeiro Valor:", Valor1)

# Terceiro Quadro IF (Valor 3 < Valor 1 < Valor 2); ou (Valor 3 < Valor 2 < Valor 1):
if (Valor3 < Valor1) and (Valor3 < Valor2):
    if Valor1 < Valor2:
        print("Valores em ordem crescente:")
        print("Terceiro Valor:", Valor3, "Primeiro Valor:", Valor1, "Segundo Valor:", Valor2)
    else:
        print("Valores em ordem crescente:")
        print("Terceiro Valor:", Valor3, "Segundo Valor:", Valor2, "Primeiro Valor:", Valor1)
