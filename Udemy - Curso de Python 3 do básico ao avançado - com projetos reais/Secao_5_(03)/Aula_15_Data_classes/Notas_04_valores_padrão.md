##  Valores padrão, field e fields em dataclasses
+ 1. **Valores Padrão**
- **se um atributo tem valor padrão, todos os atributos definidos depois dele também devem ter valor padrão** — isso é uma regra da linguagem, não só de dataclasses.

### Errado:
```python
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str = "José"
    idade: int  # Erro! Deve vir antes de atributos com default
```

### Certo:
```python
@dataclass
class Pessoa:
    idade: int
    nome: str = "José"

# OU

@dataclass
class Pessoa:
    nome: str = "José"
    idade: int = 0
```

---

+ 2. `field()`: Customizações dos campos

- A função `field()` é usada quando você quer **configurar atributos** além do valor padrão, como:

- `default`: Define um valor padrão.
- `default_factory`: Define um valor padrão usando uma função (como listas, dicts, etc).


###  `default`
+ Usado para tipos imutáveis:

```python
from dataclasses import dataclass, field

@dataclass
class Pessoa:
    nome: str = field(default="José")
    idade: int = field(default=25)
```

###  `default_factory`
+ Usado com tipos **mutáveis**, como listas ou dicionários:

```python
from dataclasses import dataclass, field

@dataclass
class Turma:
    alunos: list = field(default_factory=list)  # Garante lista nova para cada instância
```

- `fields()`: Inspeciona os campos dadataclass. Para reflexão ou debug.
