### Configurações do `@dataclass`: `frozen=True` e `order=True`
##  **`frozen=True` – Criando classes imutáveis**
- Se `frozen=True`, os atributos não podem ser modificados após a criação do objeto.
- Isso transforma a `dataclass` em uma estrutura **readonly**, útil para garantir que os dados não sejam alterados acidentalmente.

### Exemplo:
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Pessoa:
    nome: str
    idade: int

p1 = Pessoa("Ana", 25)
print(p1)

# Tentando modificar um atributo (gera erro)
p1.idade = 30  # AttributeError: cannot assign to field 'idade'
```

---

##  **`order=True` – Adicionando comparações entre objetos**
- Por padrão, `dataclass` não permite **comparação relacional** (`<`, `>`, `<=`, `>=`).
 Se `order=True`, ele gera automaticamente os métodos:

- `__lt__` (menor que)
- `__le__` (menor ou igual)
- `__gt__` (maior que)
- `__ge__` (maior ou igual)

### Exemplo:
```python
from dataclasses import dataclass

@dataclass(order=True)
class Pessoa:
    idade: int
    nome: str  # A ordem de comparação segue a ordem dos atributos!

p1 = Pessoa(25, "Ana")
p2 = Pessoa(30, "Bruno")

print(p1 < p2)  # True (compara primeiro pela idade)
print(p1 > p2)  # False
```

---


