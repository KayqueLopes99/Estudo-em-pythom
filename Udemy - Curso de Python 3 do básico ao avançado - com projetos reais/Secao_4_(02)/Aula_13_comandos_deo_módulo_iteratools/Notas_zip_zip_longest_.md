## zip e zip_longest do itertools
- Solução do Exercício `Aula_45.py`:
```py
from itertools import zip_longest
lista_states = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list_siglas = ['BA', 'SP', 'MG', 'RJ']

# Eu - 
def zipper(list_1, list_2):
    list_oficial = []
    for index in range(min(len(list_1), len(list_2))):
       list_oficial.append((list_1[index], list_2[index]))
    return list_oficial


# Aula -
def zipper_with_list_compreention(list_1, list_2):
    interval_max = (min(len(list_1), len(list_2)))
    return [
        (list_1[i], list_2[i]) for i in range(interval_max)
    ]


print(zipper(lista_states, list_siglas))
print(zipper_with_list_compreention(lista_states, list_siglas))


print(list(zip(lista_states, list_siglas)))
print(list(zip_longest(lista_states, list_siglas)))

```

---

###  0.1 `zip()`:
- A função `zip()` combina elementos de **múltiplas sequências** até o comprimento da **menor** delas. 
- Se uma lista for menor que outra, os elementos excedentes da maior **serão ignorados**.  
- Usa todos os valores da  lista menor, e o restante dos valores da lista maior são ignorados.

+ Sintaxe:
```python
zip(iterável1, iterável2, ...)
```
- **`iterável1, iterável2, ...`**: São as listas ou outras estruturas que queremos combinar.  
- Retorna um **iterador** que pode ser convertido em lista ou tuplas.  
- Um iterador é um objeto que permite percorrer elementos de uma sequência (como listas, tuplas e dicionários) um por um, sem precisar carregar todos os elementos na memória de uma vez.

```python
nomes = ["Ana", "Carlos", "Maria"]
idades = [25, 30, 22, 23]

combinado = list(zip(nomes, idades))
print(combinado)
```
```python
[('Ana', 25), ('Carlos', 30), ('Maria', 22)] # ignorou o 23, so considera os da enor lista.
```

---

### 0.2. `zip_longest()` do módulo `itertools`**
- O `zip_longest()` funciona como o `zip()`, **mas não trunca os elementos** da sequência maior.  
- Caso um iterável seja mais curto, ele preenche os valores faltantes com um **valor padrão** (por padrão, `None`).
- Usa o valor da lista *Maior*, ele usa todos os valores da lista menor e da maior e se algum valor da lista maior sobrar (restantes) ele é prenchido com None ou outra coisa escolhida.
+ Sintaxe:
```python
from itertools import zip_longest
itertools.zip_longest(iterável1, iterável2, ..., fillvalue=valor)
```
- **`iterável1, iterável2, ...`** ; Listas ou sequências que serão combinadas.  
- **`fillvalue=valor`** : Valor que será usado para preencher os elementos faltantes na lista menor (opcional, `None` por padrão).  

```python
from itertools import zip_longest

nomes = ["Ana", "Carlos", "Maria"]
idades = [25, 30]

combinado = list(zip_longest(nomes, idades, fillvalue="Sem idade"))
print(combinado)
```
**🔹 Saída:**
```python
[('Ana', 25), ('Carlos', 30), ('Maria', 'Sem idade')]
```

## Exercicio `Aula_46.py`
- Solução com zip_longest

```py
from itertools import zip_longest
 
lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma)  # [22, 4, 6, 10, 55, 60, 70]

```
- Neste caso, usamos o "fillvalue" como 0 (zero), assim conseguimos capturar os valores restantes da lista maior, realizando contas, sem obter um erro em nosso programa.