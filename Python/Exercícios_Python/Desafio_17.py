# Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa .

import math

cateto_oposto = int(input("Escolha o valor do primeiro cateto: "))

cateto_adjacente = int(input("Escolha o valor do segundo cateto: "))

hipotenusa = math.sqrt(pow(cateto_adjacente,2) + pow(cateto_oposto,2))


print('opposite side: {}'.format(cateto_oposto))

print('adjacent side: {}'.format(cateto_oposto))

print('The hypotenuse is: {}'. format(hipotenusa))