# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
# import pygame
from time import sleep
lista_oficial = []  # Lista para armazenar as sublistas.
# pygame.init()
print("="*20)
while True:
    print("1 - Jogar na Mega Sena.")
    print("0 - Sair.")
    opcao = int(input("Informe uma Opção: "))
    if opcao == 1:
        print("======= Vamos Lá =======")
        qtd = int(input("Informe Quantas Vezes você vai jogar: "))
        for i in range(qtd):       
            sublista = []
            # Enquanto o tamanho d lista não for 6.
            while len(sublista) < 6:
                numero = randint(1, 60)
                # Se o número não estiver na Lista.
                if numero not in sublista:
                    sublista.append(numero)
                    sublista.sort()
            lista_oficial.append(sublista)

        for i, sublista in enumerate(lista_oficial):
            print(f"Jogo {i+1}: {sublista}")
            sleep(2)
            # pygame.time.wait(1000)  # pausa o programa por 500 milissegundos
        print("+="*5, 'Boa Sorte', "=+"*5)

    elif opcao == 0:
        print("Saindo...")
        break

    else:
        print("Informe Algo Válido.")
