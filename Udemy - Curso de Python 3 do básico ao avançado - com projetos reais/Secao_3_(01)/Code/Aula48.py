#        +01234
#        -54321
string = 'ABCDE' # 5 CARACTERES COM len().
lista = list
print(bool([])) # falsy
print(lista, type(lista))


#         0    1       2       3     4
#        -5   -4      -3      -2    -1
lista = [19, True, 'Kayque', 22.12, []]
lista[1] = False # -> Alteração + Acesso.
print(lista)
print(lista[1], type(lista[2]))


lista_02 = [10, 20, 30, 40]
# lista_02[2] = 300
# del lista_02[2]
# print(lista_02)
# print(lista_02[2])
lista_02.append(50)
lista_02.pop()
lista_02.append(60)
lista_02.append(70)
ultimo_valor = lista_02.pop(3)
print(lista_02, 'Removido,', ultimo_valor)


lista_03 = [10, 20, 30, 40]
lista_03.append('Kay')
nome = lista_03.pop()
lista.append(1233)

del lista[-1]
# lista.clear()
lista_03.insert(100, 5)
print(lista_03[4])
# Buscar item fora do range: ERRO
# Colocar um índice grande ele coloca no final da lista.


lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)


"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)