# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas.
# O nome com todas minúsculas.
# Quantas letras ao todo(Sem considerar espaços).
#  Quatas letras tem o primeiro nome.

nome = str(input('Informe seu nome completo: ')).strip()
print('Maiúsculas: {}'.format(nome.upper()))

print("Minúsculas: {}".format(nome.lower()))

nome2 = nome.replace(' ','')
print("Numero de letras sem espaço: {}".format(len(nome2)))

nome3 = nome.split()
print(nome3)
print('Quantidade de letras no primeiro nome: {}'.format(len(nome3[0])))

