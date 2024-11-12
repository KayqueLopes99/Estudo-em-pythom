# Escreva um programa que faça o computador "Pensar" em um número inteiro entre 0 e 5e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

# O programa deve escrever na tela se o usuário venceu ou perdeu
import random
# Temos alguns numeros aleatorios com essa biblioteca.

a = int(input('Digite o primeiro algarismo de 0 a 5: '))

ramdomi = random.randint(0, 5)

if a == ramdomi:
    print("Venceu!")
else:
    print("Perdeu!")