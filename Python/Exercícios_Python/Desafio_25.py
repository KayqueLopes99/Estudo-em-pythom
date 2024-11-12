# Crie um programa que leia o nome de uma pessoa e diga se ela tem Silva no nome.
nome = str(input("Informe o nome do usuario: ")).title()
palavras = nome.split()
print(palavras)
print('Primeira palavras !?')
print("Silva" in palavras)
