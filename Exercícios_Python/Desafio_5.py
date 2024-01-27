# Faça um programa que leia um número
# interio e mostre na tela o seu sucessor
# e antecessor

numero = int(input("Informe um numero: \n"))

print("Vamos ver seu sucessor e antecessor do numero {:.2f}".format(numero))
antesessor = numero - 1
sucessor = numero + 1 
print("Seu santecessor: {:.2f}".format(antesessor))
print("Seu sucessor: {:.2f}".format(sucessor) )