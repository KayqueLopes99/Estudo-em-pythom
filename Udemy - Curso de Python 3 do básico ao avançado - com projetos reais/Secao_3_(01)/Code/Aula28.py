"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Informe seu Nome: ') 
idade = input('Informe sua Idade: ')


# Quando você escreve if idade:, está verificando se a variável idade é considerada "verdadeira" em um contexto lógico.
if nome and idade:
    print(f"Seu Nome: {nome}")
    print(f"Seu Nome invertido: {nome[::-1]}")
    if ' ' in nome:
        print("Seu Nome contém espaços.")
    else:
        print("Seu Nome não contém espaços.")
    print(f"O Nome {nome} tem {len(nome)} Letras.")
    print(f"A primeira Letra do seu nome: {nome[0]}")
    print(f"A Ultima Letra do seu nome: {nome[-1]}")

else:
    print("Desculpe, você deixou campos vazios.")