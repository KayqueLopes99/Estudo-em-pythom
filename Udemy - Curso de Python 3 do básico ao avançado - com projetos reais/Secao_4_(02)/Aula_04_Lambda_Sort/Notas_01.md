## Introdução à função lambda + list.sort e sorted
- A função lambda é uma função como qualquer outra em Python. Porém, são funções anônimas que contém apenas uma linha. Ou seja, tudo deve ser contido dentro de uma únca expressão. 

- Usadas com métodos como **`list.sort()`** e a função **`sorted()`** para personalizar a ordenação de listas.  

- Sintaxe
```python
lambda argumentos: expressão_retornada, valores_atribuidos
```
- **`lambda`** cria uma função anônima.
- **`argumentos`** são os parâmetros da função.
- **`expressão`** é a operação retornada.

- Exemplo
```python
soma = lambda x, y: x + y
print(soma(3, 4))  # Saída: 7
```
A função `lambda` acima é equivalente a:
```python
def soma(x, y):
    return x + y
```


##  `sort()`:  
- Sintaxe:
```python
lista.sort(key=None, reverse=False)
```
- **`key`**: Função usada para personalizar a ordenação (opcional).
- **`reverse`**: `True` para ordenar em ordem decrescente, `False` para crescente (padrão).

- Ordenação Crescente**
```python
numeros = [5, 3, 8, 2, 4]
numeros.sort()
print(numeros)  # Saída: [2, 3, 4, 5, 8]
```

- Ordenação Decrescente**
```python
numeros = [5, 3, 8, 2, 4]
numeros.sort(reverse=True)
print(numeros)  # Saída: [8, 5, 4, 3, 2]
```

---

## `sorted()`: Criação de nova lista ordenada **copia rasa**
- Sintaxe
```python
nova_lista = sorted(iterável, key=None, reverse=False)
```
- Funciona com **qualquer iterável** (listas, tuplas, dicionários, etc.).
- **Retorna** uma nova lista ordenada sem modificar o original.

- Ordenação Crescente
```python
numeros = [5, 3, 8, 2, 4]
nova_lista = sorted(numeros)
print(nova_lista)  # Saída: [2, 3, 4, 5, 8]
print(numeros)  # A lista original permanece inalterada: [5, 3, 8, 2, 4]
```

- Ordenação Decrescente
```python
numeros = [5, 3, 8, 2, 4]
nova_lista = sorted(numeros, reverse=True)
print(nova_lista)  # Saída: [8, 5, 4, 3, 2]
```

- Ordenando Dicionários
```py

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
```
- A ordenação alfabetica depende da `unicode` do python maisculas e depois as minusculas. 