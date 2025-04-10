##  `dataclasses` – Explicação 
### **O que é?**:
- `dataclasses` é um módulo introduzido no Python 3.7 (PEP 557) que fornece uma forma mais **concisa** e **automática** de criar classes que armazenam dados.
-  Ao usar o decorador `@dataclass`, o Python gera automaticamente métodos comuns que você teria que escrever manualmente em classes tradicionais, como:
- é um Açúcar sintatico: Resume!
- Importação: `from dataclasses import dataclass`.

- `__init__()` → para inicializar os atributos  
- `__repr__()` → para representação textual (útil para debug)  
- `__eq__()` → para comparar objetos  
- `__hash__()` → para uso em dicionários e conjuntos (opcional)

---

### **Por que usar?**:

- Imagine que você precise de uma classe para representar uma pessoa:

```python
# Sem dataclass
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f"Pessoa(nome={self.nome}, idade={self.idade})"
```

- Com `dataclass`, isso se torna:

```python
from dataclasses import dataclass

@dataclass
class Pessoa:
#   variavel: tipo
    nome: str
    idade: int
```

- Muito mais limpo, fácil de manter e **menos repetição de código**!

---

### 🛠️ **Funcionalidades extras**

- Suporte a **valores padrão**:
```python
@dataclass
class Produto:
    nome: str
    preco: float = 0.0
```

- Suporte a **tipos imutáveis** (como `namedtuple`) com `frozen=True`:
```python
@dataclass(frozen=True)
class Coordenada:
    x: float
    y: float
```

- Comparações automáticas:
```python
a = Pessoa("Ana", 20)
b = Pessoa("Ana", 20)
print(a == b)  # True
```

---

### 📚 Documentação oficial:
- https://docs.python.org/3/library/dataclasses.html

---
 
###  `__init__` e `__post_init__` em `dataclasses`  

- O módulo `dataclasses` simplifica a criação do método `__init__()` automaticamente, mas também permite modificar sua lógica com o método especial `__post_init__()`. 

+ | `__init__` | Chamado automaticamente pelo `dataclass` para inicializar os atributos. | Define os atributos com os valores passados. |
+ | `__post_init__` | Chamado **depois** do `__init__`. | Permite ajustes ou validações adicionais. |
---

## **`__init__` no `dataclass`**  
- Quando você usa `@dataclass`, o Python gera automaticamente o método `__init__()` com base nos atributos definidos.
- Quiser manter o init colocar: `@dataclass(init=False)`-> voCê faz o init.


## **`__post_init__` – Ajustes pós-inicialização**  
- Se precisarmos **modificar ou validar os atributos após a inicialização**, usamos `__post_init__()`.

Exemplo prático:
```python
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int

    def __post_init__(self):
        # Corrige para deixar o nome sempre com a primeira letra maiúscula
        self.nome = self.nome.title()

        # Garante que a idade seja um número positivo
        if self.idade < 0:
            raise ValueError("A idade não pode ser negativa!")

# Teste
p1 = Pessoa("ana", 25)
print(p1)  # Pessoa(nome='Ana', idade=25)

p2 = Pessoa("maria", -5)  # Gera um ValueError
```



