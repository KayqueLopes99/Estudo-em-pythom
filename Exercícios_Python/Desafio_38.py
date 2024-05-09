# Escreva um programa que leia dois números interos e compare-os. mostrando na tela uma mensagem:

# - O Primeiro valor é maior 
# - O Segundo valor é maior  
# - Não existe valor maior, os dois são iguais.

numero1 = int(input('\033[31m Informe o Primero Número: \033[m'))

numero2 = int(input('\033[31m Informe o Segundo Número: \033[m'))

if numero1 > numero2:
    print('O Primeiro número {} é maior que o Segundo número {}'.format(numero1,numero2))
elif numero2 > numero1:
    print('O Segundo número {} é maior que o Primeiro número {}'.format(numero2,numero1))
else:
    print("Números iguais.")