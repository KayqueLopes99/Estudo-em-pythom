# set são conjuntos.
# Crienado um set.
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# s1 = set() # vazio
# s1 = {'Luiz', 1, 2, 3} # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)


lista1 = [1, 2, 3, 3, 3, 3, 3, 1]
sep_1 = set(lista1)
lista2 = list(sep_1)
sep_1 = {1, 2, 3}
print(3 in sep_1)
print(3 not in sep_1)
for numero in sep_1:
    print(numero)

s1 = set()
s1.add('Luiz')
s1.add(1)
s1.update(('Olá Mundo', 1, 2, 3, 4))
# s1.clear()
s1.discard(1)
# print(s1)

print()

sep_01 = {1, 2, 3}
sep_02 = {2, 3, 4}

sep_03_operacao = sep_01 | sep_02
print(sep_03_operacao)
sep_03_operacao = sep_01 & sep_02
print(sep_03_operacao)
sep_03_operacao = sep_02 - sep_01
print(sep_03_operacao)
sep_03_operacao = sep_01 ^ sep_02
print(sep_03_operacao)