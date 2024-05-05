# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = str(input("Informe o nome da cidade: ")).title()
# .strip() para retirar os espaços caso o usuário digite.
palavras = cidade.split()
print(palavras)
print('Primeira palavras !?')
print("Rio" == palavras[0])

