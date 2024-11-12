# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem papes. Se p valor digitad for impar desconsidere.
soma = 0
for i in range(1,7):
    a1 = int(input("Informe o {} Algarismo: ".format(i)))
    if a1 % 2 == 0:
        soma += a1
print("Soma dos pares: {}".format(soma))

