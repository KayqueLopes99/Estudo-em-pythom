# Faça um programa qye mostre na tela uma contagem regressiva para o estouro de fogos de artificio, com pausa.


import pygame

# Inicialização
pygame.init()
print("Fogos de artificio em:")

for i in range(10, -1, -1):
    # Atraso de 1000 milissegundos (1 segundo)
    pygame.time.delay(1000)
    print(i)
print("Fogos de artificio!")