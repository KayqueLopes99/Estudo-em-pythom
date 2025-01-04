# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
lista_01 = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
     {'nome': 'Daniel', 'sobrenome': 'Silva'},
     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
     {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def ordena(item):
    return item['nome']


# OU

# Ordenar pelo nome (alfabetica)
lista_01.sort(key=lambda item: item['nome'])

for item in lista_01:
    print(item)



lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
lista.sort(reverse=True)
print(lista)
sorted(lista)





lista_02 = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]



def exibir(lista):
    for item in lista:
        print(item)
    print()



l1 = sorted(lista_02, key=lambda item: item['nome'])
l2 = sorted(lista_02, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)