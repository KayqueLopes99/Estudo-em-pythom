# Desenvolva um programa que laia o comprimento de três retas a diga ao usuário sa elas podem ou não formar um triângulo.

lado1 = float(input('Informe o Primeiro Lado: '))
lado2 = float(input('Informe o Segundo Lado: '))
lado3 = float(input('Informe o Terceiro Lado: '))

if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1:
    print("Pode formar um Triângulo!")
else: 
    print("Não pode formar um Triângulo!")
