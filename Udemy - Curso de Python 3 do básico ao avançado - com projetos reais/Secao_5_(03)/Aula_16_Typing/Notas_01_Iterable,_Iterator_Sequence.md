## Criando sua própria lista com Iterable, Iterator e Sequence (collections.abc)
- Introduduzindo os protocolos. 
- Essas classes fazem parte do módulo `collections.abc` e servem como **interfaces** (ou contratos) que dizem:  
> "Se você quer ser tratado como uma lista, ou um iterador, siga essas regras."
- Obriga a definir os métodos esperados dos módulos na herança. 
---

## 1. `Iterable`
- Um **iterable** é qualquer objeto que pode ser percorrido com um `for` (como listas, strings, etc). Para isso, ele precisa implementar o método:

```python
__iter__(self)
```

- Esse método deve **retornar um iterador**.

---

## 2. `Iterator`
- Um **iterador** precisa ter dois métodos:

```python
__iter__(self)
__next__(self)
```

- `__iter__()` retorna o próprio objeto.
- `__next__()` retorna o próximo item, e lança `StopIteration` quando acabar.

---

## 3. `Sequence`
- Herda de `Iterable` e adiciona comportamento de sequência (como lista, tupla). Você deve implementar:

```python
__getitem__(self, index)
__len__(self)
```


## Implementanda uma sequence
```py
from collections.abc import Sequence

class MyList(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0
        # Índice auxiliar para controle da iteração (__next__)
        self._next_index = 0

    def funcion_append(self, *values):
        # Adiciona um ou mais valores à estrutura, armazenando no dicionário
        for value in values: 
            self._data[self._index] = value
            self._index += 1  

    def __len__(self):
        # Retorna o número de elementos armazenados
        return self._index

    def __getitem__(self, index):
        # Retorna o item correspondente ao índice
        return self._data[index]

    def __setitem__(self, index, value):
        # Atualiza o valor em um índice específico
        self._data[index] = value

    def __iter__(self):
        # Retorna a própria instância como iterador (padrão Python)
        return self

    def __next__(self):
        # Define a lógica para iteração com 'for' ou 'next()'
        if self._next_index >= self._index:
            # Zera ele para realizar a Iteração mais um vez
            self._next_index = 0 
            raise StopIteration

        # Retorna o próximo valor e avança o índice
        value = self._data[self._next_index]
        self._next_index += 1
        return value


if __name__ == '__main__':
    list_the_data = MyList()

    list_the_data.funcion_append("Kayque", "Samuel")
    list_the_data.funcion_append("Daniel")

    # Atualiza diretamente um valor da estrutura
    list_the_data[2] = 'Daniel Costa'

    # Mostra o dicionário interno
    print(list_the_data._data)

    # Percorre os dados usando o protocolo de iteração
    for item in list_the_data:
        print(item)

    

```