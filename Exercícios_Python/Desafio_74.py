# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
import random

# Inicializa maior com 0 e menor com um número alto.
maior = 0
menor = 100


tupla = (random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), )

print(tupla)

# Itera sobre cada número na tupla.
# A variavel numero vai percorer a tupla procurando o maior e menor.
for numero in tupla:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(f"\033[35mMaior Número:\033[m {maior}")
print(f"\033[35mMenor Número:\033[m {menor}")
