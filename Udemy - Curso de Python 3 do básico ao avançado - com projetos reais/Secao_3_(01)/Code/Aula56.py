# É importante você não alterar os valores por completo na lista.
# Use uma lista fixa.
# Não alterar os valores mútaveis. 

frase = '    Olha só que   , coisa interesasante          '
lista_frase_primaria = frase.split(',')

lista_frase_secundaria = []

for indice, frase in enumerate(lista_frase_primaria):
    lista_frase_secundaria.append(lista_frase_primaria[indice].strip())

# print(lista_frase_secundaria)
frases_unidas = ' - '.join(lista_frase_secundaria)
print(frases_unidas)