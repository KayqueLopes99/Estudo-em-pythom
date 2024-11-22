# Exercício guiado com while
# Iterando strings com while

#       1234556789101112

nome = input("Informe o seu nome: ")
tamanho_nome = len(nome)
novo_nome = ''
indice = 0

# Acumulação.
while indice < tamanho_nome:
    nova_letra = nome[indice]
    novo_nome += f"*{nova_letra}* "
    indice += 1
print(novo_nome)