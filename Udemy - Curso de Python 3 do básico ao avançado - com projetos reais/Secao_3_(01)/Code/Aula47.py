""" Exercício.

Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.


-> Uma dica para está questão podemos armazenar as letras que estão na palavra em uma varíavel, e depois usar o loop for para percorrer a palavra colocando as letras ques estão nela, o qual se localizam na variavel que está armazenando elas.
"""

import os
palavra_secreta = 'one piece'
contagem_tentativas = 0
palavra_visivel_formada = ["*"] * len(palavra_secreta)
while True:
    print("-" * 33)
    print("-=== Jogo da Palavra Secreta ===-")
    print("-" * 33)
    print("1 - Entrar no Jogo.")
    print("2 - Sair [Desistir].")
    opcao = input("Informe uma opção do menu: ")
    
    # Verifica se a entrada é numérica
    if not opcao.isdigit():
        print("Isso não é um número.")
        continue
    
    # Converte a entrada para inteiro
    int_opcao = int(opcao)
    
    # Verifica a opção escolhida
    if int_opcao == 1:  
        print(f"Tentativa: {contagem_tentativas}.")
        letra = input("Informe uma letra: ").lower()
        contagem_tentativas += 1

        if len(letra) > 1:
            print("Uma Letra, por favor.")
            continue       
        if letra in palavra_secreta:            
           # Vamos enumerar todas as letras. 'i' é o índice da letra, e 'caractere' é a letra correspondente da palavra_secreta.

           for i, caractere in enumerate(palavra_secreta):
                if caractere == letra:  # Verifica se a letra fornecida pelo usuário está na posição atual.
                  palavra_visivel_formada[i] = letra
            
           print(palavra_visivel_formada)

        else:
            print(f"A caractere [{letra}] Não está a Palavra Secreta.")

        if "*" not in palavra_visivel_formada:
              print(f"Palavra Completada Parabens!!!: Palavra é {palavra_secreta}.")
              palavra_visivel_formada = ["*"] * len(palavra_secreta) 
              contagem_tentativas = 0
              os.system('cls')
              
              
        
    elif int_opcao == 2: 
        print("Saindo do Jogo...")
        
        break

    else:  # Caso o número não esteja no menu
        print("Opção não está presente no menu.")

