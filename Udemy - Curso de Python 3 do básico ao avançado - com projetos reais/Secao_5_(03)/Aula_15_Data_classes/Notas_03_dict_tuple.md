## `dataclasses.asdict` e `dataclasses.astuple`
- Essas funções fazem parte do módulo `dataclasses`.
- Antes de usar essas funções, é preciso importar o módulo `dataclasses` e marcar a classe com o decorador `@dataclass`.

---

### `asdict`

- A função `asdict()` converte uma instância de uma data class em um **dicionário** (`dict`), onde as **chaves** são os nomes dos atributos e os **valores** são os respectivos valores.


```python
from dataclasses import asdict

asdict(objeto_data_class)
```

```python
from dataclasses import dataclass, asdict

@dataclass
class Pessoa:
    nome: str
    idade: int

p = Pessoa("José", 22)
print(asdict(p))  # Saída: {'nome': 'José', 'idade': 22}
```

---

### `astuple`

- A função `astuple()` converte a instância de uma data class em uma **tupla** (`tuple`) com os valores dos atributos na **ordem em que foram definidos**.


```python
from dataclasses import astuple

astuple(objeto_data_class)
```


```python
from dataclasses import dataclass, astuple

@dataclass
class Pessoa:
    nome: str
    idade: int

p = Pessoa("José", 22)
print(astuple(p))  # Saída: ('José', 22)
```

---

### OBS: 
- Não funcionam com classes que **não** são `@dataclass`.

