## Combinations, Permutations e Product - Itertools
- Conceitos de matemática. 
- O módulo `itertools` fornece funções para gerar combinações, permutações e produtos cartesianos de elementos iteráveis.  

## 0.1 `combinations()` – Combinações sem repetição
- Gera todas as combinações possíveis de um conjunto, escolhendo um número específico de elementos por vez, **sem repetir a ordem**.  
- iterável + tamanho do grupo.

- Sintaxe  
```python
itertools.combinations(iterável, tamanho)
```
- **`iterável`**: A sequência de elementos.  
- **`tamanho`**: O número de elementos por combinação.  

- Exemplo  
```python
from itertools import combinations

letras = ['A', 'B', 'C']
resultado = list(combinations(letras, 2))

print(resultado)
# Saída: [('A', 'B'), ('A', 'C'), ('B', 'C')]
```
- A ordem **não** importa: `('A', 'B')` é o mesmo que `('B', 'A')`.  

---

## 0.2 `permutations()` – Permutações (todas as ordens possíveis)
- Gera todas as permutações possíveis de um conjunto, levando em conta a ordem dos elementos.  

- Sintaxe 
```python
itertools.permutations(iterável, tamanho)
```
- **`iterável`**: A sequência de elementos.  
- **`tamanho`** *(opcional, padrão `len(iterável)`)**: Número de elementos por permutação.  

- Exemplo
```python
from itertools import permutations

letras = ['A', 'B', 'C']
resultado = list(permutations(letras, 2))

print(resultado)
# Saída: [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
```
- A ordem **importa**: `('A', 'B')` **é diferente** de `('B', 'A')`.  

---

## 0.3 `product()` – Produto Cartesiano (com repetição)  
- Gera todas as combinações possíveis de elementos, **permitindo repetição**.  
- Sintaxe  
```python
itertools.product(iterável1, iterável2, ..., repeat=N)
```
- **`iterável1, iterável2, ...`**: Sequências que serão combinadas.  
- **`repeat`** *(opcional)*: Repete o mesmo iterável N vezes.  

- Exemplo
```python
from itertools import product

num = [1, 2]
letras = ['A', 'B']
resultado = list(product(num, letras))

print(resultado)
# Saída: [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]



```
- Com `repeat`  
```python
resultado = list(product([0, 1], repeat=3))
print(resultado)
# Saída: [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]


```

````py

from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n') # desenpacotar
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
]

print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))
# saida do product:
"""
('preta', 'p')
('preta', 'm')
('preta', 'g')
('branca', 'p')
('branca', 'm')
('branca', 'g')
"""

````
