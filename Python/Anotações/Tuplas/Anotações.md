# Varíaveis Compostas: Tuplas.
## Conceito
- Em uma Declaração de uma varíavel com atribuição de valor, só podemos atribuir uma coisa para ela.
- Exemplo:
> Lanche = bolo

> lanche = suco X 
- Não podemos atribuir suco, pois ele irá substituir o bolo atribuido. 
- Logo tem-se essa necessidade.
- Isso é possivel com as Tuplas.

## Construção
- Uma Tupla é uma varíavel que guarda diferentes valores(elementos).
- Acessamos cada elemento pelo seu índice correspondente.
- A tupla não pode ser alterada - você não pode adicionar, remover ou modificar os elementos.

### Acessando Elementos
- Usando índices, começando do zero:

```python
# Acessando o primeiro elemento (índice 0)
print(minha_tupla[0])  # Saída: 1

# Acessando o último elemento (índice -1)
print(minha_tupla[-1]) # Saída: True
```
- Fatiamento: O fatiamento permite acessar subconjuntos de uma tupla usando índices.

```Python
subtupla = nome_da_tupla[inicio:fim]
```

- Por exemplo, se você tem uma tupla t = (0, 1, 2, 3, 4, 5)
- subtupla = t[1:4]  -> Isso retornará (1, 2, 3)
- subtupla = t[2]  -> Isso retornará (2)
- subtupla = t[1:]  -> Isso retornará (1, 2, 3, 4, 5)
- subtupla = t[-1]  -> Isso retornará ao ultimo elemento(5)

## Usando len(string):
- Usamos para saber quantos elemetos tem a tupla.

## Usando Estrutura de Repetição:
- Para percorrer.
- Irá acessar cada elemeto.
- Exemplo:
```python
for c in tupla: # ATÉ O FIM DA TUPLA.
    print(c)
```


### Sintaxe
A sintaxe para criar uma tupla é simples. 

```python
# SINTAXE: 
nome_da_tupla = (elemento1, elemento2, elemento3, ...)
subtupla = nome_da_tupla[inicio:fim]

# Criando uma tupla vazia
tupla_vazia = ()

# Criando uma tupla com um único elemento (note a vírgula)
tupla_solo = (42,)

# Criando uma tupla com múltiplos elementos
minha_tupla = (1, 2, 3, 'abc', True)
```


### Imutabilidade

```python
minha_tupla[0] = 10  # Isso causará um TypeError
```

### Desempacotamento de Tuplas
O desempacotamento permite atribuir os valores de uma tupla a várias variáveis:

```python
# Desempacotando uma tupla
x, y, z, a, b = minha_tupla
print(x)  # Saída: 1
print(y)  # Saída: 2
```

### Métodos de Tuplas
Tuplas têm poucos métodos disponíveis devido à sua imutabilidade. Os mais comuns são `count()` e `index()`:

```python
# Contando elementos
print(minha_tupla.count(1))  # Saída: 1

# Encontrando o índice de um elemento
print(minha_tupla.index('abc'))  # Saída: 3
```

# Enumerate
- É uma função embutida que adiciona um contador aos itens de um iterável (como uma lista, tupla, etc.) e retorna um objeto enumerado.

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


# Sorted (Ordenação):
- É uma função embutida que retorna uma nova lista dos elementos de um iterável, ordenados.

- Exemplo:
```python
numeros = [3, 1, 4, 1, 5, 9, 2]
print(sorted(numeros))
```
- Saída:
```
[1, 1, 2, 3, 4, 5, 9]
```

- Exemplo:
```python
palavras = ['banana', 'abacate', 'damasco', 'cereja']
print(sorted(palavras))
```
- Saída:
```
['abacate', 'banana', 'cereja', 'damasco']
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

# del
- Comando para Deletar ou apagar por completo.
``` py
tupla = (1, 2, 3, 4)
del tupla  # Deleta a tupla inteira
```
