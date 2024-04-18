# Biblioteca Random em Python

A biblioteca `random`  implementa geradores de números pseudoaleatórios para várias distribuições.

## random.random()

Esta função retorna o próximo número de ponto flutuante no intervalo [0.0, 1.0).

```python
import random
print(random.random())
```

## random.randint(a, b)

Esta função retorna um número inteiro aleatório N de tal forma que a <= N <= b.

```python
import random
print(random.randint(1, 10))
```

## random.choice(seq)

Esta função retorna um elemento aleatório de uma sequência não vazia.

```python
import random
print(random.choice(['apple', 'banana', 'cherry', 'date']))
```

## random.shuffle(seq)

Esta função embaralha os elementos de uma lista no local.

```python
import random
fruits = ['apple', 'banana', 'cherry', 'date']
random.shuffle(fruits)
print(fruits)
```