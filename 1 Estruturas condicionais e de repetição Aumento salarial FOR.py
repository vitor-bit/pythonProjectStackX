# Algoritmo 1. Estruturas condicionais e de repetição: Aumento salarial (FOR)
# Dev: Vitor Bitencourt
# Data 22/06/2022

SalarioInicial = 1000.00
AumentoPorcentual = 0.015
AumentoPorcentualTela = 1.5
AnoInicial = 0

NomeFun = str(input("Digite o nome do funcionário: "))

print("O funcionário", NomeFun, "teve no ano de 2000, o salário inicial de R$1.000")
Salario = (SalarioInicial * AumentoPorcentual) + SalarioInicial
print("No ano de 2001, recebeu um aumento de 1,5% sobre seu salário inicial, totalizando R$",Salario)
print("A partir de 2001,"
	  " os aumentos salariais sempre corresponderam ao dobro do percentual do ano anterior, sendo assim:")

for AnoInicial in range(2001, 2017):
    Salario = 0
    AumentoPorcentual = AumentoPorcentual * 2
    Salario = (SalarioInicial * AumentoPorcentual) + SalarioInicial
    AnoInicial = AnoInicial + 1
    AumentoPorcentualTela = AumentoPorcentualTela * 2
    print("No ano de", AnoInicial, "recebeu o sálario de R$",Salario, "com o aumento salarial de",
        AumentoPorcentualTela,"%")