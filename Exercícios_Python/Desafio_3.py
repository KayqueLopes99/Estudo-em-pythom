# Crie um script Python que leia dois numeros a tente 
# mostrar a soma entre eles.
numero_1 = float(input('\033[35m Digite o primeiro algarismo\033[m'))
numero_2 = float(input('\033[36mDigite o segundo algarismo\033[m'))
soma = numero_1 + numero_2
print('\033[37mSoma dos dois algarismos: {} e {}: \033[m'.format(numero_1, numero_2), soma)