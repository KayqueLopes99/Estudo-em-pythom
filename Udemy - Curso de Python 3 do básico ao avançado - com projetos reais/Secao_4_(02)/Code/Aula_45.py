# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

import copy
lista_states = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list_siglas = ['BA', 'SP', 'MG', 'RJ']
list_oficial = []

for index in range(len(lista_states)):
    list_oficial.append((lista_states[index], list_siglas[index]))

print(list_oficial)

