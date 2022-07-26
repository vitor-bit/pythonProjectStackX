# Algoritmo 006. Receber nomes e salários (While)
# Dev: Vitor Bitencourt
# Data 10/06/2022
Laco1 = True
SalarioCarlos = float(input("Carlos, digite seu sálario: "))
SalarioJoao = SalarioCarlos / 3
print("Sálario do Carlos:", SalarioCarlos)
print("Sálario do João:", SalarioJoao)
# ---------------- Estrutura de repetição while, para calcular os sálarios ao longo dos meses:
Mes = 1
while Laco1:
    if SalarioJoao >= SalarioCarlos:
        Laco1 = False

    else:
        SalarioCarlos = SalarioCarlos * 1.02
        SalarioJoao = SalarioJoao * 1.05
        Mes += 1
    continue
    break
print("Sálario de Carlos após aplicar seu salário integralmente na caderneta de poupança, que rende 2% ao mês:"
        ,SalarioCarlos,", durante", Mes, "meses.")
print("Sálario de João após aplicar seu salário integralmente no fundo de renda fixa, que rende 5% ao mês:"
      , SalarioJoao, ",durante", Mes, "meses.")
print("Foram precisos", Mes, "meses para o sálario de joão ser equivalente ou maior que o de Carlos.")


# ----------------- PROFESSOR

Salario = ValorPoupanca = RendaPoupanca = ValorFundoRendaFixa = RendaFundo = Meses = 0
RendaPoupanca = 1.02
RendaFundo = 1.05

Salario = float(input("Qual o salário: "))

ValorPoupanca = Salario * RendaPoupanca
print(ValorPoupanca)
Salario = Salario / 3
ValorFundoRendaFixa = Salario * RendaFundo
print(ValorFundoRendaFixa)

while True:
    Meses += 1
    print(f"O valor de investimentos do João é: , {ValorFundoRendaFixa:,.2f}, mês", Meses)
    if ValorFundoRendaFixa <= ValorPoupanca:
        ValorFundoRendaFixa = ValorFundoRendaFixa * RendaFundo
        continue
    else:
        break