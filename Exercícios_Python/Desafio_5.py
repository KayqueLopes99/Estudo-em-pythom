# Faça um programa que leia um número
# interio e mostre na tela o seu sucessor
# e antecessor

numero = int(input("Informe um numero: \n"))

print("\033[33m Vamos ver seu sucessor e antecessor do numero {:.2f} \033[m".format(numero))
antesessor = numero - 1
sucessor = numero + 1 
print("\033[34m Seu santecessor: {:.2f} \033[m".format(antesessor))
print("\033[34m Seu sucessor: {:.2f} \033[m".format(sucessor))