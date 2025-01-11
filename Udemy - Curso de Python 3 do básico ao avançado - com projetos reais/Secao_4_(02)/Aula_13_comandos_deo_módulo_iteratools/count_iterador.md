## `count()` do módulo `itertools` – Um Iterador Infinito  
- O `count()` é uma função do módulo `itertools` que gera um iterador infinito, começando de um valor inicial e incrementando a cada passo.
- Ele é útil para gerar sequências numéricas automaticamente, sem precisar de um loop `while` ou `for` com contadores manuais.  
- É utilizado para contar quantas vezes um determinado elemento aparece dentro de uma estrutura como lista e tupla e mais outras. A 
- Está no módulo (itertools)

- *O range é iteravel e não é um iterator*: Tem fim.
+ Sintaxe 
```python
from itertools import count
itertools.count(start=0, step=1)
```
- **`start`** *(opcional, padrão `0`)*: O valor inicial da contagem.  
- **`step`** *(opcional, padrão `1`)*: O valor pelo qual cada próximo número será incrementado. Pode ser negativo para contar para trás.  

---


- Exemplos:
```py
tupla_exemplo = (1, 2, 3, 2, 4, 2)
contagem = tupla_exemplo.count(2)
print(contagem)  # Saída: 3
```

```python
from itertools import count

contador = count(start=5, step=2)  # Começa no 5 e incrementa de 2 em 2

for _ in range(5):  # Pegamos apenas os primeiros 5 valores para evitar loop infinito
    print(next(contador))

# Saída:
# 5
# 7
# 9
# 11
# 13
```


````py
from itertools import count

c1 = count(start=8, step=8)
r1 = range(1,11)

print('c1', hasattr(c1, '__iter__')) # iteravel
print('c1', hasattr(c1, '__next__')) # Iterator
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

print("Count")
for index in c1: # index = next.
    if index > 100:
        break
    print(index, end=' ')

print()

print("Range")
for index in r1: # index = next.
    print(index, end=' ')

````