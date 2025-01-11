"""
Considerando duas listas de inteiros ou flutuantes (lista A e lista B)
Alguns dos valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
==================== resultado
lista_soma = [2, 4, 6, 8]
"""
lista_a = [10, 20, 30, 40, 5, 6, 7]
lista_b = [1, 2, 3, 4]


# - Solução 0.1
def zipper_with_list_compreention(list_1, list_2):
    # Menor lista
    interval_max = (min(len(list_1), len(list_2)))
    return [
        sum((list_1[i], list_2[i])) for i in range(interval_max)
    ]
print(zipper_with_list_compreention(lista_a, lista_b))



# - Solução 0.2 - Melhor. 
list_with_zip = list(zip(lista_a, lista_b))
def sum_the_elements_of_list(list_zip):
    list_oficial_with_sum = []
    for index_tuples_of_list in list_zip:
      summation = sum(index_tuples_of_list)
      list_oficial_with_sum.append(summation)
    return list_oficial_with_sum

print(sum_the_elements_of_list(list_with_zip))