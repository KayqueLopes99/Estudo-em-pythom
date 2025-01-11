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

from itertools import zip_longest
lista_states = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list_siglas = ['BA', 'SP', 'MG', 'RJ']

# Eu - 
def zipper(list_1, list_2):
    list_oficial = []
    for index in range(min(len(list_1), len(list_2))):
       list_oficial.append((list_1[index], list_2[index]))
    return list_oficial


# Aula -
def zipper_with_list_compreention(list_1, list_2):
    interval_max = (min(len(list_1), len(list_2)))
    return [
        (list_1[i], list_2[i]) for i in range(interval_max)
    ]


print(zipper(lista_states, list_siglas))
print(zipper_with_list_compreention(lista_states, list_siglas))


print(list(zip(lista_states, list_siglas)))
print(list(zip_longest(lista_states, list_siglas)))
