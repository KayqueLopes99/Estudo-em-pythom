## Métodos Matemáticos
##  `sum()`
A função `sum()` calcula a soma de todos os elementos em um iterável. Pode incluir um valor inicial opcional para a soma.

- Sintaxe:
```python
sum(iterable, start=0)
```
- `iterable`: Iterável cujos elementos serão somados.
- `start`: (Opcional) Valor inicial para a soma (padrão é 0).

- Exemplo:
```python
numeros = [10, 20, 30]
resultado = sum(numeros)
print(resultado)  # Saída: 60

# Soma com valor inicial:
resultado_com_inicial = sum(numeros, 5)
print(resultado_com_inicial)  # Saída: 65
```


## `max()`
- A função `max()` retorna o maior elemento de um iterável ou entre os valores fornecidos.

- Sintaxe:
```python
max(iterable)
max(valor1, valor2, ...)
```

- Exemplo:
```python
numeros = [10, 20, 30]
maior = max(numeros)
print(maior)  # Saída: 30

# Comparando valores diretamente:
maior_direto = max(5, 15, 25)
print(maior_direto)  # Saída: 25
```


## `min()`
- A função `min()` retorna o menor elemento de um iterável ou entre os valores fornecidos.

- Sintaxe:
```python
min(iterable)
min(valor1, valor2, ...)
```

- Exemplo:
```python
numeros = [10, 20, 30]
menor = min(numeros)
print(menor)  # Saída: 10

# Comparando valores diretamente:
menor_direto = min(5, 15, 25)
print(menor_direto)  # Saída: 5
```


## max e min *observação*:
- Podem retornar a maior ou menor estrutura de dado.
- Retornar a menor ou maior estrutura pelo tamanho com auxilio do len(). 
```py
lista_states = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list_siglas = ['BA', 'SP', 'MG', 'RJ']

def zipper(list_1, list_2):
    list_oficial = []
    for index in range(min(len(list_1), len(list_2))):
       list_oficial.append((list_1[index], list_2[index]))
    return list_oficial

print(zipper(lista_states, list_siglas))

```