## **`groupby` – Agrupando Valores (`itertools`)**   
- Cuidado com as repetições de código. 
- Agrupa elementos consecutivos de um iterável que possuem o mesmo valor ou atendem a um critério específico.  
- Sintaxe  
```python
itertools.groupby(iterável, chave=None)
```
- **`iterável`**: A sequência de elementos a ser agrupada.  
- **`chave`** *(opcional)*: Uma função que define o critério de agrupamento.  
- **IMPORTANTE**: Para que `groupby` funcione corretamente, os elementos devem estar **ordenados** pelo critério de agrupamento (*sort* ou *sorted*).

- Agrupando valores repetidos 
```python
from itertools import groupby

dados = [1, 1, 2, 2, 2, 3, 3, 4]
agrupado = groupby(dados)

for chave, grupo in agrupado:
    print(f"{chave}: {list(grupo)}")
```
**🔹 Saída:**  
```
1: [1, 1]
2: [2, 2, 2]
3: [3, 3]
4: [4]
```
  

---

- Agrupando por uma função (par ou ímpar)
```python
from itertools import groupby

numeros = [1, 2, 2, 3, 4, 4, 5, 6]

# Função para classificar números como par (0) ou ímpar (1)
def par_ou_impar(n):
    return n % 2

agrupado = groupby(numeros, key=par_ou_impar)

for chave, grupo in agrupado:
    tipo = "Ímpares" if chave == 1 else "Pares"
    print(f"{tipo}: {list(grupo)}")
``` 
```
Ímpares: [1]
Pares: [2, 2]
Ímpares: [3]
Pares: [4, 4]
Ímpares: [5]
Pares: [6]
```
---

+ Exemplo Da Aula:
```py
from itertools import groupby
from copy import deepcopy
students_list = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

def ordenation_for_key(students_data):
    return students_data['nota']

students_list.sort(key=ordenation_for_key)
students_grouped = groupby(students_list, key=ordenation_for_key)

for chave, grupo in students_grouped:
    print(chave)
    for aluno in grupo:
        print(aluno)


```
