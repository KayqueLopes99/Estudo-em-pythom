# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.


import random
while True:

    usuario = int(input("Informe um número:"))
    pergunta = str(input("Par ou Ímpar? [P/I]: ")).upper().strip()[0]
    computador = random.randint(1, 10)
    # ESCOLHA do usuário e do computador somados.
    Total = usuario + computador
    # Par.
    if Total % 2 == 0:
        resultado = 'P'
    else:
    # Impar
        resultado = 'I'
    print(f"Você jogou {usuario} e o computador {computador}. Total de {Total} que é {resultado}")
    # Essa é a condição para parada.
    if pergunta != resultado:
        print("Game Over.")
        break
    else:
        print("====    Você VENCEU!!!   ====")
        print("=== Vamos Jogar novamente ===")
