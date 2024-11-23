# Faça um programa que abra e reproduza um audio.

# Importa a biblioteca pygame
import pygame

# Inicializa todos os módulos importados do pygame
pygame.init()

# Carrega a música 'desafio21.mp3' para ser reproduzida
pygame.mixer.music.load('desafio21.mp3')

# Começa a reproduzir a música que foi carregada anteriormente
pygame.mixer.music.play()

# Adiciona um loop de espera ativo para manter o programa em execução enquanto a música está tocando
while pygame.mixer.music.get_busy():
    # Verifica a cada 10 milissegundos se a música ainda está tocando
    pygame.time.Clock().tick(10)

# Aguarda até que todos os eventos sejam processados
pygame.event.wait()
