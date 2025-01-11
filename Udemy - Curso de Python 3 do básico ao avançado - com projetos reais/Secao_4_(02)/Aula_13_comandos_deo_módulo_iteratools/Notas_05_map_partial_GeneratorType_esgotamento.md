## map, partial, GeneratorType e esgotamento de Iterators
## 0.1 `map()`:
- O `map()` é uma função embutida no Python usada para aplicar **uma função** a **todos os elementos** de um iterável (como uma lista ou tupla), sem precisar usar um `for`.
- Mapeamento significa transformar cada elemento de uma lista em outra coisa. Por exemplo, se temos uma lista de números e queremos dobrá-los, estamos mapeando cada número para o seu dobro.
- Vai percorrer de um em um elemento.
- list_compreention.
- Sintaxe
```python
map(funcao, iteravel)
```
- **`funcao`**: A função que será aplicada a cada elemento.
- **`iteravel`**: A sequência de valores (lista, tupla, etc.).

- O `map()` retorna um objeto do tipo `map` (um iterador), então geralmente é convertido para `list()` ou `tuple()`.
---
- Exemplos: 

+ Usando `for`
```python
numeros = [1, 2, 3, 4, 5]
dobrados = []

for num in numeros:
    dobrados.append(num * 2)

print(dobrados)  # [2, 4, 6, 8, 10]
```

+ Usando `map()`
```python
numeros = [1, 2, 3, 4, 5]

dobrados = map(lambda x: x * 2, numeros)

print(list(dobrados))  # [2, 4, 6, 8, 10]
```
---

## 0.2 `functools.partial()`:
- A função `partial()` do módulo `functools` permite **pré-configurar** uma função, fixando alguns dos seus argumentos. 

- Semilar a uma closure, pois ela é uma função que recebe uma função e um ou varios dos argumentos da sua função vai ser fixo.

- Sintaxe
```python
from functools import partial

nova_funcao = partial(funcao, arg1, arg2, ...)
```

#### **Exemplo**
```python
from functools import partial

def potencia(base, expoente):
    return base ** expoente

quadrado = partial(potencia, expoente=2)
print(quadrado(3))  # 9

cubo = partial(potencia, expoente=3)
print(cubo(2))  # 8
```
- `quadrado(3)` equivale a `potencia(3, 2)` e `cubo(2)` equivale a `potencia(2, 3)`.
---

## 0.3 `GeneratorType`:
- Os geradores são uma forma eficiente de lidar com grandes quantidades de dados sem carregá-los todos na memória. Eles são criados com `yield` ou expressões geradoras.

- O tipo `GeneratorType` pode ser verificado no módulo `types`.

```python
from types import GeneratorType

def meu_gerador():
    yield 1
    yield 2
    yield 3

gen = meu_gerador()
print(isinstance(gen, GeneratorType))  # True
```

- Um gerador produz valores conforme necessário e mantém o estado entre chamadas.
---

### 4. **Esgotamento de Iterators**
- Iteradores no Python são objetos que podem ser percorridos uma vez. Após serem completamente iterados, ficam esgotados e não retornam mais valores.

```python
numeros = iter([10, 20, 30])

print(next(numeros))  # 10
print(next(numeros))  # 20
print(next(numeros))  # 30
# print(next(numeros))  # StopIteration (se descomentar)

# O iterador está esgotado
print(list(numeros))  # []
```
- Reutilizar converta em lista.