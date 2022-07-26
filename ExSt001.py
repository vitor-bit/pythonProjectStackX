# Algoritmo 001 : Primirivos e Identificadores
# Dev : Vitor Bitencourt
# Data : 20.05.2022


# Uso de Bibliotecas

import math

print(math.sqrt(4))
print(math.pow(7, 5))
print(2 ** 2)
print(divmod(25, 4))
print(25 // 4)
print(25 % 4)

# Soma e Subtração ------------------
print(3 + 8)
print(8 - 3)

# Pôtencia -----------------------------
print(2 ^ 4)

# Divisão -----------------------------
print(4 / 4)
# print(4 / 0)

# Precedência de operadores ---------------------------
# a ** 2 + b * 3 % 2, sendo que a=4 e b=3
# 1. a ** 2 + b * 3 % 2 (original)
# 2. 4 ** 2 + 3 * 3 % 2 (troquei os literais por números)
# 3. 16 + 3 * 3 % 2 (Potência)
# 4. 16 + 9 % 2 (Multiplicação)
# 5. 16 + 1 (Resto da divisão)
# 6. 17 (Soma)
print(4 ** 2 + 3 * 3 % 2)

a = 4
b = 3
print(a ** 2 + b * 3 % 2)

# Operadores lógicos: AND E -------------
print(4 < 8 and 3 < 4)  # T e T = True
print(8 == 8 and 3 > 4)  # T e F = False
print(8 == 7 and 3 < 4)  # F e T = False
print(4 > 8 and 3 > 4)  # F e F = False

# Operadores relacionais

# == True, Se a e b são iguais
print(77 == 77)
print(77 == 76)

# != True, Se a e b são diferentes
print(44 != 31)

print(2 + 3 * 5 + 30 // 10)

print(True or False and not True)

