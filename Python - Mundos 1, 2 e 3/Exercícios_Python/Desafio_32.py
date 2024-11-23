# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input("Informe o Ano: "))

if ano % 4 == 0:
    print("Ano {} Bissexto.".format(ano))

else:
    print("Ano {} Não Bissexto.".format(ano))