# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule  o preço da passagem, cobrando R$0,50 POR Km para viagens de até 200Km  e r$ para viagens longas.

Viagem = int(input("Informe a diatância da viagem em Km: "))

if Viagem <= 200:
    Resultado = Viagem * 0.5
else:
    print("Viagem muito longa!")
    Resultado = Viagem * 0.45
print("Valor: R${}".format(Resultado))