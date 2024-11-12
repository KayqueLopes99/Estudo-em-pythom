# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

import math

numero_escolhido = float(input('Digite um numero real para aredondar: '))

floor = math.floor(numero_escolhido)

print('O numero {} tem a parte inteira: {}'.format(numero_escolhido, floor))




