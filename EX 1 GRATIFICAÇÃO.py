# Algoritmo 001: Gratificação de Natal (if)
# Dev: Vitor Bitencourt
# Data 06/06/2022


Nome = input("Digite seu nome: ")
Numero_De_Horas_Extras = int(input("Digite as horas extras que trabalhou: "))
Numero_De_Hora_Faltas = int(input("Digite as horas que faltou no trabalho: "))


H = Numero_De_Horas_Extras - (2/3 * Numero_De_Hora_Faltas)

Min = int(H * 60)

if Min < 600:
    print(Nome, "sua gratificação de natal foi de R$100, pois trabalhou", Min, "minutos.")

else:
    if (Min >= 600) and (Min <= 1200):
        print(Nome, "sua gratificação de natal foi de R$200, pois trabalhou", Min, "minutos.")

    else:
        if (Min >= 1201) and (Min <= 1800):
            print(Nome, "sua gratificação de natal foi de R$300, pois trabalhou", Min, "minutos.")

        else:
            if (Min >= 1801) and (Min <= 2400):
                print(Nome, "sua gratificação de natal foi de R$400, pois trabalhou", Min, "minutos.")

            else:
                print(Nome, "sua gratificação de natal foi de R$500, pois trabalhou", Min, "minutos.")
