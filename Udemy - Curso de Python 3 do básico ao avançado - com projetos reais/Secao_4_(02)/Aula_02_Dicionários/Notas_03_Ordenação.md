## O comando **`sorted()`**

1. **Ordenação Simples com `sorted()`**:
   Para ordenar uma lista ou outro iterável em ordem ascendente, você pode usar a função `sorted()`. Por exemplo:
   ```python
   lista = [5, 2, 3, 1, 4]
   lista_ordenada = sorted(lista)
   print(lista_ordenada)  # Saída: [1, 2, 3, 4, 5]
   ```

2. **Ordenação Decrescente com `sorted()`**:
   Se você deseja ordenar em ordem decrescente, basta definir o parâmetro `reverse=True`:
   ```python
   lista_decrescente = sorted(lista, reverse=True)
   print(lista_decrescente)  # Saída: [5, 4, 3, 2, 1]
   ```

3. **Ordenação de Dicionários por Valor usando `operator.itemgetter()`**:
   Para ordenar um dicionário por valor, você pode usar a função `sorted()` em conjunto com `operator.itemgetter(1)` (onde `1` representa o índice do valor ou 0 para chaves). Veja um exemplo:
   ```python
   import operator
   
   exemplo_dict = {'first': 3, 'second': 4, 'third': 2, 'fourth': 1}
   dict_ordenado_por_valor = sorted(exemplo_dict.items(), key=operator.itemgetter(1))
   print(dict_ordenado_por_valor)
   # Saída: [('fourth', 1), ('third', 2), ('first', 3), ('second', 4)]
   ```
   Nesse exemplo, o dicionário foi convertido em uma lista de tuplas (chave, valor) e ordenado com base no val