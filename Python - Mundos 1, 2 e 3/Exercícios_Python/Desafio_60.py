# Faça um programa que leia um número qualquer e ostre o seu fatorial.
# 5! = 5 x 4 x 3 x 2 x 1 = 120
valor1 = int(input('Informe o Algarismo: '))


if valor1 == 0 or valor1 == 1:
    fatorial = 1
else:
    fatorial = valor1
    while valor1 != 1:
        valor1 -= 1
        fatorial = fatorial * valor1

print("Fatorial: {}".format(fatorial))
