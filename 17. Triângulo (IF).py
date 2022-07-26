# Algoritmo 17. Triângulo (IF)
# Dev: Vitor Bitencourt
# Data: 21/06/2022
#Triângulo Equilátero: possui os 3 lados iguais.
#Triângulo Isóscele: possui 2 lados iguais.
#Triângulo Escaleno: possui 3 lados diferentes.

Medida1 = float(input("Medida do primeiro lado: "))
Medida2 = float(input("Medida do segundo lado: "))
Medida3 = float(input("Medida do terceiro lado: "))

if (Medida1 == Medida2) and (Medida1 == Medida3):
    print("É um Triângulo Equilátero, pois possui os 3 lados iguais.")
elif (Medida1 == Medida2) and (Medida1 != Medida3):
    print("É um Triângulo Isóscele, pois possui 2 lados iguais.")
elif (Medida2 == Medida3) and (Medida2 != Medida1):
    print("É um Triângulo Isóscele, pois possui 2 lados iguais.")
elif (Medida1 == Medida3) and (Medida1 != Medida2):
    print("É um Triângulo Isóscele, pois possui 2 lados iguais.")
elif (Medida1 != Medida2) and (Medida1 != Medida3):
    print("É um Triângulo Escaleno, pois possui 3 lados diferentes.")
