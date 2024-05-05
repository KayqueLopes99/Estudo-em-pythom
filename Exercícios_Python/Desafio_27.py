# Faça um programa qua laia o nome completo de uma pessoa, mostrando am seguida o primeiro a o último nome separadamente.
# Ex: Ana Maria da Souza primeiro = Ana último = Souza

nome = str(input('Informe seu nome completo: ')).title()

palavras = nome.split()
print(palavras)

print("Primeiro nome: ", palavras[0])
print("Último nome: ", palavras[-1])
