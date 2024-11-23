
### Métodos de Tuplas
- Tuplas têm poucos métodos disponíveis devido à sua imutabilidade. Os mais comuns são `count()` e `index()`:
- Metodos de listas podem ser usados nas tuplas.

```python
# Contando elementos
print(minha_tupla.count(1))  # Saída: 1

# Encontrando o índice de um elemento
print(minha_tupla.index('abc'))  # Saída: 3
```

## Enumerate() para enumerar valores de iteráveis (pegar índices)
- É uma função embutida que adiciona um contador aos itens de um iterável (como uma lista, tupla, etc.) e retorna um objeto enumerado.
- Ultiização do `for`.
- o Iterator é zerado após o primeiro uso em um `for`. Assim, coloque ele no proprio `for`, como no exemplo abaixo.
- Podemos converter o enuerate em uma lista, retorando tipo tuplas dentro de uma lista.
- Ele criar uma tupla com indice e o valor. 
- O comando `start=indice]_escolhido` dentro do enumerate para começar de uma determinado ponto.

- Exemplo:
```python
cores = ['vermelho', 'verde', 'azul']
for indice, cor in enumerate(cores):
    print(indice, cor)
```
- Saída:
``` 
0 vermelho
1 verde
2 azul
```

``` python
"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

lista_enumerada = list(enumerate(lista))
print(lista_enumerada)

#for item in enumerate(lista):
#   print(item)

# desempacotamento. vai separando o indice e o nome. 
for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)


for tupla_enumerada in enumerate(lista):
     print('FOR da tupla:')
     for valor in tupla_enumerada:
         print(f'\t{valor}')
```

















# Juntar Tuplas: 
- Quando você junta duas ou mais tuplas, você está, na verdade, criando uma nova tupla que contém todos os elementos das tuplas originais em uma sequência. Isso é feito usando o operador de concatenação `+`.

- Exemplo de Junção de Tuplas:
```py
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6, 7)
tupla_junta = tupla1 + tupla2
print(tupla_junta)
```
- Saída:
```
(1, 2, 3, 4, 5, 6, 7)
```

# Método count()
- É utilizado para contar quantas vezes um determinado elemento aparece dentro de uma tupla. A sintaxe é a seguinte:
- Exemplo:
```py
tupla_exemplo = (1, 2, 3, 2, 4, 2)
contagem = tupla_exemplo.count(2)
print(contagem)  # Saída: 3
```

### Método index()
- Usado para encontrar o índice da primeira ocorrência de um elemento específico na tupla. Se o elemento não estiver presente, um erro será gerado. A sintaxe é:
- Exemplo:
```python
tupla_exemplo = (1, 2, 3, 2, 4, 2)
indice = tupla_exemplo.index(2)
print(indice)  # Saída: 1
```

## Método del()
- O comando `del` em Python é usado para deletar objetos, variáveis, itens em listas, ou chaves de dicionários, removendo-os completamente da memória. 
## Exemplos de uso do `del`
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

3. **Deletar uma chave de um dicionário**:
   ```python
   dic = {'a': 1, 'b': 2, 'c': 3}
   del dic['b']  # Remove a chave 'b' do dicionário, resultando em {'a': 1, 'c': 3}
   ```


