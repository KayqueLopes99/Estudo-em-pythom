# Melhoria do Jogo de desadio 28

# O programa deve escrever na tela se o usuário venceu ou perdeu
import random
# Temos alguns numeros aleatorios com essa biblioteca.

a = int(input('Digite o primeiro algarismo de 0 a 5: '))
chance = 1
ramdomi = random.randint(0, 10)
while a != ramdomi:
    a = int(input('Digite o primeiro algarismo de 0 a 10: '))
    chance += 1
print("Venceu!, foram necessárias {} Tentativas.".format(chance))
