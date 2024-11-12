# DEL
O comando `del` em Python é usado para deletar objetos, variáveis, itens em listas, ou chaves de dicionários, removendo-os completamente da memória. 
### Exemplos de uso do `del`

1. **Deletar uma variável**:
   ```python
   x = 10
   del x  # Remove a variável 'x' da memória
   ```

2. **Deletar um elemento específico de uma lista**:
   ```python
   lista = [1, 2, 3, 4]
   del lista[2]  # Remove o elemento no índice 2 (valor 3), resultando em [1, 2, 4]
   ```

3. **Deletar uma fatia de uma lista**:
   ```python
   lista = [1, 2, 3, 4, 5]
   del lista[1:3]  # Remove os elementos de índice 1 a 2, resultando em [1, 4, 5]
   ```

4. **Deletar uma chave de um dicionário**:
   ```python
   dic = {'a': 1, 'b': 2, 'c': 3}
   del dic['b']  # Remove a chave 'b' do dicionário, resultando em {'a': 1, 'c': 3}
   ```

5. **Deletar múltiplas variáveis**:
   ```python
   a, b, c = 1, 2, 3
   del a, b  # Remove 'a' e 'b' da memória
   ```
