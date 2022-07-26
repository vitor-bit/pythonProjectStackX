# Algoritmo 005: Empresa com 10 funcionários (While)
# Dev: Vitor Bitencourt
# Data 06/06/2022

Laco1 = 1
Laco2 = True
Laco3 = True

while Laco1 <= 10:
    # Quadro do laço principal

    SalarioMinimo = 450
    SalarioInicial = 0
    SalarioFinal = 0
    AuxilioAlimentacao = 0

    Codigo = input("Digite o código do funcionário: ")
    HorasTrabalhadas = float(input("Digite as horas trabalhadas: "))

    # ---------------------------------- Condicionais Categoria e Turno:
    while Laco2:
        Categoria = input("Digite a categoria: ")
        if Categoria == 'O' or Categoria == 'G':
            Laco2 = False
        else:
            print("As categoria possíveis são: O e G, digite novamente.....")
            continue
        break

    # ---------------------------------- Turno:
    while Laco3:
        Turno = input("Digite o turno do trabalho: ")
        if Turno == 'M' or Turno == 'V' or Turno == 'N':
            Laco3 = False
        else:
            print("Os turnos de trabalho possíveis são: M, V e N, digite novamente.....")
            continue
        break
    # ------------------------------------ Condicionais para a Categoria G e Turno N:
    if Categoria == "G" and Turno == "N":
        ValorHora = SalarioMinimo * 0.18
        SalarioInicial = HorasTrabalhadas * ValorHora
        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        else:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
    # ------------------------------------ Condicionais para a Categoria G e Turno M ou V:
    if Categoria == "G" and Turno == "M" or Turno == "V":
        ValorHora = SalarioMinimo * 0.15
        SalarioInicial = HorasTrabalhadas * ValorHora
        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        else:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
    # ------------------------------------ Condicionais para a Categoria O e Turno N:
    if Categoria == "O" and Turno == "N":
        ValorHora = SalarioMinimo * 0.13
        SalarioInicial = HorasTrabalhadas * ValorHora
        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        else:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
    # ------------------------------------ Condicionais para a Categoria O e Turno M ou V:
    if Categoria == "O" and Turno == "M" or Turno == "V":
        ValorHora = SalarioMinimo * 0.13
        SalarioInicial = HorasTrabalhadas * ValorHora
        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        else:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
    # -------------------------------------- Quadro Resumo:
    print("Código:", Codigo, "/ Horas Trabalhadas:", HorasTrabalhadas, "/ Categoria:", Categoria,
        "/ Turno:", Turno)
    print("Valor Da Hora:", ValorHora, "/ Sálario Inicial:", SalarioInicial, "/ Auxílio Alimentação:",
        AuxilioAlimentacao, "/ Sálario Final:", SalarioFinal)

    # ------------------------------------  Verificar os laços:
    print("Número do laço principal:", Laco1)
    Laco1 = Laco1 + 1
    Laco2 = True
    Laco3 = True
print("Fim.")